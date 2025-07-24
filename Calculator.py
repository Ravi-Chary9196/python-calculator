import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "del":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("600x400")

# Entry widget
entry = tk.Entry(root, font="Arial 50")
entry.pack(fill=tk.BOTH, ipadx=25, pady=25)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Create and place buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font="Arial 20")
        button.pack(side='left', expand=True, fill='both')
        button.bind("<Button-1>", click)

# Start the application
root.mainloop()
