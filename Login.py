from adminchk import adminc
import getpass as gp
import Caesar_Cipher as CC

# Input the Username and Password
usrnm = input('Enter your username: ')
passw = gp.getpass('Enter you password(no display): ')

# Opening the file
File = open('data.dat', 'r+')
lst = File.readlines()
filelist = [(lst[0][0:len(lst[0])-1]), (lst[1][0:len(lst[1])-1]), (lst[2][0:len(lst[2])])]
# Creating a string for each line without the '\n' escape sequence
fileline1 = (filelist[0])
fileline2 = (filelist[1])
fileline3 = (filelist[2])

# Creating a Dictionary for each line(representing the level of the person in the Data) string
fildict = eval(fileline1)
fildict2 = eval(fileline2)
fildict3 = eval(fileline3)

filedict = {}
filedict2 = {}
filedict3 = {}

for ii  in fildict.keys():
        filedict[CC.deCaeser_Cipher(ii)] = CC.deCaeser_Cipher(fildict[ii])
for ii  in fildict2.keys():
        filedict2[CC.deCaeser_Cipher(ii)] = CC.deCaeser_Cipher(fildict2[ii])
for ii  in fildict3.keys():
        filedict3[CC.deCaeser_Cipher(ii)] = CC.deCaeser_Cipher(fildict3[ii])


# Checking if the person is a key in the admin dictionary and the password is its value to check
# if the person is an admin
if usrnm in filedict2 and passw == filedict2[usrnm]:
        print("\nYou are an admin. You'll have access to all commands.")
        
        # Running the 'adminc' function which I made as well WITHOUT specifying if_owner
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
else:
    print('not allowed')

# Closing the file
File.close()
