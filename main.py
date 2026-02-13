import os
import customtkinter as ctk
from PIL import Image

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
            # print("She said yes!") # debug message
            self.create_yes_page()
    
    def say_no(self):
         print("how did you get here.")
         self.create_no_page()

    def try_again(self):
         self.clear_frame() # required or else the previous scene (no page) is shown
         self.create_start_page()
         

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
    
    def clear_frame(self):
         # When called, it loops through each widget in the window and destroys it.
         for widget in self.game_frame.winfo_children():
              widget.destroy()
            
    def create_start_page(self):
        self.clear_frame
        
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
            self.game_frame, text= "No :((", command = self.say_no,
            font = ("VCR OSD MONO", 20), fg_color = BTN_COLOUR,
            hover_color = BTN_HOVER, text_color = BTN_TEXT_COLOUR,
            corner_radius = 0, width = 140, height = 50
        )
        self.no_btn.place(x=290, y=384)

        # adding first image
        question_path = os.path.join(os.path.dirname(__file__), 'assets/question_cat.jpg')
        question_img = ctk.CTkImage(light_image = Image.open(question_path), size = (220, 220))
        question_label = ctk.CTkLabel(self.game_frame, text="", image = question_img)
        question_label.pack(pady=20)
        question_label.place(x=120, y = 120)

    def create_yes_page(self):
         self.clear_frame()
         
         # Yippee!
         self.label = ctk.CTkLabel(
            self.game_frame, text = "Yippee!",
            font = ("VCR OSD MONO", 28), text_color= TEXT_COLOUR
            )
         self.label.pack(pady = 50)

         happy_path = os.path.join(os.path.dirname(__file__), 'assets/happy_cat.jpg')
         happy_img = ctk.CTkImage(light_image = Image.open(happy_path), size = (220, 220))
         happy_label = ctk.CTkLabel(self.game_frame, text="", image = happy_img)
         happy_label.place(x = 120, y = 120)
    
         self.label = ctk.CTkLabel(
              self.game_frame, text= "Happy Valentine's Day <3\n I love you!",
              font=("VCR OSD MONO", 20), text_color=TEXT_COLOUR
         )
         self.label.place(x = 90, y = 370)
         pass

    def create_no_page(self):
         self.clear_frame()

         # but why :(
         self.label = ctk.CTkLabel(
              self.game_frame, text="But why :(", 
              font=("VCR OSD MONO", 20), text_color=TEXT_COLOUR
         )
         self.label.pack(pady = 50)

         sad_path = os.path.join(os.path.dirname(__file__), 'assets/sad_creature.jpg')
         sad_img = ctk.CTkImage(light_image = Image.open(sad_path), size = (220, 220))
         sad_label = ctk.CTkLabel(self.game_frame, text="", image = sad_img)
         sad_label.place(x = 120, y = 120)

         self.try_again_btn = ctk.CTkButton(
            self.game_frame, text= "Answer again? Please? :(", command = self.try_again,
            font = ("VCR OSD MONO", 20), fg_color = BTN_COLOUR,
            hover_color = BTN_HOVER, text_color = BTN_TEXT_COLOUR,
            corner_radius = 0, width = 260, height = 50
        )
         self.try_again_btn.place(x=85, y=381)

         pass

if __name__ == "__main__":
    app = ValentineApp()
    app.mainloop()