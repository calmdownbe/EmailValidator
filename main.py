# Python email validator using Regular Expressions
import re

print"Email Validator"

email = raw_input("Input the email address to be validated: ")

if not re.match("^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
    print "Email is not valid."
else:
    print "Email is valid."


