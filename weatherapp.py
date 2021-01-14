# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:55:28 2021

@author: abhis
"""

import tkinter as tk
import requests
import time

def get_weather(canvas):
    city=textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=e0e5517fe786f93e2580e51f81491a04".format(city)
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp= int(json_data['main']['temp']-273)
    min_temp= int(json_data['main']['temp_min']-273)
    max_temp= int(json_data['main']['temp_max']-273)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind= json_data['wind']['speed']
    sunrise=time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise']-21600))
    sunset=time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset']-21600))
    final_info=condition+'\n'+ str(temp)+ 'C'
    final_data='\n'+'Max Temp:'+str(max_temp)+'\n'+ 'Min Temp:'+ '\n'+ str(min_temp) + '\n'+ 'Pressure:'+ str(pressure)+'\n'+ str(humidity) +'\n' + "Wind speed:" + str(wind) + '\n'+ 'Sunrise:'+ sunrise +'\n' + 'Sunset:'+ sunset
    label_1.config(text=final_info)
    label_2.config(text=final_data)
canvas = tk.Tk()
canvas.geometry('600x500')
canvas.title('Weather App')

f=('ppopins',15,'bold')
t=('poppins',35,'bold')

textfield= tk.Entry(canvas,font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',get_weather)
label_1=tk.Label(canvas,font=t)
label_1.pack()
label_2=tk.Label(canvas,font=f)
label_2.pack()
canvas.mainloop()
