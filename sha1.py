#!/usr/bin/python3

from tkinter import Tk     
from tkinter.filedialog import askopenfilename


from tkinter import *
import os # https://stackoverflow.com/questions/58475025/typeerror-an-integer-is-required-got-type-str-for-writing-to-file
import subprocess

import re



def main():

    
    def getDataToHash():
        ...       
        x = e_1.get()
        print(x)
        f = open("test.txt", "w")
        f.write(x)
        f.close()

        print("The test.txt reads...")
        f = open("test.txt", "r")       
        print(f.read())

        cmd = "openssl dgst -sha1 test.txt | cut -d ' ' -f 2 > sha1-hash.txt \n"
        f = open("openssl-command.sh", "w")
        f.write(cmd)
        f.close()
        print(os.system('chmod +x openssl-command.sh'))
        print(os.system('./openssl-command.sh'))
        print("The encoded test is...")
        f = open("sha1-hash.txt", "r")       

        z = f.read()
        e_2.delete(0, END)
        e_2.insert(0, z.rstrip('\r\n'))
       
        
    def getFileToHash():
        ...
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        fileNamePath = askopenfilename() # show an "Open" dialog box and return the path to the selected file

        print(fileNamePath) #get path

        #b = open("encodedBase64.txt", "r")       
        print("The file to be hashed " + fileNamePath ) # show the path
        #filePath = print(b.read())

       
        cmd = 'openssl sha1 ' + fileNamePath # Build the command
        b = open("openssl-file-hash-command.sh", "w")
        b.write(cmd)
        b.close()

        print(os.system('chmod +x openssl-file-hash-command.sh'))
        print(os.system('./openssl-file-hash-command.sh > the-file-hashed.txt'))
    
        b = open("the-file-hashed.txt", "r")
        #print("The hashed file." + b)       
        y = b.read()
        yy = re.findall("= (\w{,999}|\d{,999})",y)
        print(yy)
        
        e_4.delete(0, END)
        #e_4.insert(0, yy.rstrip('\r\n'))
        e_4.insert(0, yy)
        

    
    
    root = Tk()
    root.title(" Simple SHA Hashing Tool ")

    label_1 = Label(root, text="\n Hash a String \n")
    label_1.pack()
    
    e_1 = Entry(root, width=50)
    e_1.pack()
    
    hashButton = Button(root, text="Hash String", command=lambda:  getDataToHash()) ###################
    hashButton.pack()


    e_2 = Entry(root, width=50)
    e_2.pack()
    e_2.insert(0, "This SHA1 Hashes too...")


###################

    label_2 = Label(root, text="\n Hash A File \n")
    label_2.pack()

    #e_3 = Entry(root, width=50)
    #e_3.pack()
    #e_3.insert(0, " ") 

    hashFileButton = Button(root, text=" Select a File to Hash", command=lambda: getFileToHash())
    hashFileButton.pack()

    e_4 = Entry(root, width=50)
    e_4.insert(0, "The sha1 hash is ...")
    e_4.pack()
   

    label_3 = Label(root, text=" _________________ ")
    label_3.pack()
   


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
