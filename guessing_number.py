from random import randint
from tkinter import *

number=randint(1,20) #generate random no between 1 to 20

#check whether the value is high , low or just right
def check():
    guess=int(guess_number.get())
        
    if guess > number:
        output="Your guess was too high"

    elif guess < number:
        output="Your guess was too low"

    else:
        output="Well Done your guess was correct"    


    result['text']=output   #to show the result


#create root window
root=Tk()

root.geometry("355x300")    #set width x height

root.resizable(0,0)         #don't allow to resize

root.title("Guessing Game") #set title

welcome_text=Label(text="Welcome to the game.\n You have to guess the no from 1 to 20 ",font=("comicsansns",13,"bold"))
welcome_text.pack(pady=20)

result=Label(text="Good Luck",fg="green",font=("comicsansns",13,"bold"))
result.pack()

guess_number=Entry()
guess_number.pack(pady=5)

check_ans=Button(text="Check",bg='black',fg="white",command=check)
check_ans.pack(pady=10)

root.mainloop()