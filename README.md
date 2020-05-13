# Cheesecommerce
A simple Flask application with client-side rendering through vanilla JavaScript. 

## Installing packages
* Create a virtual environment then start (optional)
* install packages through pip, example for Linux -> $ pip3 install -r requirements.txt

## Running application
On working directory (Linux/MacOS)
```
$ export FLASK_APP=application.py
$ export FLASK_ENV=development (debug mode)
$ flask run
```
Windows
```
c:..> set FLASK_APP=application.py
c:..> set FLASK_ENV=development
c:..> flask run
```
## To access Customer page
Access http://127.0.0.1:5000/customer/

## To access Admin page
Access http://127.0.0.1:5000/admin/

## Future improvements
* Create a UnitTest to test API implementations
* Formatted JSON data in UI
