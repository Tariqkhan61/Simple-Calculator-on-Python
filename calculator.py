from tkinter import Tk, StringVar, Entry, Button, messagebox
import tkinter.font as tkFont

class Calculator:
    def __init__(self, master):
        # Window configuration
        master.title("Colorful Calculator")
        master.geometry("370x500+100+100")
        master.config(bg="#2c3e50")
        master.resizable(False, False)
        
        # Custom font
        self.entry_font = tkFont.Font(family='Helvetica', size=28, weight='bold')
        self.button_font = tkFont.Font(family='Helvetica', size=18, weight='bold')
        
        # Equation variable
        self.equation = StringVar()
        self.entry_value = ''
        
        # Entry widget
        Entry(width=14, bg='#ecf0f1', fg='#2c3e50', borderwidth=0, 
              font=self.entry_font, textvariable=self.equation, 
              justify='right').place(x=10, y=20, height=60, width=350)
        
        # Button colors
        num_color = '#3498db'
        op_color = '#e74c3c'
        eq_color = '#2ecc71'
        clr_color = '#f39c12'
        
        # Button layout
        buttons = [
            ('7', 10, 100, num_color), ('8', 100, 100, num_color), ('9', 190, 100, num_color), ('/', 280, 100, op_color),
            ('4', 10, 180, num_color), ('5', 100, 180, num_color), ('6', 190, 180, num_color), ('*', 280, 180, op_color),
            ('1', 10, 260, num_color), ('2', 100, 260, num_color), ('3', 190, 260, num_color), ('-', 280, 260, op_color),
            ('C', 10, 340, clr_color), ('0', 100, 340, num_color), ('=', 190, 340, eq_color), ('+', 280, 340, op_color),
            ('.', 10, 420, num_color), ('(', 100, 420, op_color), (')', 190, 420, op_color), ('⌫', 280, 420, clr_color)
        ]
        
        # Create buttons dynamically
        for (text, x, y, color) in buttons:
            if text == '=':
                Button(width=5, height=2, text=text, relief='flat', bg=color, fg='white',
                      font=self.button_font, command=self.solve).place(x=x, y=y)
            elif text == 'C':
                Button(width=5, height=2, text=text, relief='flat', bg=color, fg='white',
                      font=self.button_font, command=self.clear).place(x=x, y=y)
            elif text == '⌫':
                Button(width=5, height=2, text=text, relief='flat', bg=color, fg='white',
                      font=self.button_font, command=self.backspace).place(x=x, y=y)
            else:
                Button(width=5, height=2, text=text, relief='flat', bg=color, fg='white',
                      font=self.button_font, command=lambda t=text: self.show(t)).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set('')

    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = str(eval(self.entry_value))
            self.equation.set(result)
            self.entry_value = result
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            self.clear()
        except Exception:
            messagebox.showerror("Error", "Invalid calculation!")
            self.clear()

root = Tk()
calculator = Calculator(root)
root.mainloop()