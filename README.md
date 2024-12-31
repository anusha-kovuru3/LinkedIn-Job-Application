# LinkedIn Easy Apply Job Automation

This project automates the **Easy Apply** job process on LinkedIn using Selenium and a Tkinter-based graphical user interface (GUI). The application allows users to easily apply for jobs on LinkedIn by filling out a few required fields (email, password, phone number, job ID, and location) and automating the entire process.

## Features

- **Automated Login**: Login to LinkedIn using your credentials.
- **Easy Apply**: Automatically applies to jobs with the "Easy Apply" option using predefined input fields.
- **Job Search**: Search for jobs based on job ID and location.
- **Handling Additional Fields**: Detects and skips jobs that have additional fields to avoid errors during the application process.
- **Job Saving**: If a job application can't be completed, it automatically saves the job for later.
- **GUI**: A user-friendly GUI built with Tkinter for easy input of credentials and job details.

## Requirements

- Python 3.x
- **Selenium**: Used for automating the web browser.
- **Tkinter**: Python library for building the GUI.
- **Google Chrome** and **ChromeDriver**: Web browser and its driver for Selenium.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/linkedin-easy-apply-automation.git
    ```

2. Navigate to the project directory:
    ```bash
    cd linkedin-easy-apply-automation
    ```

3. Install the necessary libraries:
    ```bash
    pip install selenium
    ```

4. Download and install **Google Chrome** and **ChromeDriver** from:
    - [Google Chrome](https://www.google.com/chrome/)
    - [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads)

5. Ensure that `chromedriver.exe` is added to your system's PATH, or place it in the project directory.

## How to Use

1. **Launch the Application**:
   - Run the Python script to open the GUI:
     ```bash
     python main.py
     ```

2. **Input Your Details**:
   - **Email**: Your LinkedIn account email.
   - **Password**: Your LinkedIn account password.
   - **Phone**: A 10-digit phone number to be used in the application process.
   - **Job ID**: The keyword or job title you're looking for (e.g., "Software Engineer").
   - **Location**: The job location (e.g., "India").

3. **Start the Application**:
   - Click the "Start Application" button to begin the automation process. The script will handle logging in, searching for jobs, and applying using the details you provided.

4. **Monitoring**:
   - During the process, the script will automatically submit applications to jobs that have the "Easy Apply" option. It will also handle cases where additional information is requested by skipping those jobs and saving them for later.

5. **Complete**:
   - The process will print a message for each job application: whether it was successfully submitted or skipped. You can stop the process anytime by closing the GUI.

## How It Works

1. **Login to LinkedIn**: The script first opens LinkedIn's login page, enters the email and password, and logs in.
2. **Job Search**: Once logged in, it navigates to the job search page based on the provided job ID and location.
3. **Job Application**: The script clicks on each job listing and applies for jobs with the "Easy Apply" button. It automatically fills in your phone number and skips jobs with additional fields.
4. **Error Handling**: If a job has too many pages or additional fields, the script will abort the application and save the job for later.
5. **Cookies**: After logging in, cookies are saved and reused in future sessions to bypass login again.

