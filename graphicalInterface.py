import tkinter as tk
import main


class GraphicalInterface:

    def __init__(self):
        app = tk.Tk()

        app.title('Data Analysis of a Document Tracker')

        # Inputs
        inputs = ["visitor_uuid", "doc_uuid", "task_name", "file_name"]
        self.labels = []
        self.text_boxes = []
        for input_box in inputs:
            label = tk.Label(app, text=input_box)
            self.labels.append(label)

            text_box = tk.Entry(app)
            self.text_boxes.append(text_box)

            label.grid()
            text_box.grid()

        # Render button to execute task
        self.button = tk.Button(
            app,
            text='Run task',
            width=25,
            command=lambda: self.run_task()
        )

        self.button.grid()

        # Display GUI
        app.mainloop()

    def run_task(self):
        visitor_uuid = self.text_boxes[0].get()
        doc_uuid = self.text_boxes[1].get()
        task_name = self.text_boxes[2].get()
        file_name = self.text_boxes[3].get()

        task_res = main.invoke_task(visitor_uuid, doc_uuid, task_name, file_name)
        if task_res is not None:
            tk.messagebox.showinfo(f"Result of task {task_name}", task_res)



if __name__ == '__main__':
    gui = GraphicalInterface()
