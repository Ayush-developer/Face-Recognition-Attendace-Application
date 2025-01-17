# Face Recognition Attendance Application

![Face Recognition Attendance](assets/logo.png) <!-- Add a logo image in the assets folder -->

## Overview

The Face Recognition Attendance Application is designed to automate the attendance process using facial recognition technology. This application leverages OpenCV and deep learning convolutional neural networks (CNN) to recognize employee faces from CCTV footage and integrate the attendance records with a MySQL database.

## Features

- **Real-time Face Detection**: Utilizes OpenCV to extract faces from CCTV video footage.
- **Deep Learning Recognition**: Employs CNN models for accurate facial recognition.
- **Attendance Management**: Records employee attendance in a MySQL database.
- **User-Friendly Interface**: Easy to use interface for managing attendance records.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - OpenCV
  - NumPy
  - TensorFlow/Keras (for deep learning)
- **Database**: MySQL
- **Development Environment**: Jupyter Notebook or any Python IDE

## Installation

### Prerequisites

- Python 3.x
- MySQL Server
- Required Python Libraries

### Steps to Install

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Ayush-developer/Face-Recognition-Attendace-Application.git
   cd Face-Recognition-Attendace-Application
   ```

2. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MySQL Database**
   - Create a new database in MySQL.
   - Import the provided SQL script to set up the required tables.

4. **Configure Database Connection**
   - Update the database connection settings in the application code.

## Usage

1. **Run the Application**
   ```bash
   python main.py
   ```

2. **Capture Faces**
   - Use the application to capture employee faces and add them to the database.

3. **Start Attendance Tracking**
   - The application will continuously monitor the CCTV feed and log attendance.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV documentation
- TensorFlow/Keras documentation
- Inspiration from various open-source projects

## Contact

For any inquiries, please contact [Your Name](mailto:your.email@example.com).
