import customtkinter as ctk

# To force light mode for pastel colours
ctk.set_appearance_mode("Light")

class ValentineApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Square window
        self.geometry("500x500")
        
        # Window title
        self.title("Important question...")
        
        # Setting background colour (front is back)
        self.configure(fg_color="#faacd4")
       
        # No resizing to cater for custom images
        self.resizable(False,False)

if __name__ == "__main__":
    app = ValentineApp()
    app.mainloop()