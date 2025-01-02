from tkinter import *

def save_Text():
    with open("Saved Text.txt", "w", encoding = "latin1") as file:
        text = txt_content.get("1.0", END)
        file.write(text)
        print("The text has been saved correctly")

root = Tk()
root.geometry("500x450+500+200")
root.title("User Input")
root.resizable(width=False, height=False)

lbl_Instruction = Label(root, text = "Please enter the text to be stored:", font=("bold", 10))
lbl_Instruction.pack()

txt_content = Text(root, width = 40, height = 4)
txt_content.pack()

btn_save = Button(root, text = "Save Text", command = lambda: save_Text())
btn_save.pack()

root.mainloop()