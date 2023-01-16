from tkinter import messagebox
import webbrowser
import requests
from dotenv import load_dotenv
import os
from tkcalendar import *
from tkinter import *


load_dotenv()



def create_pixel():
    pixel_creation_endpoint = f"https://pixe.la/v1/users/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPHID')}"
    pixel_params = {
        "date":select_date(),
        "quantity": str(user_input.get())
    }
    

    response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
    messagebox.showinfo(message=response.text)

def delete_pixel():
    pixel_delete_endpoint = f"https://pixe.la/v1/users/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPHID')}/{select_date()}"
    response = requests.delete(url=pixel_delete_endpoint, headers=headers)
    messagebox.showinfo(message=response.text)

def update_pixel():
    pixel_update_endpoint = f"https://pixe.la/v1/users/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPHID')}/{select_date()}"
    update_params ={
        "quantity":user_input.get(),
    }
    
    response = requests.put(url=pixel_update_endpoint, json=update_params, headers=headers)
    messagebox.showinfo(message=response.text)
def open_graph():
    webbrowser.open(f"https://pixe.la/v1/users/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPHID')}.html",new=1)



window = Tk()
window.title("Reading Habit Tracker")
window.iconphoto(True, PhotoImage(file="D:/projetos/maiores/habit_traker/book_icon.png"))
window.config(pady=20,padx=20)
calendar = Calendar(window, selectmode="day",background="black")
calendar.grid(row=0,column=0,columnspan=4)

def select_date():
    calendar.config(date_pattern="yyyyMMdd")
    date = calendar.get_date()
    return date




pages_label = Label(text="Pages:")
pages_label.grid(row=1,column=0,columnspan=2,pady=10,sticky="e")
user_input = Entry(width=10)
user_input.grid(row=1, column=2,sticky="w")

headers = {
    "X-USER-TOKEN":os.getenv("PIXELA_TOKEN")
}


create_button = Button(text="ADD",command=create_pixel)
create_button.grid(row=2, column=0,pady=10)

update_button = Button(text="UPDATE",command=update_pixel)
update_button.grid(row=2, column=1,pady=10, sticky="w")

delete_button = Button(text="DELETE",command=delete_pixel)
delete_button.grid(row=2, column=2,pady=10,sticky="w")

show_graph = Button(text="Show Graph", command=open_graph)
show_graph.grid(row=2, column=3)



window.mainloop()