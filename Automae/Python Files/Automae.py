# Import libraries to python script
from pathlib import Path
import re, sys
from tkinter import *
import tkinter as tk
import os, subprocess, time

# Create root folder for GUI
root = Tk()

# Create label widget for a "Welcome message"

Start = Label(root, text= "Welcome to Automae. Choose an option to continue")

# Determine Domain Name that system is connected to
domainDetermine = subprocess.Popen('systeminfo | findstr /B Domain', stdout=subprocess.PIPE, universal_newlines=True, shell=True)

(output, err) = domainDetermine.communicate()

domainDetermine_status = domainDetermine.wait()

domainFound = output.split()

os.system('cls')
#print('cleared cmd')
print('This is your Domain:',domainFound[1])

ouDetermine = subprocess.Popen(['powershell', '-Command', 'Get-ADOrganizationalUnit -Filter "*" | Format-Table Name'], stdout=subprocess.PIPE, universal_newlines=True, shell=True)



# Determing Organizational Units in the Domain



#ouResultorg = ouDetermine.stdout.decode("utf-8")
(output, err) = ouDetermine.communicate()
ouStatus = domainDetermine.wait()

ouFound = output

# Create file for Organizational unit config
def ouFile():
    
    if (os.path.exists("ouList.txt") == False):
        
        file = open("ouList.txt", "w")

        file.write(ouFound)

        file.close()

        print('"ouList" file populated')

    else:
        
        file = open("ouList.txt", "w")

        file.write(ouFound)

        file.close()

        print('"ouList" file updated')  

    return 

ouFile()
           

#ouResult = ouResultorg.split()
#print("List of Organizational Units:",ouFound)



#




#print(ouMatches, domainFound)




# Put Welcome label widget on screen
Start.pack()



# Install neccessary ADDS features through powershell

#def adFeatures():
   
    #Dir = Button(text= "Dir", command= dirCMD, padx=50)
    #Dir.pack()
    #os.system('Install-WindowsFeature AD-Domain-Services,RSAT-AD-Tools,RSAT-AD-AdminCenterRSAT-ADLDS,RSAT-ADDS-Tools')
    #os.system(exit)
    #return

# Make functions that lets user input name for user creation




def addUser():
    
    global domainTitle

    domainTitle.pack_forget()

    addUserLabel.pack()
    
    addInput.pack()

    addUserConfirm.pack()
    

    return


def addConfirm():
    global addInput
    addUserLabel.pack_forget()
    addInput.pack_forget()
    addUserConfirm.pack_forget()



    

    global ouList
    ouList = []

    ouFileOpen = open('ouList.txt', 'r')

    ouFileRead = ouFileOpen.readlines()

    for line in ouFileRead:

        ouList.append(line.strip())

# Delete unneccessary spaces and labels ("Name" and "----")

    if ouList[1] == 'Name':

        ouList.remove('Name')
        ouList.remove('----')
        ouList.remove(ouList[-1])
        
        
        
        print("OU List",ouList)
        

    global dc1
    dc1 = domainFound[1]
    dc1Sep = dc1.split('.')

    dc1SepNew = [i.replace("'", '') for i in dc1Sep]

    userName = addInput.get()

    print("UserName get:",userName)
    
    for i in ouList:
        if i == ouList[-1]:
            #print("Last Line")
            pass
        else:

            
            

            #dc1.append(domainFound[1])

            print("DC1 List:",dc1)

            print("This is addInput:",userName)

            
            print('DC1 Split',dc1SepNew)


            print("Packing Buttons")

            OU = str(i)

            ouName = str(OU)

            print('Organized Name:',ouName)
            
            OU = Button(root, text=i, command=lambda:os.system('dsadd user cn='+userName+',ou='+ouName+',dc='+dc1Sep[0]+',dc='+dc1Sep[1]))
        # print("This is the Command being run:",OU)

            #print("This is the Command being run:",OU)

            OU.pack()
        

        print("User add output:",output)
    


        


    return
    


# Add Function Labels

addUserLabel = Label(root, text= 'Type the username'+ "you'd like to create, and press"+'"Confirm" to continue')
addInput= Entry(root, width=40, borderwidth= 5)
addUserConfirm = Button(root, text= "Confirm", command=addConfirm)
addUserOU = Label(root, text= 'Pick the organizational Unit of the user')




def delUser():


    x = Entry(root, width=40, borderwidth= 5)
    #ouquery = os.system("dsadd user "cn=eli,ou=Headquarters,dc=asani,dc=local" -fn eli -ln hammond -upn eli@asani.local -pwd !!ChangePlease1234 -mustchpwd yes")
    delUserbutton = Button(root, text= "Enter username that you'd like to delete", command=delClick)
   
   
    x.pack()
    delUserbutton.pack()
   

    #x.pack_forget()
    #delUserbutton.pack_forget()
    return

def delClick():

    global delUser
    global x

    delClik = "Deleting user:" + x.get()
    delLabel = Label(root, text=delClik)
    delLabel.pack()

    os.system('dsrm CN')
    return

# Make Buttons for Domain Server Functions, Local Functions, and Extra Functions

def domainClick():
    # Define variables for each task that has longer commands

    #dsAdd = os.system('dsadd user "cn=eli,ou=Headquarters,dc=asani,dc=local" -fn eli -ln hammond -upn eli@asani.local -pwd BigBoiAce5097 -mustchpwd yes')
    Start.pack_forget()
    domainButton.pack_forget()
   
    global domainTitle

    domainTitle = Label(root, text= 'Click the "Domain Fuctions" button to choose an option')

    domainMenu = Menubutton(root, text ="Domain Functions")

    domainMenu.menu = Menu(domainMenu)

    domainMenu["menu"] = domainMenu.menu

    domainMenu.menu.add_command(label="Make current computer a Domain Server", command=lambda: print("Domaaaain!!"))
    domainMenu.menu.add_command(label="Add user to Domain", command= addUser)
    domainMenu.menu.add_command(label="Delete user in Domain", command= delUser)
    domainMenu.menu.add_command(label="List all users in Domain", command=lambda: print("Domaaaain!!"))
    domainMenu.menu.add_command(label="Change user permissions in Domain", command=lambda: print("Domaaaain!!"))
    domainMenu.menu.add_command(label="Add a computer or workstation to Domain", command=lambda: print("Domaaaain!!"))
    domainMenu.menu.add_command(label="Delete a computer or workstation to Domain", command=lambda: print("Domaaaain!!"))
    domainMenu.menu.add_command(label="List current computers in Domain", command=lambda: print("Domaaaain!!"))
   
    #domainMenu.menu.add_command(label="Add ADDS features", command= CMD)
   
    # Install-WindowsFeature AD-Domain-Services, RSAT-AD-Tools,RSAT-AD-AdminCenterRSAT-ADLDS

    domainTitle.pack()
    domainMenu.pack()
    

    return

# Make Buttons for Domain Server Functions, Local Functions, and Extra Functions  
domainButton = Button(text= "Domain Server Functions", command= domainClick, padx=50)

domainButton.pack()

# Put Buttons on the screen




# Make Grid variable for Buttons

# exampleGrid.grid = (row=0,column=0)
# exampleGrid2.grid = (row=0,column=0)





# End Automae
root.mainloop()