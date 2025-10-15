from turtle import *
import pandas

t=Turtle()
screen=Screen()
image="blank_states_img.gif"
screen.addshape(image)
screen.title("U.S. States Game")
t.shape(image)


data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_state=[]

while len(guessed_state)<50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 States Correct",prompt="What's another states name?").title()

    if answer_state=="Exit":
        missed_states=[state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missed_states.append(state)
        new_data=pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t1=Turtle()
        t1.hideturtle()
        t1.penup()
        state_data=data[data.state==answer_state]
        t1.goto(state_data.x.item(),state_data.y.item())
        t1.write(answer_state)
