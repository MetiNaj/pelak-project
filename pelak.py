import cv2
import numpy as np
import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# Load YOLO
yolo_weights = "yolov3.weights"  # Replace with your weights file path
yolo_config = "yolov3.cfg"  # Replace with your config file path
yolo_names = "coco.names"  # Replace with your names file path

net = cv2.dnn.readNet(yolo_weights, yolo_config)
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Load class labels
with open(yolo_names, "r") as f:
    classes = [line.strip() for line in f.readlines()]

def recognize_vehicle(frame):
    height, width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    plate_number = ""
    vehicle_type = ""
    vehicle_color = ""

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = (0, 255, 0)  # Green color for bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)

            # Collect data based on detected classes
            if "license plate" in label.lower():
                plate_number = label  # Customize according to your needs
            else:
                vehicle_type = label
                vehicle_color = "Unknown"  # This can be improved with more logic

    # Formatting the license plate number output
    if plate_number:
        plate_number = f"شماره پلاک = {plate_number}"

    return plate_number, vehicle_type, vehicle_color

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'output.txt')

    # Open the output file with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            plate_number, vehicle_type, vehicle_color = recognize_vehicle(frame)

            # Log the detected information
            if plate_number:
                f.write(f"{plate_number}\n")
            if vehicle_type:
                f.write(f"نوع خودرو: {vehicle_type}\n")
            if vehicle_color:
                f.write(f"رنگ خودرو: {vehicle_color}\n")

        cap.release()
    return output_file


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(video_path)

        # Process the uploaded video
        output_file = process_video(video_path)
        return f'Video processed. Results saved in {output_file}'

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
