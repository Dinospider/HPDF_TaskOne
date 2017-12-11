# HPDF_AssignmentOne
HPDF - Task One

Project based on Python - Flask framework. Purpose of the project is to execute basic back-end functionalities.

__init__.py       : Main file containing routes to web application
Templates folder  : Contains all html files used for the webapp

To start, run 'Python __init__.py'(for Windows) from a flask environment.
The webapp will then run on the machine.

The web pages accessible are:
->http://localhost:5000/ : Hello World
->http://localhost:5000/authors : Responds with a list of authors and their posts
->http://localhost:5000/setcookie : Sets two cookies, name and age, given by user
->http://localhost:5000/getcookies : Gets the cookies
->http://localhost:5000/robots.txt : Denies access to user
->http://localhost:5000/html : Renders a HTML page
->http://localhost:5000/input : Receives input from user and logs it to console

Note: http://localhost:5000/ is just a sample, it may run on any other port