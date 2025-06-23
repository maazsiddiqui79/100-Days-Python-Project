import turtle
import pandas as pd


# Set up screen
scr = turtle.Screen()
scr.title("India States Quiz")  # Updated title to match the map
scr.setup(width=750, height=600)

# Load and set the map image
map_image = "blank_states_img.gif"
scr.addshape(map_image)
turtle.shape(map_image)

data = pd.read_csv("50_states.csv")
all_states = [i.lower() for i in data["state"]]
    
print(all_states) #
guessed_state =0

while True:
    ans = scr.textinput(prompt="Enter a State Name:",title=f"Guessed State:{guessed_state/50}").lower() # type: ignore

    if ans.lower() in all_states:
        guessed_state += 1
        
        match_state = data[data["state"]== ans.title()]
        
        
        x_loc= match_state.x.item()
        y_loc= match_state.y.item()
        
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x=x_loc-10,y=y_loc-10)
        t.color("Black")
        t.write(arg=ans.title(),font=("Arial", 58, "normal"))
        t.clear()
        t.write(arg=ans.title(),font=("Arial", 48, "normal"))
        t.clear()
        t.write(arg=ans.title(),font=("Arial", 38, "normal"))
        t.clear()
        t.write(arg=ans.title(),font=("Arial", 28, "normal"))
        t.clear()
        t.write(arg=ans.title(),font=("Arial", 18, "normal"))
        t.clear()
        t.write(arg=ans.title(),font=("Arial", 8, "normal"))
    elif ans is None:
        break
        turtle.bye()   
        sys.exit()
        
    
        
        


    # scr.mainloop()
