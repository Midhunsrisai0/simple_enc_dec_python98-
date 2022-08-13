from tkinter import *


def encrypt(n , shift):
    new_str = ''
    for i in n:
        if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            x = ord(i) + shift
            if(x>122):
                x = 96 + (x%122)
                new_str += chr(x)
            else:
                new_str+=chr(x)

        elif(ord(i) >= ord('A') and ord(i) <= ord('Z')):
            x = ord(i) + shift
            if(x>90):
                x = 64 + (x%90)    #65 is ascii value of 'A'
                new_str += chr(x)
            else:
                new_str+=chr(x)
        else:
            new_str += i
    return new_str
###


def decrypt(n , shift):
    new_str = ''
    for i in n:
        if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            x = ord(i) - shift
            if( x < 97):
                 x = 122-(96-x)
                 new_str+=chr(x)
            else:
                new_str+=chr(x)
        elif(ord(i) >= ord('A') and ord(i) <= ord('Z')):
            x = ord(i) - shift
            if(x<65):
                x=90-(64-x)
                new_str+=chr(x)
            else:
                new_str+=chr(x)
        else:
            new_str += i
    return new_str


mw = Tk()
mw.geometry('400x400')


def click(n):
    message = text_input.get()
    key = int(key_input.get())
    if(n ==1):
        new_message = encrypt(message, key)
        out_input.delete(0, END)
        out_input.insert(0, new_message)
    else:
        new_message = decrypt(message, key)
        out_input.delete(0, END)
        out_input.insert(0, new_message)


input_label = Label(mw, text='Enter your text here: ', font=30)
text_input = Entry(mw, font=30)
key_label = Label(mw, text='Enter your key: ', font=30)
key_input = Entry(mw, font=30)
out_label = Label(mw, text='Required text is: ', font=30)
out_input = Entry(mw, font=30)
b1 = Button(mw, text='Encrypt', font='30', command=lambda : click(1))
b2 = Button(mw, text='Decrypt', font='30', command=lambda : click(2))

out_label.grid(row=2, column=1, padx=10, pady= 10)
out_input.grid(row=2, column=2, padx=10, pady= 10)
key_label.grid(row=1, column=1, pady=10)
key_input.grid(row=1, column=2, pady=10)
input_label.grid(row=0, column=1, pady=10)
text_input.grid(row=0, column=2, pady=10)

b1.grid(row=3, column=1, padx=10, pady=10)
b2.grid(row=3, column=2, padx=10, pady=10)

mw.mainloop()
