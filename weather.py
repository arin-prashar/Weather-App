# importing required files
import tkinter as tk
import requests
from tkinter import messagebox
import ttkbootstrap as ttk
from PIL import Image, ImageTk

def get_weather(city):
    API_key="f2bc7946391b854f686dcede47d1d09c"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res=requests.get(url)
    if res.status_code==404:
        messagebox.showerror("Error","City not found")
        return None
    data=res.json()
    icon_id=data['weather'][0]['icon']
    temprature=data['main']['temp']-273.15
    description=data['weather'][0]['description']
    city=data['name']
    country=data['sys']['country']

    icon_url=f"http://openweathermap.org/img/w/{icon_id}.png"
    return (icon_url,temprature,description,city,country)

def search():
    city_name=city_entry.get()
    result=get_weather(city_name)
    if result is None:
        return
    icon_url,temprature,description,city,country=result
    location_label.configure(text=f"{city},{country}")

    image=Image.open(requests.get(icon_url,stream=True).raw)
    icon=ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image=icon

    # update the temperature and description labels
    temperature_label.configure(text=f"{temprature:.2f}°C")
    description_label.configure(text=description) 
    
root=ttk.Window(themename='morph')
root.title("Weather App")
root.geometry("400x400")

# entry widget
city_entry=ttk.Entry(root,width=20,font=('Quicksand',18))
city_entry.pack(pady=10)

# button widget
search_button=ttk.Button(root,text="Search",command=search,bootstyle="warning")
search_button.pack(pady=10)

# label widget -> to show city/country name
location_label=ttk.Label(root,font="Helvetica, 25")
location_label.pack(pady=10)

# label widget -> to show the weather icon
icon_label=ttk.Label(root)
icon_label.pack(pady=10)

# label widget -> to show temperature
temperature_label=ttk.Label(root,font="Helvetica, 20")
temperature_label.pack(pady=10)

# label widget -> to show weather description
description_label=ttk.Label(root,font="Helvetica, 15")
description_label.pack(pady=10)

root.mainloop()