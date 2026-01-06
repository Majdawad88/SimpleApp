# git clone https://github.com/Majdawad88/SimpleApp.git
class SimpleApp:
    def __init__(self, window):
        self.window = window  # Save the window in our pocket to use later
        self.window.title("Simple App")
        
        # Adding a button (Method call)
        # 'command=self.say_hi' tells the button which method to run when clicked
        self.btn = tk.Button(window, text="Click Me", command=self.say_hi)
        self.btn.pack()

    def say_hi(self):
        print("Hello User!")

root = tk.Tk()        # Create the actual window object
app = SimpleApp(root) # We pass 'root' into the 'window' parameter
root.mainloop()       # Keep the window open

