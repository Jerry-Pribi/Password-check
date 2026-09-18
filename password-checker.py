from tkinter import *
import customtkinter as ctk
import re


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    rgb = (r, g, b)
    return '#%02x%02x%02x' % rgb


def draw_dradient(canvas, width, height, color1, color2, vertical=True):
    """Draw a smooth gradient from color1 to color2 on the given canvas"""
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    
    steps = height if vertical else width
    
    for i in range(steps):
        ratio = i / steps
        r= int(r1 + (r2 - r1) * ratio)
        g= int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b2) * ratio)
        color = rgb_to_hex(r, g, b)

        if vertical:
            canvas.create_line(0, i, width, i, fill=color)
        else: 
            canvas.create_line(i, 0, i, height, fill=color)
result_text_id = None  

def Check():
    global password_input, canvas, result_text_id
    score = 0
    feedback = []
    password = password_input.get().strip()

    if password == "":
        feedback.append("Musíš zadat heslo!")
    else:
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Použij aspoň 8 znaků.")

        if len(password) >= 12:
            score += 1

        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Přidej malá písmena.")

        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Přidej velká písmena.")

        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("Přidej čísla.")

        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            feedback.append("Přidej speciální znaky.")

        if re.search(r'(.)\1{2,}', password):
            score -= 1
            feedback.append("Nepoužívej opakující se znaky (např. 'aaa').")

    levels = ["Velmi slabé", "Slabé", "Ucházející", "Dobré", "Silné", "Velmi silné", "Ultra silné helso"]
    level = levels[max(0, min(score, 6))]

    
    feedback_text = "\n".join(feedback) if feedback else "Skvělé heslo!"
    display_text = f"Síla hesla: {level}\n{feedback_text}"

   
    if result_text_id is None:
        result_text_id = canvas.create_text(
            250, 300,
            text=display_text,
            font=("Playwrite New Zealand Basic", 14, "bold"),
            fill="white",
            width=350  
        )
    else:
        canvas.itemconfig(result_text_id, text=display_text)
        

def main():
    global canvas
    global password_input
    root = Tk()
    width = 500
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - width / 2)
    center_y = int(screen_height / 2 - height / 2)
    root.resizable(False, False)
    root.title("Password Checker!")
    root.geometry(f"{width}x{height}+{center_x}+{center_y}")

    # Canva
    canvas = Canvas(root, width=width, height=height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    VINE_RED = "#560606"
    BLACK = "#00090C"
    
    # Light blue fade: sogt sky blue
    draw_dradient(canvas, width, height, BLACK, VINE_RED, vertical=True)

    # Main Label
    main_label = canvas.create_text(
        200, 40,
        text="Password Checker",
        font=("Playwrite New Zealand Basic", 20, "bold"),
        fill="white"
    )
    canvas.coords(main_label, 250, 50)
    
    password_label = canvas.create_text(
        220, 220,
        text="Entry your password", 
        font=("Playwrite New Zealand Basic", 17, "bold"),
        fill="white")
    canvas.coords(password_label, 250, 170)
    
    password_input = Entry(
        canvas, bg=BLACK, fg="white",
        bd=0, highlightthickness=0, font=("Playwrite New Zealand Basic", 14, "italic"),
        insertbackground=VINE_RED)
    canvas.create_window(250, 220, window=password_input, width=300,height=45)
    
    check_password = ctk.CTkButton(
        root, text="Check", width=80, 
        font=("Playwrite New Zealand Basic", 15, "bold"), 
        border_width=2, border_color=BLACK ,bg_color=VINE_RED, hover_color="#B00000",
        height=25, command=Check)
    check_password.place(x=210,y=400)
    
    root.mainloop()

if __name__ == "__main__":
    main()
