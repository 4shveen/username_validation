'''Username Validation
Prompt the user to enter a username. Write a Python program to check if the username meets the
following criteria:
- The username must be at least 5 characters long.
- The username must not contain any special characters or spaces.
If the username meets the criteria, print "Valid username.
" Otherwise, print "Invalid username.
"'''
from colorama import Fore,Style
# Take input from user - username
username = input("Enter username: ")

# Check length of username
length = len (username)

# Check for absence of special characters or spaces
special_characters_count = sum (not c.isalnum() for c in username )

# Validate or Invalidate accordingly
if length >= 5 and special_characters_count == 0 :
    print (Fore.GREEN+"Valid username")
else :
    print (Fore.RED+"Invalid username")