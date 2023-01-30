# University attendance and departure system QR Code using (python/django)
![Qr Code Home](https://github.com/omarreda22/Attendance-and-leaving-system-using-QR-Code/blob/main/static/qr_code_project.PNG)


## How it work(professor side)
before every lecture for every professor 
1. professor create QR code for attendance and departure 
2. the worker print this qr code and paste on for example lecture room door (also will display in site)

![Professor_side](https://github.com/omarreda22/Attendance-and-leaving-system-using-QR-Code/blob/main/static/professor_side%20(1).gif)



## How it work(student side)
1. student will scann QR Code by his phone 
2. qr code will take him to register form
3. student will submit by name and id
4. he will display in students table for this lecture

![student_side](https://github.com/omarreda22/Attendance-and-leaving-system-using-QR-Code/blob/main/static/student_sdie.gif)


## How to install on Windows
1. clone this project
2. install virtualenv
```
pip install virtualenv
```
3. create new virtual environment
```
py -m venv venv
```
4. activate the new virtual
```
.\venv\Scripts\activate
```
5. install requirements.txt
```
pip install -r requirements.txt
```
6. run local server to begin
 ```
 py manage.py runserver
 ```
 7. go live with [localhost:8000](http://localhost:8000/)
 
 ### To install on Unix/macOS  [see this document](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments)
 
 
 ## Access admin panel 
 1. run on trimnal 
 ```
 py manage.py createsuperuser
 ```
 2. create new admin user
 2. go to [localhost:8000/admin](http://localhost:8000/admin)



### Enjoy^^
 
