# Validate a input user excercise
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits


username = input("Enter a username: ")



if len(username) > 12:
    print("Your user name cannot be more than 12 characters.")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not username.isalpha():
    print("Your username cannot contain number.")
else:
    print(f"Werlcome {username}")