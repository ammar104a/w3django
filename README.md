# w3django
Django Tutorial w3 schools
					Django Setup

1) Creating a virtual environment
py -m venv myworld
python -m venv myworld

2) Activating a virtual environment
myworld\Scripts\activate.bat
source myworld/bin/activate

3) Installing Django in a virtual environment
py -m pip install Django
python -m pip install Django

4) Checking Django Version
django-admin --version

5) Creating a Project  inside the venv
django-admin startproject my_tennis_club

6) Running a server
py manage.py runserver

7) Creating an app inside a project 
py manage.py startapp members

8) Views: are python funtions that takes requests and returns responses.
In this case, mytennis_club/members/views.py
e.g
from django.shortcuts import render
from django.http import HttpResponse

def members (requests):
	return HttpResponse("Hello World!")

9) URLS: 
a) Create a file called urls.py in my_tennis_club/members/urls.py
from django.urls import path
from . import views 

urlpatterns = [
	path('memers/', views.memers, name='members'),
]
b) Modify my_tennis_club/my_tennis_club/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('', include('members.urls')),
	path('admin/', admin.site.urls),
]

10) Displaying a webpage
my_tennis_club/members/templates/myfirst.html
<!DOCTYPE html>
<html>
<body>

<h1>Hello World!</h1>
<p>Welcome to my first Django project!</p>

</body>
</html>
my_tennis_club/members/views.py
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
my_tennis_club/my_tennis_club/settings.py
Add members to installed apps and dont forget to:
python manage.py migrate

11) Django Models
Creating a model = creating a table in the projects database
from django.db import models

class Member(models.Model):
	firstname = models.CharField(max_length = 255)
	lastname = models.CharField(max_length = 255)
# Use py manae.py makemigrations members to apply changes
# and then to create the table py manage.py migrate
# py manage.py sqlmigrate members 0001 to view sql statements that were executed
(myworld) C:\Users\sabai\myworld\my_tennis_club>python manage.py sqlmigrate members 0001
BEGIN;
--
-- Create model Member
--
CREATE TABLE "members_member" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "firstname" varchar(255) NOT NULL, "lastname" varchar(255) NOT NULL);
COMMIT;

12) Inserting Data
py manage.py shell
from members.models import Member
Member.objects.all()
member = Member(firstname='Emil', lastname='Refsnes')
member.save()
Member.objects.all().values()

13) Inserting Multiple Records
 member1 = Member(firstname='Tobias', lastname='Refsnes')
 member2 = Member(firstname='Linus', lastname='Refsnes')
 member3 = Member(firstname='Lene', lastname='Refsnes')
 member4 = Member(firstname='Stale', lastname='Refsnes')
 member5 = Member(firstname='Jane', lastname='Doe')
 members_list = [member1, member2, member3, member4, member5]
 for x in members_list:
   x.save()

14) Updating Data
from members.models import Member
x = Member.objects.al()[4]
x.first name Will give the first name of the meber on index 4 and id 5
x.firstname = "Ammar" will change the value of x and the first ame saved at index 4 id 5
Member.objects.all().values()

15) Delteting Data 
from members.models import Member
x = Member.objects.all()[5]
x.firstname will give the first name = 'Jane'
x.delete() will delete the whole member and not just the first name and will result in (1, {'members.Member': 1})

16) Adding More Fields to the Model
my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null = True)
  joined_date = models.DateField(null = True)

py manage.py makemigrations members
python manage.py migrate

17) Inserting data into the null fields
py manage.py shell
from members.models import Member
x = Member.objects.all()[0]
x.phone = 5551234
x.joined_date = '2022-01-05'
x.save()
Member.objects.all().values() to view the changes
or to view seperate fields, x.firstname, x.lastname, x.phone, x.joined_date

				  Django Display
1) Preparing a template
my_tennis_club/members/templates/all_members.html
<!DOCTYPE html>
<html>
<body>
<h1>Members</h1>

<ul>
	{% for x in mymembers %}
		<li> {{x.firstname}} {{x.lastname}} {{x.phone}} {{x.joined_date}}</li>
	{% endfor %}
</ul>

</body>
</html>
my_tennis_club/members/views.py:
from django.http import HttpRespose
from django.template import loader
from .models import Member

def members(request):
	mymembers = Member.objects.all().values()
	template = loader.get_template('all_members.html')
	context = {
		'mymembers': mymembers,
	}
	return HttpResponse(template.render(context, request))

Tag Reference
A list of all template tags:

Tag	Description
autoescape	Specifies if autoescape mode is on or off
block	Specifies a block section
comment	Specifies a comment section
csrf_token	Protects forms from Cross Site Request Forgeries
cycle	Specifies content to use in each cycle of a loop
debug	Specifies debugging information
extends	Specifies a parent template
filter	Filters content before returning it
firstof	Returns the first not empty variable
for	Specifies a for loop
if	Specifies a if statement
ifchanged	Used in for loops. Outputs a block only if a value has changed since the last iteration
include	Specifies included content/template
load	Loads template tags from another library
lorem	Outputs random text
now	Outputs the current date/time
regroup	Sorts an object by a group
resetcycle	Used in cycles. Resets the cycle
spaceless	Removes whitespace between HTML tags
templatetag	Outputs a specified template tag
url	Returns the absolute URL part of a URL
verbatim	Specifies contents that should not be rendered by the template engine
widthratio	Calculates a width value based on the ratio between a given value and a max value
with	Specifies a variable to use in the block
