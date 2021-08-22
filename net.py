from datetime import date

# Read the current date
current_date = date.today()

# Print the formatted date
print (f"hoy es {current_date.day}/{current_date.month}/{current_date.year}")
print("Today is :%d-%d-%d" % (current_date.day,current_date.month,current_date.year))

# Set the custom date
custom_date = date(2020, 12, 16)
print("The date is:",custom_date)
from requests import get, exceptions
import string

# Import sys module
import sys

# Total number of arguments
print('Total arguments:', len(sys.argv))

print("Argument values are:")
# Iterate command-line arguments using for loop
for i in sys.argv:
  print(i)

def check_internet_connection():
    try:
        get('http://google.com', timeout = 3)
        print('connected')
    except exceptions.ConnectionError:
        print('not connected')

check_internet_connection()

# Use of String Formatting
float1 = 563.78453
print("{:5.2f}".format(float1))

# Use of String Interpolation
float2 = 563.78453
f3= str("%5.2f" % float2)
print("%5.2f" % float2)
print(f3)

#print(list(string.ascii_letters) + list(string.digits) + list(string.punctuation))


# Declare a fruit list
fruits = ["Mango","Orange","Guava","Banana"]

# Insert an item in the 2nd position
fruits.insert(1, "Grape")

# Displaying list after inserting
print("The fruit list after insert:")
print(fruits)
 
# Remove an item
fruits.remove("Guava")

# Print the list after delete
print("The fruit list after delete:")
print(fruits)

fruits.append("Aguacate")
fruits.append("Aguacate")
print("The fruit list after añadir aguacate:")
print(fruits)
fruits.remove("Aguacate")

fruits[4]="Aguacato"
print(fruits)
print(len(fruits))
fruta="Orange"
print(f" la {fruta} aparece {fruits.count(fruta)} veces ")
print(fruits.count("Orange"))

# Define a tuple of websites
websites = ("google.com","yahoo.com", "ask.com", "bing.com")
print(type(websites))

# Create a list from tuple using list comprehension
site_list = [ site for site in websites ]
print(site_list)
print(type(site_list))