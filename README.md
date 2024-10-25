<div style="font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; background-color: #f4f4f4; color: #333; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
    <h1 style="color: #4CAF50;">🚗 Vehicle License Plate Recognition System</h1>
    <div style="margin-bottom: 20px;">
        <h2 style="color: #4CAF50;">🔍 Introduction</h2>
        <p>This project is a <strong>Vehicle License Plate Recognition System</strong> built using Python, OpenCV, and Flask. The application allows users to upload a video file, which is then processed to detect vehicles, recognize their types, colors, and license plates. The results are saved in a text file, providing a clear overview of detected vehicles. This project aims to streamline the process of monitoring vehicle movements and enhance security in various environments such as parking lots and traffic surveillance systems.</p>
        <p>این پروژه یک <strong>سیستم شناسایی پلاک خودرو</strong> است که با استفاده از پایتون، OpenCV و Flask ساخته شده است. این برنامه به کاربران اجازه می‌دهد تا یک فایل ویدئویی را بارگذاری کنند، که سپس برای شناسایی خودروها، تشخیص نوع، رنگ و پلاک آن‌ها پردازش می‌شود. نتایج در یک فایل متنی ذخیره می‌شوند و نمای واضحی از خودروهای شناسایی شده ارائه می‌دهند. هدف این پروژه ساده‌سازی فرآیند نظارت بر حرکت خودروها و افزایش امنیت در محیط‌های مختلف مانند پارکینگ‌ها و سیستم‌های نظارت ترافیکی است.</p>
    </div>
    <div style="margin-bottom: 20px;">
        <h2 style="color: #4CAF50;">📋 Features</h2>
        <ul style="list-style-type: square; margin: 10px 0;">
            <li>Real-time vehicle detection and recognition 🚙</li>
            <li>License plate recognition capabilities 📑</li>
            <li>Color and type detection of vehicles 🎨</li>
            <li>Results saved in a text file for easy review 📂</li>
            <li>User-friendly interface for video upload 📤</li>
            <li>Support for various vehicle types, including cars, trucks, and motorcycles 🚛</li>
            <li>Ability to handle multiple video formats (MP4, AVI, etc.) 🎥</li>
            <li>Integration with databases for storing recognized license plates 📊</li>
            <li>Detailed logs of detected vehicles for auditing purposes 📝</li>
            <li>Customizable detection parameters for improved accuracy ⚙️</li>
        </ul>
    </div>
    <div style="margin-bottom: 20px;">
        <h2 style="color: #4CAF50;">⚙️ Installation</h2>
        <p>To run this project, ensure you have the following prerequisites:</p>
        <ul style="list-style-type: square; margin: 10px 0;">
            <li>Python 3.x installed on your machine. You can download it from the official <a href="https://www.python.org/downloads/" style="color: #4CAF50;">Python website</a>.</li>
            <li>OpenCV library 📦</li>
            <li>Flask framework 🌐</li>
            <li>Other dependencies mentioned in requirements.txt</li>
        </ul>
        <p>### Installation Steps:</p>
        <ol>
            <li>Clone the repository using the following command:</li>
            <pre style="background-color: #e8e8e8; padding: 10px; border-radius: 5px; overflow: auto;">git clone https://github.com/MetiNaj/pelak-project.git</pre>
            <li>Navigate to the project directory:</li>
            <pre style="background-color: #e8e8e8; padding: 10px; border-radius: 5px; overflow: auto;">cd repository</pre>
            <li>Create a virtual environment (optional but recommended) to manage dependencies:</li>
            <pre style="background-color: #e8e8e8; padding: 10px; border-radius: 5px; overflow: auto;">python -m venv venv</pre>
            <li>Activate the virtual environment:</li>
            <ul>
                <li>On Windows:</li>
                <pre style="background-color: #e8e8e8; padding: 10px; border-radius: 5px; overflow: auto;">venv\Scripts\activate</pre>
                <li>On macOS/Linux:</li>
                <pre style="background-color: #e8e8e8; padding: 10px; border-radius: 5px; overflow: auto;">source venv/bin/activate</pre>
            </ul>
            <li>Install the required libraries using:</li>
            <pre style="background-color: #e8e8e8; padding: 10px; border-radius: 5px; overflow: auto;">pip install -r requirements.txt</pre>
            <li>Ensure that you have a suitable IDE or code editor, such as Visual Studio Code, for efficient coding and debugging. Additionally, consider using virtual environments to manage your project's dependencies more effectively.</li>
        </ol>
    </div>
    <div style="margin-bottom: 20px;">
        <h2 style="color: #4CAF50;">📝 Usage</h2>
        <p>To use the system, follow these steps:</p>
        <ol>
            <li>Clone the repository: <code>git clone https://github.com/yourusername/repository.git</code></li>
            <li>Navigate to the project directory: <code>cd repository</code></li>
            <li>Run the Flask app: <code>python app.py</code></li>
            <li>Access the web interface at <strong>http://localhost:5000</strong> in your browser 🌐</li>
            <li>Upload a video file through the web interface. Ensure that the video contains clear views of vehicle license plates 🚗.</li>
            <li>Review the results in the generated text file after processing. This file will include all recognized plates, types, and colors of vehicles detected during the video processing.</li>
            <li>You can also adjust the settings in the configuration file for tailored results to meet your needs ⚙️.</li>
        </ol>
        <p>### Example of Output:</p>
        <pre style="background-color: #e8e8e8; padding: 10px; border-radius: 5px; overflow: auto;">Detected Vehicles:
1. License Plate: XYZ1234, Type: Car, Color: Red
2. License Plate: ABC5678, Type: Truck, Color: Blue
3. License Plate: LMN9101, Type: Motorcycle, Color: Black
        </pre>
    </div>
    <div style="margin-bottom: 20px;">
        <h2 style="color: #4CAF50;">📚 Libraries Used</h2>
        <ul style="list-style-type: square; margin: 10px 0;">
            <li><strong>OpenCV:</strong> For image processing and computer vision tasks, enabling the detection of vehicles and license plates.</li>
            <li><strong>Flask:</strong> For creating the web application that handles user interactions and video uploads.</li>
            <li><strong>Numpy:</strong> For numerical operations on arrays, essential for handling image data efficiently.</li>
            <li><strong>Pandas:</strong> For data manipulation and analysis, allowing us to organize and present results effectively.</li>
            <li><strong>Matplotlib:</strong> For visualizing results and debugging purposes, helping to provide graphical outputs during development 📊.</li>
        </ul>
    </div>
    <div style="margin-bottom: 20px;">
        <h2 style="color: #4CAF50;">🚀 Future Enhancements</h2>
        <p>In future versions of this project, we aim to implement the following features:</p>
        <ul style="list-style-type: square; margin: 10px 0;">
            <li>Integration with machine learning models for enhanced accuracy in license plate recognition 🧠.</li>
            <li>Real-time video feed processing using webcams or IP cameras 🎥.</li>
            <li>Support for multiple languages in the interface 🌍.</li>
            <li>Mobile app development for on-the-go access to the recognition system 📱.</li>
            <li>Advanced analytics dashboard for monitoring vehicle statistics over time 📈.</li>
        </ul>
    </div>
    <footer style="text-align: center; margin-top: 40px; font-size: 0.9em; color: #777;">
        <p>© 2024 Vehicle License Plate Recognition System. All rights reserved. 🎉</p>
        <p>For any inquiries or support, please reach out to <a href="mailto:mahdinajar1385@gmail.com" style="color: #4CAF50;">mahdinajar1385@gmail.com</a>.</p>
    </footer>
</div>
