import pandas
# -------------
import pyperclip
from random import choice,shuffle,randint#--------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import json
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    letter_list = [choice(letters)for char in range(randint(8,10))]
    symbol_list = [choice(symbols)for each_num in range(randint(2,4))]
    num_list = [choice(numbers)for each in range(randint(2,4))]
    password_list = letter_list + symbol_list+ num_list
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0,f"{password}")
window = Tk()
window.config(padx=50,pady = 50)
window.title("Password Manager")
canvas = Canvas(width=200,height=200,highlightthickness=0)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = logo)
canvas.grid(column = 1,row = 0)
web_label = Label(text = "Website:")
web_label.grid(column = 0 , row = 1)
email_label = Label(text = "Email/Username:")
email_label.grid(column = 0 , row = 2)
password_label = Label(text = "Password:")
password_label.grid(column = 0 , row = 3)
web_entry = Entry(width=32)
web_entry.grid(column = 1 , row = 1 )
web_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(column = 1 , row = 2 , columnspan = 2)
email_entry.insert(0,"bahar84a@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(column = 1 , row = 3)
generate_button = Button(text = "Generate Password",command=generate_password )
generate_button.grid(column = 2 , row = 3 )

#list = [web_entry,email_entry,password_entry]

def data_saver():
    w = web_entry.get()
    e =email_entry.get()
    p =  password_entry.get()
    new_data = {w:{"email": e,
                   "password": p
               }
    }
    if len(w)==0 or len(e) == 0 or len(p) == 0 :
        messagebox.showerror(title= "ERROR", message="You have left the box empty smart ass!")
    else:
      try:
        with open("data.on", "r") as file:
            data = json.load(file)

            #json.dump(new_data,file, indent=4)
      except FileNotFoundError:
          with open("data.on", "w") as file:
              json.dump(new_data,file,indent=4)
      else:
          data.update(new_data)
          with open("data.on", "w") as file:
            json.dump(data,file, indent=4)
      finally:
            web_entry.delete(0,END)
            password_entry.delete(0,END)
def searcher():
  w = web_entry.get()
  try:
    with open("data.on","r") as file:
        data = json.load(file)
        data[w]
  except FileNotFoundError:
    messagebox.showinfo(title = "error",message="there is still no file")
  except KeyError:
      messagebox.showinfo(title="error", message=f"sorry you have no such an information in {w} website")
  else:
    messagebox.showinfo(title = w,message= f"Email : {data[w]["email"]}\n Password : {data[w]["password"]}")

add_button = Button(text = "Add",width=44,command = data_saver)
add_button.grid(column = 1 , row = 4,columnspan = 2 )
search_button = Button(text = "search",width=15,command=searcher)
search_button.grid(column = 2 , row = 1 )
#Password Generator Project







window.mainloop()