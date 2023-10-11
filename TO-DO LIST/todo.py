import tkinter as tk
def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        pass
def clear_tasks():
    task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=40, selectbackground="yellow")
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()
clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
clear_button.pack()

root.mainloop()
