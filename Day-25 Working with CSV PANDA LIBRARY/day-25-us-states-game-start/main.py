import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



df = pandas.read_csv('50_states.csv')

state_coordinates = {}

for index, row in df.iterrows():
    state_coordinates[row['state']] = (row['x'], row['y'])

is_on = True
while is_on:
    user_guess = screen.textinput(title="Enter your guess: ", prompt="Enter your guess: ")

    

    if user_guess in state_coordinates:
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()

        x, y = state_coordinates[user_guess]

        marker.goto(x, y)

        marker.write(user_guess, align="center", font=("Arial", 10, "normal"))

    elif user_guess == "exit":
        is_on = False

    else:
        screen.textinput(title="Guess the States: ", prompt="Enter your guess: ")



turtle.mainloop()
