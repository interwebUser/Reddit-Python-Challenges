import random
import time
from tkinter import Pack,Label,mainloop,Tk,Button,Entry,Frame,Widget,Grid,StringVar

responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", " Yes - definitely.",
            "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
            "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
            "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
            "My sources say no.", "Outlook not so good.", "Very doubtful."]

def eight_ball():
    #input("\n\nWhat would you like to ask the Magic 8-Ball?\n")
    print("\n\n\nThinking...\n\n")
    time.sleep(1)
    selection = random.randint(1, len(responses))
    answer = responses[selection]
    print(answer + "\n\n")
    another_question = input("Would you like to ask another question? (Y/N)")
    another_question = another_question.upper()
    
    if another_question == "Y":
        eight_ball()
    else another_question == "N":
        print("\n\nHope you got your answer.\n")
        exit()

root = Tk()
root.title("Magic 8-Ball by Khalil Najjar")
root.geometry("500x300")

canvas = tk.canvas(root, height=300, width=500)

window_label = Label(root, text="Welcome to the Magic 8-Ball", width = 40, font = ("arial", 20, "bold"))
window_label.pack()

inquiry = Label(root, text="Enter your question:", width = 15, font = ("arial", 12))
inquiry.place(x=20,y=90)

name = StringVar()
question_box = Entry(root, textvariable=name)
question_box.place(x=180, y=94, width=200)

def check_question(name):
    if len(name.get()) > 1 and "?" in name.get():
        eight_ball()
    else:
        print("Questions always have question marks! \"?\"")

ask = Button(root, text="Ask", command=name)
ask.place(x=200, y=250)

abort = Button(root,text="Quit", command=exit)
abort.place(x=250, y=250)
root.mainloop()