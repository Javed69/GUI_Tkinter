'''print does not work in tkinter'''
from tkinter import *
from PIL import ImageTk,Image
#from tkinter import messagebox #to use message box we need to import it 
import sqlite3
import requests # needs to install
import json # inbuild in python



root = Tk()
root.title('Learn to code at codemy.com')

root.iconbitmap('image.png.ico')#for icon ico formate by window

root.geometry("600x100")

# create a zipcode look up function
def ziplookup():
	#zip.get()
	#iplabel = Label(root,text = zip.get())
	#ziplabel.grid(row  = 1,column = 0 ,columnspan =2)
	
	try:


		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=90A3EC28-B83A-4887-A1B1-446B95A4FBFC")

		api = json.loads(api_request.content)
		city = api[0]['ReportingArea'] 
		quality = api[0]['AQI']
		category = api[0]['Category']['Name']

		if category == "Good":
			weather_color = "#0C0"
		elif category == "Moderate":
			weather_color = "#FFFF00"
		elif category == "Unhealthy for Sensitive Groups":
			weather_color = "#ff9900"
		elif category == "Unhealthy":
			weather_color = "#FF0000"
		elif category == "Very Unhealthy":
			weather_color = "#990066"
		elif category == "Hazardous":
			weather_color = "#660000"

		root.configure(background = weather_color)

		myLabel = Label(root , text = city + " Air Quality " +  str(quality) + " " + category , font = ("Helvetica" , 20) , background = weather_color )
		myLabel.grid(row = 1 ,column = 0 ,columnspan = 2)

	except Exception as e:

		api = "Error..."


# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=90A3EC28-B83A-4887-A1B1-446B95A4FBFC


zip = Entry(root)
zip.grid(row = 0 ,column = 0 , sticky = W+E+N+S )

zipbutton = Button(root,text = "Lookup Zipcode" , command = ziplookup)
zipbutton.grid(row = 0 , column = 1)









root.mainloop()