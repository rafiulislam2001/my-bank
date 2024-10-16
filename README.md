#####Running a simple app on web#####

###Overview:###
The My Bank app is a simple web built using Flask and Wrekzueg. It allows users secretly login into bank’s web portal and allows to check balance, withdraw and deposit. This README file provide step-by-step guide on how to set up, run, and test the application, both locally and using Docker.


###Technologies used:###
Flask: A lightweight WSGI web application framework in python.
Wrekzueg: Manage the underlying technical details of the web framework.
HTML: For front-end user interface design.
Docker: For containerization the application. 


###Installatione:###
1. Clone the repository and enter into it:
  ```
	git clone https://github.com/yourusername/my-bank.git
	cd my-bank
  ```
3. Install Flask
  ```
	pip install flask
  ```
5. Create a requirements.txt file and add Flask==2.0.2 and Wrekzeug==2.0.2 into it.
6. Create Dockerfile to send instruction to build the app.
7. Create docker-compose.yml to version control.
8. Create templates: Create a templates and create index.html, login.html, deposit.html, withdraw.html inside templates.

	##Example structure###
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


###Running the app:###
#Without docker:#
1. Run the flask app:
  ```
	python bank.py
  ```
3. Access the app:
  ```
	curl http://localhost:5000
  ```

#Without docker#
1. Build the application:
   ```
	docker build -t 5000:5000 my-bank .
   ```
3. Run the application:
   ```
	docker run -d -p 5000:5000 my-bank
   ```
