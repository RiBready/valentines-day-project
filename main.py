import customtkinter as ctk

# -- Config! --
# To force light mode for pastel colours
ctk.set_appearance_mode("Light")
BG_COLOUR = "#e0a7ff"
DIALOGUE_BOX ="#faacd4"
BORDER_COLOUR = "#a6e9ff"

class ValentineApp(ctk.CTk):
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
            self,fg_color=DIALOGUE_BOX, border_width=4, border_color=BORDER_COLOUR, corner_radius=0
            )
        # Dialogue Box frame layout manager (Pack)
        self.game_frame.pack(padx=20, pady=20, fill="both", expand=True)
        

if __name__ == "__main__":
    app = ValentineApp()
    app.mainloop()