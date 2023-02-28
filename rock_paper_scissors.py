import random
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""


def choice_to_number(choice):
    rps = {'rock': 0, 'paper': 1, 'scissors': 2}
    return rps[choice]


def number_to_choice(number):
    rps = {0: 'rock', 1: 'paper', 2: 'scissors'}
    return rps[number]


def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def result(user_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_number(user_choice)
    comp = choice_to_number(comp_choice)
    if (user == comp):
        print("We tied.")
    elif ((user-comp) % 3 == 1):
        print("You win this time.")
        USER_SCORE += 1
    else:
        print("I win.")
        COMP_SCORE += 1
    text_area = tk.Text(master=window, height=9, width=30)
    text_area.grid(column=0, row=4)
    answer = 'Your choice: {uc} \nMy choice: {cc}\n Your score: {us}\n My score: {cs}'.format(
        uc=USER_CHOICE, cc=COMP_CHOICE, us=USER_SCORE, cs=COMP_SCORE)
    text_area.insert(tk.END, answer)


def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'rock'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'paper'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def scissors():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'scissors'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


rock_button = tk.Button(text='Rock', command=rock)
rock_button.grid(column=0, row=1)
paper_button = tk.Button(text='Paper', command=paper)
paper_button.grid(column=0, row=2)
scissors_button = tk.Button(
    text='Scissors', command=scissors)
scissors_button.grid(column=0, row=3)


window.mainloop()
