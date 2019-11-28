import tkinter as tk
from Logic.Tasks import Tasks
import main


class GraphicalInterface:

    def __init__(self):
        app = tk.Tk()

        app.title('Data Analysis of a Document Tracker')

        # Inputs
        inputs = ["user_uuid", "doc_uuid", "task_name", "file_name"]
        self.labels = []
        self.text_boxes = []
        for input_box in inputs:
            label = tk.Label(app, text=input_box)
            self.labels.append(label)

            text_box = tk.Entry(app)
            self.text_boxes.append(text_box)

            label.grid()
            text_box.grid()

        # Buttons
        tasks = ["2a", "2b", "3a", "3b", "4d", "5", "6"]
        self.buttons = []
        for task in tasks:

            self.buttons.append(tk.Button(
                app,
                text='Run task ' + task,
                width=25,
                command=lambda: self.run_task(task)
            ))

            self.buttons[tasks.index(task)].grid()

        app.mainloop()

    def run_task(self, task_id: str):
        user_uuid = self.text_boxes[0].get()
        doc_uuid = self.text_boxes[1].get()
        task_name = self.text_boxes[2].get()
        file_name = self.text_boxes[3].get()
        main.invoke_task(user_uuid, doc_uuid, task_name, file_name)


if __name__ == '__main__':
    gui = GraphicalInterface()
