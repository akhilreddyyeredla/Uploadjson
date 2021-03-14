# File Structure
**app/views.py ->** will have the routes 


**files_managment ->** All the core code which are in different files according to the features


**database_conn.py ->** Mongo connection class which returns the connection object


**run.py ->** Flask start point


**requriments.py ->** all the librarys which are used accross the project

# End Points


**JSON Upload [POST]**
End point -> localhost:5000/upload-json


payload -> upload as a file with a key name **"**json_file**"**

**Get Data [GET]**
End point -> http://127.0.0.1:5000/get-data?symbol=symbol_name


**Delete Image [POST]**
End point -> http://127.0.0.1:5000/update-data?symbol=symbol_name

Payload -> JSON data which exact key names as in collection



