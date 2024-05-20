import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Text, Canvas, Listbox, Scrollbar

class ReminderApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Reminder App")

        # Main frame
        self.frame = Frame(master, bg="pink")
        self.frame.pack(padx=10, pady=10)

        # Canvas for drawing
        self.canvas = Canvas(self.frame, width=300, height=50, bg="pink")
        self.canvas.create_text(150, 25, text="Reminder App", font=("Arial", 20), fill="white")
        self.canvas.pack()

        # Label and entry for the reminder title
        self.title_label = Label(self.frame, text="Title:", bg="pink")
        self.title_label.pack(anchor='w')
        self.title_entry = Entry(self.frame, bg="pink")
        self.title_entry.pack(fill='x')

        # Label and text widget for the reminder description
        self.desc_label = Label(self.frame, text="Description:", bg="pink")
        self.desc_label.pack(anchor='w')
        self.desc_text = Text(self.frame, height=5, bg="pink")
        self.desc_text.pack(fill='x')

        # Button to add the reminder
        self.add_button = Button(self.frame, text="Add Reminder", command=self.add_reminder, bg="pink")
        self.add_button.pack(side='left', padx=5)

        # Button to delete selected reminder
        self.delete_selected_button = Button(self.frame, text="Delete Selected Reminder", command=self.delete_selected_reminder, bg="pink")
        self.delete_selected_button.pack(side='left', padx=5)

        # Listbox to display reminders
        self.reminder_list = Listbox(self.frame, height=10, width=50, bg="pink", selectmode='single')
        self.reminder_list.pack(pady=10)

        # Scrollbar for the listbox
        self.scrollbar = Scrollbar(self.frame, orient='vertical')
        self.scrollbar.config(command=self.reminder_list.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.reminder_list.config(yscrollcommand=self.scrollbar.set)

    def add_reminder(self):
        # Get title and description from the entry and text widget
        title = self.title_entry.get()
        description = self.desc_text.get("1.0", "end-1c")

        # If title or description is empty, do nothing
        if not title or not description:
            return

        # Add the reminder to the list
        self.reminder_list.insert('end', f"Title: {title}\nDescription: {description}\n")

        # Clear the entry and text widget
        self.title_entry.delete(0, 'end')
        self.desc_text.delete("1.0", "end")

    def delete_selected_reminder(self):
        # Get the index of the selected item
        index = self.reminder_list.curselection()
        if index:
            self.reminder_list.delete(index)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
