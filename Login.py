import ast
from adminchk import adminc
import getpass as gp
import UserApps

# Input the Username and Password
usrnm = input('Enter your username: ')
passw = gp.getpass('Enter you password(no display): ')

# Opening the file
File = open('data.dat', 'r+')

# Creating a string for each line without the '\n' escape sequence
filelist = File.readlines()
fileline1 = filelist[0][0:len(filelist[0])-1]
fileline2 = filelist[1][0:len(filelist[1])-1]
fileline3 = filelist[2]

# Creating a Dictionary for each line(representin the level of the perso in the company) string
filedict = ast.literal_eval(fileline1)
filedict2 = ast.literal_eval(fileline2)
filedict3 = ast.literal_eval(fileline3)


# Checking if the person is a key in the admin dictionary and the password is its value to check
# if the person is an admin
if usrnm in filedict2 and passw == filedict2[usrnm]:
        print("\nYou are an admin. You'll have access to all commands.")
        
        # Running the 'adminc' function which I made as well WITHOUT specifying if_user
        # so it takes False as default
        adminc()

# Checking if the person is a key in the owner dictionary and the password is its value to check
# if the person is an owner
elif usrnm in filedict3 and passw == filedict3[usrnm]:
        print("\nYou are an owner. You'll have access to all commands.")

        # Running the 'adminc' function which I made as well with 'if_owner' set to True
        adminc(if_owner=True)

# Checking if the person is a key in the admin dictionary and the password is its value to check
# if the person is an user
elif  usrnm in filedict and passw == filedict[usrnm]:
        print('\nLogin Successful!\n')
        # Running the 'usrapps' function which i made
        UserApps.usrapps()
else:
    print('not allowed')

# Closing the file
File.close()
