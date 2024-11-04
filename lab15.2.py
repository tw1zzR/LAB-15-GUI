import tkinter as tk

def save_data():
    width = root.winfo_width()
    height = root.winfo_height()
    background_color = root.cget("bg")

    data = {
        "Width": width,
        "Height": height,
        "Background Color": background_color
    }

    with open("settings.txt", "w", encoding="utf-8") as file:
        file.write(str(data))

    label_text.config(text="Success!")

root = tk.Tk()
root.title("Settings Data")
root.geometry("480x350")
root.config(bg="Black")

root.update_idletasks()

frame = tk.Frame(root, width=100, height=100, bg="white")
frame.place(x=190, y=10)

label_text = tk.Label(text=" ", fg="white", bg="black")
label_text.place(x=210, y=180)

button_save = tk.Button(root, text="SAVE", command=save_data, width=10)
button_save.place(x=195, y=130)


root.mainloop()