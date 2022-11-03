from tkinter import *
import tkinter as tk
import os, subprocess, time

# Create root folder for GUI
root = Tk()

# Create label widget

Start = Label(root, text= "Welcome to Automae. Choose an option to continue")

# Put label widget on screen
Start.pack()

# Install neccessary ADDS features through powershell

#def adFeatures():
    
    #Dir = Button(text= "Dir", command= dirCMD, padx=50)
    #Dir.pack()
    #os.system('Install-WindowsFeature AD-Domain-Services,RSAT-AD-Tools,RSAT-AD-AdminCenterRSAT-ADLDS,RSAT-ADDS-Tools')
    #os.system(exit)
    #return
# Make Buttons for Domain Server Functions, Local Functions, and Extra Functions

def domainClick():
    # Define variables for each task that has longer commands

    #dsAdd = os.system('dsadd user "cn=eli,ou=Headquarters,dc=asani,dc=local" -fn eli -ln hammond -upn eli@asani.local -pwd BigBoiAce5097 -mustchpwd yes')
    Start.pack_forget()
    domainButton.pack_forget()
    
    domainTitle = Label(root, text= 'Click the "Domain Fuctions" button to choose an option')

    domainMenu = Menubutton(root, text ="Domain Functions")

    domainMenu.menu = Menu(domainMenu)

    domainMenu["menu"] = domainMenu.menu

    domainMenu.menu.add_command(label="Make current computer a Domain Server", command=lambda: print("Domaaaain!!"))
    domainMenu.menu.add_command(label="Add user to Domain", command=lambda: os.system('dsadd user "cn=eli,ou=Headquarters,dc=asani,dc=local" -fn eli -ln hammond -upn eli@asani.local -pwd BigBoiAce5097 -mustchpwd yes'))
    domainMenu.menu.add_command(label="Delete user in Domain", command=lambda: print("Domaaaain!!"))
    domainMenu.menu.add_command(label="List all users in Domain", command=lambda: print("Domaaaain!!"))
    domainMenu.menu.add_command(label="Change user permissions in Domain", command=lambda: print("Domaaaain!!"))
    domainMenu.menu.add_command(label="Add a computer or workstation to Domain", command=lambda: print("Domaaaain!!"))
    domainMenu.menu.add_command(label="Delete a computer or workstation to Domain", command=lambda: print("Domaaaain!!"))
    domainMenu.menu.add_command(label="List current computers in Domain", command=lambda: print("Domaaaain!!"))
    
    #domainMenu.menu.add_command(label="Add ADDS features", command= CMD)
    
    # Install-WindowsFeature AD-Domain-Services, RSAT-AD-Tools,RSAT-AD-AdminCenterRSAT-ADLDS

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