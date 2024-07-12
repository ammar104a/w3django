from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member
import random
#views.py

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Member.objects.all().values()
    # The all method is used to get all the records and fields
    # for the Member model in this case
    # The values method allows us to return each object 
    # as a python dictionary, this the names and values as
    # key/value pairs
    # to return records where the first name is only "Tobias"
    # Member.objects.filter(firstname='Tobias').values()
    # The values_list() method allows you to retur only the columns
    # that you specify 
    # Members.objects.values_list('firstname') for colums
    # Members.obects.filter(firstname= 'Emil).values for specific rows
    mydata = Member.objects.all().values()
    template = loader.get_template('template.html')
    # Filter method usage
    mydata1 = Member.objects.filter(firstname= 'Emil').values()
    # inSQL this would be:
    # SELECT * FROM members WHERE firstname = 'Emil';
    # AND usage in the .filter() method 
    mydata2 = Member.objects.filter(lastname= 'Tobias', id=2).values
    # inSQL thi would be 
    # SELECT * FROM members WHERE lastname = 'Tobias' AND id = 2;
    # OR usage in the .filter() method
    mydata3 = Member.objects.filter(lastname = 'Emil').values() |  Member.objects.filter(id = 2 ).values()
    # or you can import Q
    # SELECT * FROM members WHERE firstname = 'Emil' OR firstname = 'Tobias';
    from django.db.models import Q
    mydata4 = Member.objects.filter(Q(lastname = 'Emil') | Q( id = 2 )).values()
    # FIELD LOOKUPS 
    #mydata5 = Member.objects.filter(firstname_startswith= 'L').values()
    # WHERE firstname LIKE 'L%'
    # mydata = Member.objects.filter(firstname__startswith='L').values()
    # ORDER BY 
    # the order_by() method is used to sort query sets 
    mydata6 = Member.objects.all().order_by('firstname').values()
    # inSQL this would be 
    # SELECT * FROM members ORDER BY firstname;
    # DECENDING ORDER use the - NOT sign 
    mydata7 = Member.objects.all().order_by('-firstname').values()
    #SELECT * FROM members ORDER BY firstname DESC;
    # Multiple orderbys are also possible 
    # The data will be ordered primarily y the last name 
    # if two last names are similar, then the id reverse ordering
    # will be used 
    # SELECT * FROM members ORDER BY lastname ASC, id DESC;
    mydata8 = Member.objects.all().order_by('lastname', '-id').values()

    '''
Keyword	        Description
contains	    Contains the phrase
icontains	    Same as contains, but case-insensitive
date	        Matches a date
day     	    Matches a date (day of month, 1-31) (for dates)
endswith	    Ends with
iendswith	    Same as endswidth, but case-insensitive
exact	        An exact match
iexact	        Same as exact, but case-insensitive
in	            Matches one of the values
isnull	        Matches NULL values
gt	            Greater than
gte	            Greater than, or equal to
hour	        Matches an hour (for datetimes)
lt	            Less than
lte	            Less than, or equal to
minute	        Matches a minute (for datetimes)
month	        Matches a month (for dates)
quarter	        Matches a quarter of the year (1-4) (for dates)
range	        Match between
regex	        Matches a regular expression
iregex	        Same as regex, but case-insensitive
second	        Matches a second (for datetimes)
startswith	    Starts with
istartswith	    Same as startswith, but case-insensitive
time	        Matches a time (for datetimes)
week	        Matches a week number (1-53) (for dates)
week_day	    Matches a day of week (1-7) 1 is sunday
iso_week_day	Matches a ISO 8601 day of week (1-7) 1 is monday
year	        Matches a year (for dates)
iso_year	    Matches an ISO 8601 year (for dates)
    '''


    
    weekdays = ('Monday', 'Tuesday', 
                 'Wednesday', 'Thursday',
                 'Friday', 'Saturday',
                 'Sunday')
    faroots = ("Apple", "Apricot", "Avocado", "Bannana", "Blackberry", "Blackcurrant", "Blueberry", "Boysenberry",
    "Cherry", "Clementine", "Coconut", "Cranberry", "Currant", "Date", "Dragonfruit", "Durian",
    "Elderberry", "Feijoa", "Fig", "Goji Berry", "Gooseberry", "Grape", "Grapefruit", "Guava",
    "Honeydew", "Huckleberry", "Jackfruit", "Jujube", "Kiwi", "Kumquat", "Lemon", "Lime",
    "Lychee", "Mango", "Mangosteen", "Mulberry", "Nectarine", "Orange", "Papaya", "Passionfruit",
    "Peach", "Pear", "Persimmon", "Pineapple", "Plum", "Pomegranate", "Pomelo", "Quince",
    "Raspberry", "Redcurrant", "Rhubarb", "Starfruit", "Strawberry", "Tamarind", "Tangerine",
    "Watermelon")
    cars = [
        {"brand": "Toyota", "model": "Corolla", "year": 2020},
        {"brand": "Honda", "model": "Civic", "year": 2019},
        {"brand": "Ford", "model": "Mustang", "year": 2021},
        {"brand": "Chevrolet", "model": "Camaro", "year": 2022},
        {"brand": "Tesla", "model": "Model S", "year": 2023},
    ]
    
    
    # context is a dictionary that will be passed to
    #the template
    context = {
        'mymembers' : mydata,
        'mymembers': mymembers,
        'greeting' : random.randint(0,6),
        'day' : random.choice(weekdays),
        'fruits' : faroots,
        'x': ('Apple', 'Banana', 'Cherry'),
        'y': ('Apple', "Banana', 'Cherry"),
        'cars' : cars,
        'emptytestobject': [],
    }
        

    
    return HttpResponse(template.render(context, request))