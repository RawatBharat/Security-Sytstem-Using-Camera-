# Security-Sytstem-Using-Camera-
Description
This project implements a security system that utilizes a camera to monitor and record activity in a specific area. The system can detect motion, capture images or record videos, and raise alerts in case of suspicious events. It aims to provide an affordable and accessible solution for home or small business security.

Table of Contents
1. Features
2. Installation
3. Usage
4. Configuration
5.Contributing


1. Features
Motion detection: The system can detect motion in the camera's field of view.
Image capture: When motion is detected, images are captured and stored for further analysis.
Video recording: Optionally, the system can record short videos when significant motion is detected.
Alerts: Alerts are sent to a specified email or phone number when suspicious events occur.
Web interface: A user-friendly web interface allows users to monitor the camera feed and access recorded media.


2. Installation
To set up the Security System, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/RawatBharat/Security-Sytstem-Using-Camera-.git
Navigate to the project directory:

bash
Copy code
cd Security-Sytstem-Using-Camera-
Install the required dependencies:

Copy code
pip install -r requirements.txt


3. Usage
Configure the system settings (see Configuration).

Run the main application:

4. Configuration
Before running the system, configure the following settings in config.py:

4.1. Camera settings: Set the camera source (e.g., webcam, IP camera) and resolution.
4.2. Motion sensitivity: Adjust the motion detection sensitivity level.
4.3. Alert settings: Enter the email or phone number to receive alerts.
4.5. Storage: Specify the directory for storing images and videos.
Example configuration:

python
Copy code
# Camera settings
CAMERA_SOURCE = 0
CAMERA_RESOLUTION = (640, 480)

# Motion detection
MOTION_SENSITIVITY = 0.5

# Alert settings
ALERT_EMAIL = 'your_email@example.com'
ALERT_PHONE = 'your_phone_number'

# Storage
STORAGE_DIRECTORY = 'media'


5. Contributing
Contributions are welcome! If you find any issues or want to enhance the project, feel free to open a pull request or submit an issue.
