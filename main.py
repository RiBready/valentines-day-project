import customtkinter as ctk

# -- Config! --
ctk.set_appearance_mode("Light") # To force light mode for pastel colours
BG_COLOUR = "#e0a7ff"
DIALOGUE_BOX ="#faacd4"
BORDER_COLOUR = "#a6e9ff"
TEXT_COLOUR = "#FF4C4F"
BTN_TEXT_COLOUR = "#FF9799"
BTN_COLOUR = "#FF69B4"
BTN_HOVER = "#FAFFB6"

class ValentineApp(ctk.CTk):
    
    def say_yes(self):
            print("She said yes!") # Dummy message for now
    
    def say_no(self):
         print("how did you get here.")

    def __init__(self):
        super().__init__()
        # Square window
        self.geometry("500x500")
        # Window title
        self.title("Important question...")
        # Setting background colour (front is back)
        self.configure(fg_color=BG_COLOUR)
       # No resizing to cater for custom images
        self.resizable(False,False)

        # Dialogue Box Frame
        self.game_frame = ctk.CTkFrame(
            self,fg_color=DIALOGUE_BOX, border_width=6, border_color=BORDER_COLOUR, corner_radius=0
            )
        # Dialogue Box frame layout manager (Pack)
        self.game_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.create_start_page()
    
    def clear_screen(self):
         # When called, it loops through each widget in the window and destroys it.
         for widget in self.winfo_children():
              widget.destroy()
            
    def create_start_page(self):
         # The big question
        self.label = ctk.CTkLabel(
            self.game_frame, text="Will you be my valentine?",
            font=("VCR OSD MONO", 28), text_color=TEXT_COLOUR
        )
        self.label.pack(pady=50)

        # Yes button
        self.yes_btn = ctk.CTkButton(
            self.game_frame, text="Yes!", command=self.say_yes,
            font=("VCR OSD MONO", 20), fg_color=BTN_COLOUR,
            hover_color=BTN_HOVER, text_color=BTN_TEXT_COLOUR,
            corner_radius=0, width=140, height=50
        )
        self.yes_btn.place(x=30, y=384)

        # No button
        self.no_btn = ctk.CTkButton(
            self.game_frame, text="No :((", command=self.say_no,
            font=("VCR OSD MONO", 20), fg_color=BTN_COLOUR,
            hover_color=BTN_HOVER, text_color=BTN_TEXT_COLOUR,
            corner_radius=0, width=140, height=50
        )
        self.no_btn.place(x=290, y=384)

    def create_yes_page(self):
         self.clear_screen()
         # TODO: make a success frame
         pass

    def create_no_page(self):
         self.clear_screen
         #TODO: make sad frame
         pass

        

if __name__ == "__main__":
    app = ValentineApp()
    app.mainloop()