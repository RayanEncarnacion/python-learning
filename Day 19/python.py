from turtle import Turtle, Screen

player = Turtle()
screen = Screen()

def reset_initial_state():
    player.clear()
    player.penup()
    player.home()
    player.pendown()

TRACKED_ACTIONS = {
    "w": ("forward", 10),
    "s": ("backward", 10),
    "a": ("left", 10),
    "d": ("right", 10),
    "c": ('clear', None)
}

screen.listen()

for key, (action, distance) in TRACKED_ACTIONS.items():
    if action == "clear": screen.onkey(reset_initial_state, key)
    else: screen.onkey(lambda a=action, d=distance: getattr(player, a)(d), key)

screen.exitonclick()