# 7/22/2019
# First of many application challenges from the /r/learnpython subreddit of varying degrees of difficulty
# Link: https://docs.google.com/document/d/1TyqD2_oDtiQIh_Y55J5RfeA91JJECc97xYIKM112H9I/
# Created by Khalil Najjar

import random
import time
# from tkinter import Pack,Label,mainloop,Tk,Button,Entry,Frame,Widget,Grid,StringVar

responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", " Yes - definitely.",
            "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
            "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
            "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
            "My sources say no.", "Outlook not so good.", "Very doubtful."]

def check_question(name):
    if len(name.get()) > 1 and "?" in name.get():
        eight_ball()
    else:
        print("Questions always have question marks! \"?\"")

def eight_ball():
    another_question = "Y"
    answer_count = 0
    while another_question == "Y":
        question = input("\n\nWhat would you like to ask the Magic 8-Ball?\n")
        if len(question) > 1 and "?" in question:
            print("\n\n\nThinking...\n\n")
            time.sleep(1)
            selection = random.randint(1, len(responses))
            answer = responses[selection]
            print(answer + "\n\n")
            answer_count += 1
            another_question = input("Would you like to ask another question? (Y/N)\n")
            another_question = another_question.upper()
        else:
            print("\n\nWait a second...\n\n")
            time.sleep(1)
            print("\n\nQuestions always have question marks! \"?\"")
            eight_ball()

    print("\n\nYou asked a total of {} questions".format(str(answer_count)))

    if answer_count == 1:
        print("\n\nHope you got your answer.\n")
        exit()
    else:
        print("\n\nHope you got your answers.\n")
    

eight_ball()

# root = Tk()
# root.title("Magic 8-Ball by Khalil Najjar")
# root.geometry("500x300")

# canvas = tk.canvas(root, height=300, width=500)

# window_label = Label(root, text="Welcome to the Magic 8-Ball", width = 40, font = ("arial", 20, "bold"))
# window_label.pack()

# inquiry = Label(root, text="Enter your question:", width = 15, font = ("arial", 12))
# inquiry.place(x=20,y=90)

# name = StringVar()
# question_box = Entry(root, textvariable=name)
# question_box.place(x=180, y=94, width=200)

# ask = Button(root, text="Ask", command=name)
# ask.place(x=200, y=250)

# abort = Button(root,text="Quit", command=exit)
# abort.place(x=250, y=250)
# root.mainloop()