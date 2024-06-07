---

# Quiz Application

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Screenshots](#screenshots)

## Overview
The Quiz Application is a Python-based GUI application developed using the Tkinter library. This application allows administrators to register new users, monitor quiz scores, and provides a platform for users to take quizzes with a timer. The quiz questions are read from a file and the scores are recorded and displayed for analysis.

## Features
- **Admin Login**: Secure login for administrators to manage the quiz.
- **User Registration**: New users can be registered by the admin.
- **Password Management**: Users can change their passwords for security purposes.
- **Timed Quiz**: Users can take quizzes that are timed, ensuring a challenging experience.
- **Scoreboard**: View the scores of all users who have taken the quiz.
- **Question Management**: Questions are loaded from a text file and presented to the user.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/S-NELSON-001/python_GUI_Quiz.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd python_GUI_Quiz
    ```
3. **Install dependencies**:
    - Ensure you have Python installed (preferably Python 3).
    - Install Tkinter if not already installed. Tkinter is usually included with Python, but if not, you can install it via:
    ```bash
    sudo apt-get install python3-tk (or) pip install tk
    ```

## Usage
1. **Run the application**:
    ```bash
    python GUI.py
    ```
2. **Admin Login**:
    - Use the default admin credentials provided in the script (`username: abcd, password: python`).
    - Admin can register new users and view the scoreboard.
3. **User Login**:
    - Users can log in using their credentials.
    - Users can change their password if needed.
    - Users can start the quiz which will be timed and scored     (Hardcoded).

## Screenshots

---

Admin's Page

![firstpage](https://user-images.githubusercontent.com/107765597/225629094-3374b508-b4bf-4fab-aac8-61d24d92aaeb.PNG)


![admin_login](https://user-images.githubusercontent.com/107765597/225630439-3aab8c7c-1bdf-4bdb-a7ae-b00a6220e944.PNG)


![admin_home_page](https://user-images.githubusercontent.com/107765597/225630391-9e4a39ee-f2bc-480c-8f07-9a29825e62bf.PNG)


![New_registration](https://user-images.githubusercontent.com/107765597/225631416-a38c1043-a5cc-42ae-8341-bbcfc930b2bb.PNG)


![scoreboard](https://user-images.githubusercontent.com/107765597/225631457-947e2dd0-6106-49ed-a7a8-03429d14bb86.PNG)
The Details button show the passed student list

User's Page


![userlogin](https://user-images.githubusercontent.com/107765597/225631923-18dcf947-f23f-414a-b539-17ec99ba535e.PNG)



![instruction](https://user-images.githubusercontent.com/107765597/225632307-59289248-bf0e-4c13-becc-c1ef78581a61.PNG)



![question](https://user-images.githubusercontent.com/107765597/225632591-3d563f5b-b7ad-499d-8f01-cf5d59961057.PNG)
