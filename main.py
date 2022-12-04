import turtle
import random
import numpy

heads_label = 0
tails_label = 0
percentage_label = 0

# Creates a screen environment to work with
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Penny Flipping Probability")

# Registers shape of the penny
screen.register_shape("heads.gif")
screen.register_shape("tails.gif")

# Creates penny object
penny = turtle.Turtle()
penny.shape("heads.gif")

# Displays heads label
heads = turtle.Turtle()
heads.hideturtle()
heads.penup()
heads.color("white")
heads.goto(-250, 200)
heads.write(f"Heads: {heads_label}", align="center", font=("Courier New", 30, "normal"))

# Displays tails label
tails = turtle.Turtle()
tails.hideturtle()
tails.penup()
tails.color("white")
tails.goto(250, 200)
tails.write(f"Tails: {tails_label}", align="center", font=("Courier New", 30, "normal"))

#Displays percentage of heads and percentage of tails
percentage = turtle.Turtle()
percentage.penup()
percentage.hideturtle()
percentage.color("white")
percentage.goto(0, -300)
percentage.write(f"Standard Deviation=√(np(1-q): {0}\nZ-Score (X-μ)/σ: {0}", align="center",font=("Courier New", 30, "normal"))


# Click event
def clicked(x, y):
    side = random.choice(["heads", "tails"])
    penny.shape(f"{side}.gif")
    global tails_label
    global heads_label
    if side=="heads":
        heads_label+=1
        heads.clear()
        heads.write(f"Heads: {heads_label}\nPercentage: {round(heads_label/(sum([heads_label, tails_label])), 4)}", align="center", font=("Courier New", 30, "normal"))
    else:
        tails_label+=1
        tails.clear()
        tails.write(f"Tails: {tails_label}\nPercentage: {round(tails_label/(sum([heads_label, tails_label])),4)}", align="center", font=("Courier New", 30, "normal"))

    occurences = sum([tails_label, heads_label])
    percentage.clear()
    std_dev = round(numpy.sqrt(occurences* 0.5 * (1 - 0.5)), 4)  # Calculating a rolling standard deviation of heads and tails flips
    z_score = round((heads_label - (occurences / 2)) / std_dev,4) # Calculating a rolling z score to measure the deviations from the standard deviation
    percentage.write(f"Standard Deviation=√(np(1-q): {std_dev}\nZ-Score (X-μ)/σ: {z_score}",align="center", font=("Courier New", 30, "normal"))


penny.onclick(clicked)

turtle.done()
