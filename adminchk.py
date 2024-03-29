from logging import addLevelName


def adminc(if_owner: bool = False):

    """
    A function for admins and owners to administrate accounts present in data.dat
    
    Uses Caeser cipher for encryption
    """


    import Caesar_Cipher as CC

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


    # Making The whole process loop forever so you can do multiple processes
    while True:
        File = open('data.dat', 'r+')
        Command = 'o'
        

        # Looping the question if given the wrong input
        while Command != 'w' and Command != 'r' and Command !='q' and Command != 'rem':
            # w -> write | r -> read | rem -> remove | q -> quit
            # Taking the command fom user
            Command = input('\nwhat do you want to do? (w, r, rem, q): ').lower()

            
        if Command == 'w':
            # Inputting the username, the password, and whether the user will be an admin
            Usrnm_add = input('\nEnter the username: ')
            Usrnm_pass = input('\nEnter the password: ')
            if_admin = input('\nIs the user an admin?(y/n): ').lower()

            # Looping the question if the incompatible answer is given
            while if_admin != 'y' and if_admin != 'n':
                if_admin = input('Is the user an admin?(y/n): ').lower()
            
            # Checking if the Username is already in the users or admin dictionary
            if Usrnm_add in filedict or Usrnm_add in filedict2:
                print(f'{Usrnm_add} already exists!')

            # If not then start the process of writing the username to the dictionary
            else:

                # Checking if the username to add is an admin,
                # then the person adding the username should be owner
                if if_admin == 'y' and if_owner == True:
                    
                    # Creating a new key in the admins dictionary as the username entered,
                    # then add its value as its password
                    fildict2[CC.Caeser_Cipher(Usrnm_add)] = CC.Caeser_Cipher(Usrnm_pass)

                    # Updating the List of all users' 2nd item's(The admins' line) string
                    filelist[1] = (f'{str(fildict2)}\n')
                    filelist[0] = (f'{str(fildict)}\n')
                    filelist[2] = (str(fildict3))
                    
                    # Updating the file
                    File.seek(0)
                    File.truncate()
                    File.writelines(filelist)

                # If an admin wants to add an admin,
                # then deny and not write the username to the dictionaryy    
                elif if_admin == 'y' and if_owner == False:
                    print('\nOnly owners can add Admins.')
                
                # If the person only wants to add a user, then add it to the dictionary
                else:

                    # Creating a new key in the users dictionary as the username entered,
                    # then add its value as its password
                    fildict[CC.Caeser_Cipher(Usrnm_add)] = CC.Caeser_Cipher(Usrnm_pass)

                    # Updating the List of all users' 1st item's(The users' line) string
                    filelist[1] = (f'{str(fildict2)}\n')
                    filelist[0] = (f'{str(fildict)}\n')
                    filelist[2] = (str(fildict3))
                    
                    # Updating the file
                    File.seek(0)
                    File.truncate()
                    File.writelines(filelist)

        
        elif Command == 'r':
            print('\nUsers:\n')

            if len(filedict.keys()) > 0:
                x = 1
                # printing every key in the 1st dictionary(The users one) in a neat way
                for key in filedict.keys():
                    print(f'{x}. {key}')
                    x+=1

            else:
                print('No Users!\n')

            print('\nAdmins:\n')


            if len(filedict2.keys()) > 0:

                x = 1
                # printing every key in the 2nd dictionary(The admins one) in a neat way
                for key in filedict2.keys():
                    print(f'{x}. {key}')
                    x+=1

            else:
                print('\nNo Admins!\n')


        elif Command == 'rem':
            # Remove a certain Username along with its password
            
            # Inputting whom to remove
            Usrnm_rem = input('\nWho do you want to remove? ')

            # If the username is in the admins list and the person is not an owner, we deny the removal of the user
            if Usrnm_rem in filedict2 and if_owner == False:
                print('\nThis user is an admin. You need to be an owner to remove admins.')
            
            # Check if the username doesn't exist
            elif Usrnm_rem not in filedict and Usrnm_rem not in filedict2:
                print("\nThis username doesn't exist!")
            
            # Check if the person to remove is a user, so an admin can also remove him
            elif Usrnm_rem in filedict:
                del(filedict[Usrnm_rem])
            
            # Check if the person is an owner and the username to remove is an admin
            elif if_owner == True and Usrnm_rem in filedict2:
                del(fildict2[CC.Caeser_Ciphe(Usrnm_rem)])
            
            # Updating the list and the file
            File.seek(0)
            File.truncate()
            filelist[1] = (f'{str(fildict2)}\n')
            filelist[0] = (f'{str(fildict)}\n')
            filelist[2] = (str(fildict3))
            File.writelines(filelist)


        elif Command == 'q':
            File.close() 
            # Close the Program
            exit()
        
        # V.Imp -> Close the file
        File.close()


        for ii  in fildict.keys():
            filedict[CC.deCaeser_Cipher(ii)] = CC.deCaeser_Cipher(fildict[ii])
        for ii  in fildict2.keys():
            filedict2[CC.deCaeser_Cipher(ii)] = CC.deCaeser_Cipher(fildict2[ii])
        for ii  in fildict3.keys():
            filedict3[CC.deCaeser_Cipher(ii)] = CC.deCaeser_Cipher(fildict3[ii])
