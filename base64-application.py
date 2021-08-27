from tkinter import *
import os # https://stackoverflow.com/questions/58475025/typeerror-an-integer-is-required-got-type-str-for-writing-to-file
import subprocess



def main():

    
    def getDataToEncode():
        ...       
        x = e_1.get()
        print(x)
        f = open("test.txt", "w")
        f.write(x)
        f.close()

        print("The test.txt reads...")
        f = open("test.txt", "r")       
        print(f.read())

        cmd = 'openssl base64 -in test.txt -out encodedBase64.txt'
        f = open("openssl-command.sh", "w")
        f.write(cmd)
        f.close()
        print(os.system('chmod +x openssl-command.sh'))
        print(os.system('./openssl-command.sh'))
        print("The encoded test is...")
        f = open("encodedBase64.txt", "r")       

        z = f.read()
        e_2.delete(0, END)
        e_2.insert(0, z.rstrip('\r\n'))
       
        
    def getDataToDecode():
        ...
        b = open("encodedBase64.txt", "r")       
        print("The encoded base64 to be decoded.")
        print(b.read())

       
        cmd = 'openssl base64 -d -in encodedBase64.txt -out decodedBase64.txt'
        b = open("openssl-command.sh", "w")
        b.write(cmd)
        b.close()

        print(os.system('chmod +x openssl-command.sh'))
        print(os.system('./openssl-command.sh'))
    
        b = open("decodedBase64.txt", "r")
        print("The decoded base64.")
           
        y = b.read()
        print(y)       
        e_4.delete(0, END)
        e_4.insert(0, y.rstrip('\r\n'))

    
    
    root = Tk()
    root.title("Simple Base64 Encoder & Decoder")

    label_1 = Label(root, text=" The Encode Section")
    label_1.pack()
    
    e_1 = Entry(root, width=50)
    e_1.pack()
    
    encodeButton = Button(root, text="Encode", command=lambda:  getDataToEncode()) ###################
    encodeButton.pack()

    e_2 = Entry(root, width=50)
    e_2.pack()
    e_2.insert(0, "This encodes to...")


###################

    label_2 = Label(root, text=" The Decode Section")
    label_2.pack()

    e_3 = Entry(root, width=50)
    e_3.pack()
    e_3.insert(0, " ") 

    decodeButton = Button(root, text="Decode", command=lambda: getDataToDecode())
    decodeButton.pack()

    e_4 = Entry(root, width=50)
    e_4.insert(0, "That decodes to...")
    e_4.pack()
   


    label_3 = Label(root, text=" ")
    label_3.pack()
   


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
