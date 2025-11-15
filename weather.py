from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import requests
import pytz
from PIL import Image, ImageTk


root = Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)


# --- Search box entry ---
textfield = tk.Entry(
    root,
    justify='center',
    width=15,
    font=('poppins', 25, 'bold'),
    bg="#203243",
    border=0,
    fg="white"
)
textfield.place(x=370, y=130)
textfield.focus()


def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="WeatherApp_ArachanaSah")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        timezone.config(text=result)
        long_lat.config(text=f"{round(location.latitude,4)}°N, {round(location.longitude,4)}°E")

        # Current time
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)

        # Weather API
        api_key = "4f16bae899ea2a317c39d0d48a5c8a51"
        
        api = f"https://api.openweathermap.org/data/2.5/onecall?lat={location.latitude}&lon={location.longitude}&units=metric&exclude=hourly,minutely&appid=4f16bae899ea2a317c39d0d48a5c8a51"


        json_data = requests.get(api).json()
        print(json_data)

        

        # Current weather
        temp = json_data['current']['temp']
        humidity = json_data['current']['humidity']
        pressure = json_data['current']['pressure']
        wind = json_data['current']['wind_speed']
        description = json_data['current']['weather'][0]['description']


        # Update labels
        t.config(text=f"Temperature: {temp}°C")
        h.config(text=f"Humidity: {humidity}%")
        p.config(text=f"Pressure: {pressure} hPa")
        w.config(text=f"Wind Speed: {wind} m/s")
        d.config(text=f"Condition: {description.title()}")

        

        # --- Daily forecast cells ---
        daily = json_data['daily']

        # Helper for setting images & labels
        def set_day_data(day_index, img_label, temp_label):
            icon = daily[day_index]['weather'][0]['icon']
            img = Image.open(f"icon/{icon}@2x.png").resize((50, 50))
            photo = ImageTk.PhotoImage(img)
            img_label.config(image=photo)
            img_label.image = photo
            temp_day = daily[day_index]['temp']['day']
            temp_night = daily[day_index]['temp']['night']
            temp_label.config(text=f"{temp_day}°C\nNight: {temp_night}°C")

        set_day_data(0, firstimage, day1temp)
        set_day_data(1, secondimage, day2temp)
        set_day_data(2, thirdimage, day3temp)
        set_day_data(3, fourthimage, day4temp)
        set_day_data(4, fifthimage, day5temp)
        set_day_data(5, sixthimage, day6temp)
        set_day_data(6, seventhimage, day7temp)

        # Days
        first = datetime.now()
        for i, lbl in enumerate([day1, day2, day3, day4, day5, day6, day7]):
            next_day = first + timedelta(days=i)
            lbl.config(text=next_day.strftime("%A"))

    except Exception as e:
        messagebox.showerror("Weather App", f"Error: {e}")


# --- App Icon ---
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)

# --- Labels for weather info ---
labels = ["Temperature", "Humidity", "Pressure", "Wind speed", "Description"]
for i, text in enumerate(labels):
    Label(root, text=text, font=('Helvetica', 11), fg="white", bg="#203243").place(x=50, y=120 + i * 20)

# --- Search Box ---
Search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
Label(root, image=Search_image, bg="#57adff").place(x=270, y=120)

weat_image = PhotoImage(file="Images/Layer 7.png")
Label(root, image=weat_image, bg="#203243").place(x=290, y=127)

textfield = tk.Entry(
    root,
    justify='center',
    width=15,
    font=('poppins', 25, 'bold'),
    bg="#203243",
    border=0,
    fg="white"
)
textfield.place(x=370, y=130)
textfield.focus()

search_icon = PhotoImage(file="Images/Layer 6.png")
Button(root, image=search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather).place(x=645, y=125)

# --- Bottom Section ---
frame_bottom = Frame(root, width=900, height=180, bg="#212120")
frame_bottom.pack(side=BOTTOM)

# bottom boxes
firstbox = PhotoImage(file=r"Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file=r"Images/Rounded Rectangle 2 copy.png")

Label(frame_bottom, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame_bottom, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame_bottom, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame_bottom, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame_bottom, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame_bottom, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame_bottom, image=secondbox, bg="#212120").place(x=800, y=30)

frame_bottom.firstbox = firstbox
frame_bottom.secondbox = secondbox

# --- Clock & Timezone ---
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)

timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)

# --- Values for weather details ---
t = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=150, y=120)

h = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=150, y=140)

p = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=150, y=160)

w = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=150, y=180)

d = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=150, y=200)

# --- Forecast Frames ---
# First frame (larger)
firstframe = Frame(root, width=230, height=132, bg="#282829")
firstframe.place(x=35, y=315)
day1 = Label(firstframe, font="arial 20", bg="#282829", fg="#fff")
day1.place(x=100, y=5)
firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=1, y=15)
day1temp = Label(firstframe, bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=100, y=50)

# Other frames
frames = []
days = []
images = []
temps = []
x_positions = [305, 405, 505, 605, 705, 805]

for i, x in enumerate(x_positions):
    frame = Frame(root, width=70, height=115, bg="#282829")
    frame.place(x=x, y=325)
    frames.append(frame)

    lbl_day = Label(frame, bg="#282829", fg="#fff")
    lbl_day.place(x=10, y=5)
    days.append(lbl_day)

    lbl_img = Label(frame, bg="#282829")
    lbl_img.place(x=7, y=20)
    images.append(lbl_img)

    lbl_temp = Label(frame, bg="#282829", fg="#fff")
    lbl_temp.place(x=10, y=70)
    temps.append(lbl_temp)

# Assign variable names for compatibility
day2, day3, day4, day5, day6, day7 = days
secondimage, thirdimage, fourthimage, fifthimage, sixthimage, seventhimage = images
day2temp, day3temp, day4temp, day5temp, day6temp, day7temp = temps

root.mainloop()
