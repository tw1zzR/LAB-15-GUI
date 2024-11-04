import json; import tkinter as tk

def save_data():
    student_name = entry_name.get()
    absences = entry_absences.get()

    data = {
        "name": student_name,
        "absences": absences
    }

    with open("students_absences.json", "a") as file:
        json.dump(data, file)
        file.write("\n")

    label_text.config(text="Success!")

# Main Window
root = tk.Tk()
root.title("Students Absences")
root.geometry("480x350")
root.configure(bg="gray")

# Input Name
tk.Label(root, text="Ім'я студента:", fg="white", bg="gray").place(x=20, y=70)
entry_name = tk.Entry(root)
entry_name.place(x=170, y=70)

# Input Absences
tk.Label(root, text="Кількість пропусків:", fg="white", bg="gray").place(x=20, y=120)
entry_absences = tk.Entry(root)
entry_absences.place(x=170, y=120)

# Saving
button_save = tk.Button(root, text="Зберегти", command=save_data)
button_save.place(x=210, y=200)

# Output Message
label_text = tk.Label(text="", fg="white", bg="gray")
label_text.place(x=215, y=250)


root.mainloop()