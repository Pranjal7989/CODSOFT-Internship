import tkinter as tk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.pack(pady=10)
        
        self.complete_button = tk.Button(master, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(side=tk.LEFT, padx=5)
        
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=5)
        
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        
    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.task_listbox.delete(task_index)
        
    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.task_listbox.delete(task_index)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
