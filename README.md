<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vehicle License Plate Recognition System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2, h3, h4 {
            color: #4CAF50;
        }
        code {
            background-color: #e8e8e8;
            padding: 5px;
            border-radius: 5px;
        }
        pre {
            background-color: #e8e8e8;
            padding: 10px;
            border-radius: 5px;
            overflow: auto;
        }
        ul {
            list-style-type: square;
            margin: 10px 0;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .section {
            margin-bottom: 20px;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            font-size: 0.9em;
            color: #777;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Vehicle License Plate Recognition System</h1>

    <div class="section">
        <h2>Introduction</h2>
        <p>This project is a <strong>Vehicle License Plate Recognition System</strong> built using Python, OpenCV, and Flask. The application allows users to upload a video file, which is then processed to detect vehicles, recognize their types, colors, and license plates. The results are saved in a text file, providing a clear overview of detected vehicles.</p>
        <p>این پروژه یک <strong>سیستم شناسایی پلاک خودرو</strong> است که با استفاده از پایتون، OpenCV و Flask ساخته شده است. این برنامه به کاربران اجازه می‌دهد تا یک فایل ویدئویی را بارگذاری کنند، که سپس برای شناسایی خودروها، تشخیص نوع، رنگ و پلاک آن‌ها پردازش می‌شود. نتایج در یک فایل متنی ذخیره می‌شوند و نمای واضحی از خودروهای شناسایی شده ارائه می‌دهند.</p>
    </div>

    <div class="section">
        <h2>Features</h2>
        <ul>
            <li>Upload video files for processing.</li>
            <li>Detect vehicle types (car, truck, motorcycle, etc.).</li>
            <li>Recognize vehicle colors (basic color detection).</li>
            <li>Identify license plates using YOLO (You Only Look Once) object detection.</li>
            <li>Save results in a structured text file.</li>
            <li>User-friendly web interface built with Flask.</li>
        </ul>
        <ul>
            <li>بارگذاری فایل‌های ویدئویی برای پردازش.</li>
            <li>شناسایی نوع خودروها (خودرو، کامیون، موتورسیکلت و غیره).</li>
            <li>شناسایی رنگ خودروها (تشخیص رنگ‌های پایه).</li>
            <li>شناسایی پلاک‌های خودرو با استفاده از YOLO (شناسایی اشیاء فقط یک بار).</li>
            <li>ذخیره نتایج در یک فایل متنی ساختارمند.</li>
            <li>رابط کاربری دوستانه وب ساخته شده با Flask.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Prerequisites</h2>
        <p>Before running the project, ensure you have the following installed:</p>
        <ul>
            <li>Python 3.x</li>
            <li>OpenCV</li>
            <li>Flask</li>
            <li>NumPy</li>
            <li>YOLO weights and configuration files</li>
        </ul>
        <h3>Installation</h3>
        <ol>
            <li>Clone the repository:
                <pre><code>git clone &lt;repository-url&gt;</code></pre>
            </li>
            <li>Navigate to the project directory:
                <pre><code>cd &lt;project-directory&gt;</code></pre>
            </li>
            <li>Install the required packages:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li>Download YOLO weights and configuration files from the official <a href="https://pjreddie.com/darknet/yolo/">YOLO website</a> and place them in the project directory.</li>
        </ol>
    </div>

    <div class="section">
        <h2>Usage</h2>
        <ol>
            <li>Run the Flask application:
                <pre><code>python app.py</code></pre>
            </li>
            <li>Open your web browser and go to <code>http://127.0.0.1:5000</code>.</li>
            <li>Use the upload form to select a video file and submit it for processing.</li>
            <li>After processing, check the output text file for detected vehicle information.</li>
        </ol>
        <h3>Example Output</h3>
        <ul>
            <li>License Plate: ABC1234</li>
            <li>Vehicle Type: Car</li>
            <li>Vehicle Color: Red</li>
        </ul>
        <h3>کاربرد</h3>
        <ul>
            <li>پلاک: ABC1234</li>
            <li>نوع خودرو: خودرو</li>
            <li>رنگ خودرو: قرمز</li>
        </ul>
    </div>

    <div class="section">
        <h2>Libraries Used</h2>
        <ul>
            <li><strong>OpenCV</strong>: For computer vision tasks including image processing and object detection.</li>
            <li><strong>Flask</strong>: A lightweight web framework for creating web applications in Python.</li>
            <li><strong>NumPy</strong>: A library for numerical computations in Python.</li>
        </ul>
        <h3>کتابخانه‌های استفاده شده</h3>
        <ul>
            <li><strong>OpenCV</strong>: برای وظایف بینایی کامپیوتر شامل پردازش تصویر و شناسایی اشیاء.</li>
            <li><strong>Flask</strong>: یک فریم‌ورک وب سبک برای ایجاد برنامه‌های وب در پایتون.</li>
            <li><strong>NumPy</strong>: یک کتابخانه برای محاسبات عددی در پایتون.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Applications</h2>
        <ul>
            <li>Automated traffic monitoring systems.</li>
            <li>Parking management solutions.</li>
            <li>Security and surveillance applications.</li>
            <li>Smart city initiatives for vehicle tracking.</li>
        </ul>
        <h3>کاربردها</h3>
        <ul>
            <li>سیستم‌های نظارت بر ترافیک خودکار.</li>
            <li>راه‌حل‌های مدیریت پارکینگ.</li>
            <li>برنامه‌های امنیتی و نظارتی.</li>
            <li>ابتکارات شهر هوشمند برای ردیابی خودروها.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Conclusion</h2>
        <p>The Vehicle License Plate Recognition System is a powerful tool for monitoring and managing vehicles effectively. By leveraging deep learning techniques and computer vision, it provides a reliable way to analyze video footage and extract valuable information.</p>
        <p>سیستم شناسایی پلاک خودرو یک ابزار قدرتمند برای نظارت و مدیریت مؤثر خودروها است. با استفاده از تکنیک‌های یادگیری عمیق و بینایی کامپیوتر، این سیستم یک روش قابل اعتماد برای تحلیل ویدیوها و استخراج اطلاعات ارزشمند ارائه می‌دهد.</p>
    </div>

    <div class="section">
        <h2>License</h2>
        <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>
        <p>این پروژه تحت مجوز MIT مجوز داده شده است. برای اطلاعات بیشتر به فایل <a href="LICENSE">LICENSE</a> مراجعه کنید.</p>
    </div>
</div>

<footer>
    <p>&copy; 2024 Vehicle License Plate Recognition System. All rights reserved.</p>
</footer>

</body>
</html>
