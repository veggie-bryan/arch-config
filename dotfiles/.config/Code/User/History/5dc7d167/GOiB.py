import tkinter as tk
import os, sys
from PIL import Image, ImageTk

def resource_path(name):
    if getattr(sys, 'frozen', False):
        # Running as EXE → load files next to EXE
        return os.path.join(os.path.dirname(sys.executable), name)
    else:
        # Running as script → load files next to .py
        return os.path.join(os.path.dirname(__file__), name)

TODO_FILE = "todo_list.txt"

def load_tasks():
    path = resource_path(TODO_FILE)
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    path = resource_path(TODO_FILE)
    with open(path, "w") as f:
        for task in tasks:
            f.write(task + "\n")

selected_task_index = None
y_positions = []

def redraw_tasks():
    canvas.delete("all")
    global y_positions
    y_positions = []

    y = 10
    for i, task in enumerate(tasks):
        y_positions.append((y - 5, y + 25))

        if selected_task_index == i:
            canvas.create_rectangle(0, y - 5, 300, y + 25,
                                    fill="#e2f0ff", outline="")

        canvas.create_text(10, y, anchor="nw", text=task,
                           fill="black", font=("Arial", 12))

        y += 25
        canvas.create_line(5, y, 295, y, fill="#cccccc")
        y += 10

    canvas.config(scrollregion=(0, 0, 300, y))
    if y > 250:
        scrollbar.pack(side=tk.RIGHT, fill="y")
    else:
        scrollbar.pack_forget()

def add_task():
    new_task = entry.get().strip()
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        entry.delete(0, tk.END)
        redraw_tasks()

def remove_task():
    global selected_task_index
    if selected_task_index is not None:
        tasks.pop(selected_task_index)
        selected_task_index = None
        save_tasks(tasks)
        redraw_tasks()

def on_canvas_click(event):
    global selected_task_index

    clicked_y = canvas.canvasy(event.y)
    for i, (y1, y2) in enumerate(y_positions):
        if y1 <= clicked_y <= y2:
            selected_task_index = i
            redraw_tasks()
            return

    selected_task_index = None
    redraw_tasks()

root = tk.Tk()
root.title("Daily Tasks")
root.geometry("350x400")

root.iconbitmap(resource_path("trumpet_frog.png"))

tasks = load_tasks()

frame = tk.Frame(root)
frame.pack(pady=10)

canvas = tk.Canvas(frame, width=300, height=250, bg="white",
                   highlightthickness=1, highlightbackground="#cccccc")
canvas.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

canvas.bind("<Button-1>", on_canvas_click)

redraw_tasks()

entry = tk.Entry(root, width=30)
entry.pack(pady=(0, 5))

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Selected Task", command=remove_task)
remove_button.pack(pady=(5, 5))

frog_path = resource_path("trumpet_frog.png")
if os.path.exists(frog_path):
    frog_raw = Image.open(frog_path)
    frog_raw = frog_raw.resize((100, 110), Image.Resampling.LANCZOS)
    frog_img = ImageTk.PhotoImage(frog_raw)
    frog_label = tk.Label(root, image=frog_img, borderwidth=0, highlightthickness=0)
    frog_label.image = frog_img
    frog_label.place(relx=0, rely=1.0, anchor="sw", x=0, y=2.5)

root.mainloop()
