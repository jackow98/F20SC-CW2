# from Logic.Tasks import Tasks
import tkinter as tk
app = tk.Tk()

app.title('Data Analysis of a Document Tracker')

# Inputs
inputs = ["user_uuid", "doc_uuid", "file_name", "task_name"]
for input_box in inputs:
    tk.Label(app, text=input_box).grid()
    tk.Entry(app).grid()


# Buttons
tasks = ["2a", "2b", "3a", "3b", "4d", "5", "6"]
buttons = []
for task in tasks:
    print(task)
    buttons.append(tk.Button(app, text='Run task ' + task, width=25, command=app.destroy))
    buttons[tasks.index(task)].grid()


# app.bind("<Button-1>", Tasks.run_task_2a)

app.mainloop()
