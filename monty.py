from tkinter import *
from random import *
from time import sleep

gift = choice(["1", "2", "3"])

window = Tk()
window.geometry("800x600+320+120")
window.resizable(0,0)

surface = Canvas(window, width = 800, height = 600)
surface.pack()

places = [[50,100, 250,500], [300,100, 500,500], [550,100, 750, 500]]

gift_img = PhotoImage(file = "Gift-Icon-PNG.png")
x = places[int(gift) - 1][0] + 100
y = places[int(gift) - 1][1] + 200

surface.create_image(x, y, image = gift_img)
door_1 = surface.create_rectangle(*places[0], fill = "brown") 
door_2 = surface.create_rectangle(*places[1], fill = "brown") 
door_3 = surface.create_rectangle(*places[2], fill = "brown")
doors = {"1" :door_1, "2" : door_2, "3" : door_3}

surface.create_rectangle(*places[0], width = 5)
surface.create_rectangle(*places[1], width = 5)
surface.create_rectangle(*places[2], width = 5)

push_counter = 0



def monti(event):
	global push_counter

	first = (50 < event.x < 250) and (100 < event.y < 500)
	second = (300 < event.x < 500) and (100 < event.y < 500)
	third = (550 < event.x < 750) and (100 < event.y < 500)


	if first:
		surface.itemconfig(door_1, fill = "orange")
		user_choice = "1"
		push_counter += 1
	if second:
		surface.itemconfig(door_2, fill = "orange")
		user_choice = "2"
		push_counter += 1
	if third:
		surface.itemconfig(door_3, fill = "orange")
		user_choice = "3"
		push_counter += 1

	sleep(1)

	if push_counter == 1:
		if user_choice == gift:
			show = choice(list({"1","2","3"} - {gift}))
			coords = surface.coords(doors[show])
			
			for i in range(20):
				coords[0] += 10
				surface.coords(doors[show], *coords)
				window.update()
				sleep(0.03)
		
		else:
			show = list({"1", "2", "3"} - {gift, user_choice})[0]
			coords = surface.coords(doors[show])
			for i in range(20):
				coords[0] += 10
				surface.coords(doors[show], *coords)
				window.update()
				sleep(0.03)
	elif push_counter == 2:
		coords = surface.coords(doors[user_choice])
		for i in range(20):
			coords[0] += 10
			surface.coords(doors[user_choice], *coords)
			window.update()
			sleep(0.03)

	



window.bind("<1>", monti)





#dz
#dobavit v programmu sposobnost pervui raz ili vtoroi, third































