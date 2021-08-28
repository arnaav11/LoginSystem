def adminc(if_owner:bool = False):
    import getpass as gp
    import ast


    File = open('data.dat', 'r+')
    Command = 'o'
    filelist = File.readlines()
    fileline1 = filelist[0][0:len(filelist[0])-1]
    fileline2 = filelist[1][0:len(filelist[1])-1]
    fileline3 = filelist[2]
    filedict = ast.literal_eval(fileline1)
    filedict2 = ast.literal_eval(fileline2)
    filedict3 = ast.literal_eval(fileline3)


    # Making The whole process loop forever so you can do multiple processes
    while '1' != 'q':
        File = open('data.dat', 'r+')
        Command = 'o'
        

        # Looping the question if given the wrong input
        while Command != 'w' and Command != 'r' and Command !='q' and Command != 'rem':
            # w -> write | r -> read | rem -> remove | q -> quit
            # Taking the command fom user
            Command = input('\nwhat do you want to do? (w, r, rem, q): ').lower()

            
        if Command == 'w':
            Usrnm_add = input('\nEnter the username: ')
            Usrnm_pass = input('\nEnter the password: ')
            if_admin = input('Is the user an admin?(y/n): ').lower()

            while if_admin != 'y' and if_admin != 'n':
                if_admin = input('Is the user an admin?(y/n): ').lower()
            
            if Usrnm_add in filedict or Usrnm_add in filedict2:
                print(f'{Usrnm_add} already exists!')
            else:
                if if_admin == 'y' and if_owner == True:
                    filedict2[Usrnm_add] = Usrnm_pass
                    filelist[1] = f'{str(filedict2)}\n'
                                       
                    File.seek(0)
                    File.truncate()
                    File.writelines(filelist)
                    
                elif if_admin == 'y' and if_owner == True:
                    print('Only owners can add Admins.')
                    
                else:
                    filedict[Usrnm_add] = Usrnm_pass
                    filelist[0] = f'{str(filedict)}\n'
                                       
                    File.seek(0)
                    File.truncate()
                    File.writelines(filelist)

        
        elif Command == 'r':
            # Read the file but only write the usernames
            print('\nUsers:')
            x = 1
            for key in filedict.keys():
                print(f'\n{x}: {key}')
                x+=1

            x = 1
            print('\nAdmins:\n')
            for key in filedict2.keys():
                print(f'{x}: {key}')
                x+=1


        elif Command == 'rem':
            # Remove a certain Username along with its password
            
            Usrnm_rem = input('\nWho do you want to remove? ')
            if Usrnm_rem in filedict2 and if_owner == False:
                print('\nThis user is an admin. You need to be an owner to remove admins.')
            elif Usrnm_rem not in filedict and Usrnm_rem not in filedict2:
                print('\nThis username doesn\'t exist!')
            elif Usrnm_rem in filedict:
                del(filedict[Usrnm_rem])
            elif if_owner == True:
                del(filedict2[Usrnm_rem])
            
            File.seek(0)
            File.truncate()
            filelist = [str(filedict)+'\n', str(filedict2)+'\n', str(filedict3)]
            File.writelines(filelist)


        elif Command == 'q':
            File.close() 
            # Close the Program
            exit()
        
        # V.Imp -> Close the file
        File.close()
