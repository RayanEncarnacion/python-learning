import random
from turtle import _Screen, Turtle, Screen
from typing import List, Tuple

WIDTH = 500
X_AXIS_END = WIDTH / 2 - 20
COLORS = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
X_AXIS_START = -X_AXIS_END
Y_AXIS_START = 80
TURTLE_SEPARATION = 30

def init_turtles(colors: List[str], 
                 x_axis_start: int | float, 
                 y_axis_start: int | float,
                 turtle_separation: int) -> List[Turtle]:
    turtles = []
    
    for idx, color in enumerate(colors, 1):
        runner = Turtle()
        runner.shape('turtle')
        runner.color(color)
        runner.penup()
        runner.goto(x_axis_start, y_axis_start - (idx * turtle_separation))
        turtles.append(runner)
    
    return turtles
        
def setup(width: int | float,
          colors: List[str], 
          x_axis_start: int | float, 
          y_axis_start: int | float,
          turtle_separation: int) -> Tuple[_Screen, List[Turtle]]:

    screen = Screen()
    screen.setup(width, width)
    screen.title("Turtle race")
    
    turtles = init_turtles(colors, x_axis_start, y_axis_start, turtle_separation)
    
    return screen, turtles

def play(screen: _Screen, 
         turtles: List[Turtle], 
         x_axis_end: int | float) -> None:
    
    running = True
    guess = screen.textinput(title='Make your bet', prompt='Who will win the reace? Enter a colour:')
    
    while running:
        for turtle in turtles:
            turtle.forward(random.randint(1, 10))
            
            if turtle.xcor() > x_axis_end:
                running = False
                winner_color = turtle.pencolor()
                
                if winner_color.lower() == guess.lower():
                    print(f"You've won! The {winner_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winner_color} turtle is the winner!")
                
    screen.exitonclick()
    
screen, turtles = setup(WIDTH, COLORS, X_AXIS_START, Y_AXIS_START, TURTLE_SEPARATION)
play(screen, turtles, X_AXIS_END)

    

    