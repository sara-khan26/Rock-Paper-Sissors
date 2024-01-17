import random

#function

def game (p1,p2):
    d= "Game Draw 😟"
    w= "YOU WIN!!! 🏆"
    l= "You Loose ☠️"
    if p1==p2 :
        return d
    elif p1== 'r' :
        if p2== 'p'  :
            return w
        elif p2== 's' :
            return l
        else:
            return 'you nigger its rock paper scissor 🐒 '
    elif p1== 'p' :
        if p2== 's' :
            return w
        elif p2== 'r' :
            return l
        else:
            return 'you nigger its rock paper scissor 🐒'
    elif p1== 's' :
        if p2== 'r' :
            return w
        elif p2== 'p' :
            return l
        else:
            return 'you nigger its rock paper scissor 🐒'

#main

your_choice=input("rock🪨 / paper📃 / scissor✂️ : ")
comp_choice= random.randint(1,3)
if comp_choice==1:
    comp_choice= 'r'
if comp_choice==2:
    comp_choice= 'p'
if comp_choice==3:
    comp_choice= 's'
print(f"computer chose: {comp_choice}")
result= game(comp_choice, your_choice)
print(result)
