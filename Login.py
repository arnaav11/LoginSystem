import ast
from adminchk import adminc
import getpass as gp
import UserApps

# Input the Username and Password
usrnm = input('Enter your username: ')
passw = gp.getpass('Enter you password(no display): ')

File = open('data.dat', 'r+')
filelist = File.readlines()
fileline1 = filelist[0][0:len(filelist[0])-1]
fileline2 = filelist[1][0:len(filelist[1])-1]
fileline3 = filelist[2]
filedict = ast.literal_eval(fileline1)
filedict2 = ast.literal_eval(fileline2)
filedict3 = ast.literal_eval(fileline3)


if usrnm in filedict2 and passw == filedict2[usrnm]:
        print("You are an admin. You'll have access to all commands.")
        adminc()
elif usrnm in filedict3 and passw == filedict3[usrnm]:
        print("You are an owner. You'll have access to all commands.")
        adminc(if_owner=True)
elif  usrnm in filedict and passw == filedict[usrnm]:
        print('Login Successful!\n')
        UserApps.usrapps()
else:
    print('not allowed')


File.close()
