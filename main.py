import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x400")

counter = 0



def button_function():
    global counter
    counter += 1
    counter_txt = "Button Counter: "
    print(counter_txt + str(counter))


#Using defined button
button = ctk.CTkButton(master=app, text="Button :O", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

app.mainloop()