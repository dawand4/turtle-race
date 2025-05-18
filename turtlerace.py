import turtle as turtlemod
import random
from turtle import Screen, Turtle

def pytanie():
	odpowiedz = screen.textinput(title="Pytanie", prompt="Zagrac jeszcze raz?")
	if odpowiedz == "tak":
		turtlemod.clearscreen()
		return race()
	else:
		screen.bye()
def race():
	zolwie = []
	random.shuffle(kolory)
	for i in range(5):
		zolw = Turtle()
		zolwie.append(zolw)
		zolwie[i].hideturtle()
		zolwie[i].shape('turtle')
		zolwie[i].speed(0)
		zolwie[i].color(colors[kolory[i]])
		zolwie[i].penup()
		zolwie[i].setpos(-450, pozycje[i])
		zolwie[i].showturtle()
	user_bet = screen.textinput(title="Obstawienie", prompt="Wprowadz kolor zolwia, ktory wygra:")
	while True:
				n = random.randrange(5)
				zolwie[n].forward(5)
				if zolwie[n].xcor() > 470:
					winner = zolwie[n].pencolor()
					zwyciezca = ""
					for i in range(len(colors)):
						if list(colors.values())[i] == winner:
							zwyciezca = list(colors.keys())[i]
					if colors[user_bet] == winner:
						turtlemod.write("Zwyciestwo. Wygrywa " + zwyciezca, align="center", font=('Arial', 32, 'normal'))
					else:
						turtlemod.write("Porazka. Wygrywa " + zwyciezca, align="center", font=('Arial', 32, 'normal'))
					break
	return pytanie()
kolory = ["czarny", "szary", "czerwony", "brazowy", "pomaranczowy", "zolty", "zielony", "niebieski", "fioletowy"]
colors = {"czarny":"black", "szary":"gray", "czerwony":"red", "brazowy":"saddlebrown", "pomaranczowy":"darkorange", "zolty":"yellow", "zielony":"lawngreen", "niebieski":"mediumblue", "fioletowy":"darkviolet"}
pozycje = [-300, -150, 0, 150, 300]

screen = Screen()
screen.setup(width=1000, height=800)
screen.title("Wyscig zolwi")

race()
