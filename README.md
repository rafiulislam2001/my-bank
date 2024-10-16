# My Bank App

## Overview
The **My Bank** app is a simple web application built using Flask and Werkzeug. It allows users to securely log in to the bank's web portal, enabling them to check their balance, withdraw, and deposit funds. This README provides a step-by-step guide on how to set up, run, and test the application, both locally and using Docker.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework in Python.
- **Werkzeug**: Manages the underlying technical details of the web framework.
- **HTML/CSS**: For front-end user interface design.
- **Docker**: For containerizing the application.

## Installation
1. Clone the repository and navigate into it:
   ```bash
   git clone https://github.com/yourusername/my-bank.git
   cd my-bank
   ```
2. Install flask
   ```bash
      pip install flask
   ```
3. Create a requirements.txt file and add Flask==2.0.2 and Wrekzeug==2.0.2 into it.
4. Create Dockerfile to send instruction to build the app.
5. Create docker-compose.yml to version control.
6. Create templates: Create a templates and create index.html, login.html, deposit.html, withdraw.html inside templates.

### Example structure
```perl
	├── my-bank/
	│   ├── bank.py
	│   ├── templates/
	│   │   ├── index.html
	│   │   ├── login.html
	│   │   ├── deposit.html
	│   │   └── withdraw.html
	│   ├── requirements.txt
	│   ├── Dockerfile
	│   └── docker-compose.yml
```

## Running the app:
### Without docker:
1. Run the flask app:
  ```bash
	python bank.py
  ```
3. Access the app:
  ```bash
	curl http://localhost:5000
  ```

### Without docker:
1. Build the application:
   ```bash
	docker build -t 5000:5000 my-bank .
   ```
3. Run the application:
   ```bash
	docker run -d -p 5000:5000 my-bank
   ```






























