Doctor-Appointment-Booking-System using AI - Version == 1.0.0 [Made by Biswadeb Mukherjee]
│
├── .git/                 # Git repository directory (created when you initialize a repository)
├── .gitignore            # Git ignore file to specify which files and directories to exclude from version control
|
├── app.py                # Your Flask application
│
├── recommendation/   # Appointment Recommendation System
│        ├── data/        # Data for recommendation (real-world or synthetic)
│        ├── doctor.py    # Algorithm for taking decisions and recommending appointments
├── all.py            # For importing all libraries
├── config.py         # Database Configuration settings
├── secret.py         # Secret key generator needed for the Flask web app
├── requirements.txt  # List of Python dependencies
│
├── static/               # Static files (CSS, JavaScript, images)
│   ├── assets/           # Contain all CSS files, pictures needed for the default page
│   ├── admin.css         # CSS styles for the admin dashboard
│   ├── admin.js
│
├── templates/            # HTML templates
│   ├── home.html         # Default Page
│   ├── login.html        # Patient's login Template
│   ├── register.html     # Patient's register Template
│   ├── patient.html      # Patient's dashboard Template
│   ├── booking.html      # Appointment booking Template
│   ├── recommend.html    # Recommendation result Template (if needed)
│   ├── token.html        # For generating Patient's token
│
│
├── trainer.py            # For training the model
│
├── docs/                 # Documentation
│   ├── README.md         # Project documentation
│
├── version.txt           # File containing the project version 
│
├── README.md             # Project summary and setup instructions
