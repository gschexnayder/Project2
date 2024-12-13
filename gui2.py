from tkinter import *
from tkinter import ttk
from math2 import *

class Gui:
    def __init__(self, window):
        self.window = window

        # Frame for the dropdown menu
        self.frame_one = Frame(self.window)
        self.label_one = Label(self.frame_one, text='Select Class:', font=('Palatino', 12, 'bold'))
        self.class_var = StringVar()
        self.dropdown = ttk.Combobox(self.frame_one, textvariable=self.class_var, state="readonly", width=40)
        self.dropdown['values'] = ['', 'Intro to CSII', 'System Administration', 'Info Security Policy & Awareness',
                                   'Managing Database Environment', 'Math Foundations of CS']
        self.dropdown.current(0)  
        self.dropdown.bind("<<ComboboxSelected>>", self.my_class)

        self.label_one.pack(side='top', pady=5)
        self.dropdown.pack(side='top', pady=5, padx=20, fill='x')
        self.frame_one.pack(anchor='center', pady=10)

        # Frame for final exam weight
        self.frame_info = Frame(self.window)
        self.label_info = Label(self.frame_info, text='', font=('Palatino', 12, 'bold'))
        self.label_info.pack(pady=5)
        self.frame_info.pack()

        # Current grade input
        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first, text='Current Grade:', font=('Palatino', 12))
        self.entry_first = Entry(self.frame_first, width=40)
        self.label_first.pack(padx=20, side='left')
        self.entry_first.pack(padx=20, side='left')
        self.frame_first.pack(anchor='w', pady=10)

        # Desired grade input
        self.frame_second = Frame(self.window)
        self.label_second = Label(self.frame_second, text='Desired Grade:', font=('Palatino', 12))
        self.entry_second = Entry(self.frame_second, width=40)
        self.label_second.pack(padx=20, side='left')
        self.entry_second.pack(padx=20, side='left')
        self.frame_second.pack(anchor='w', pady=10)

        # Answer Label
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result, font=('Palatino', 12, 'bold'))
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        # Calculate Button
        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='Calculate', command=self.compute)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()

    def my_class(self, event=None):
        self.entry_first.delete(0, END)
        self.entry_second.delete(0, END)
        self.label_result.config(text='')
        selected_class = self.class_var.get()

        # Update final exam weight and labels based on the selected class
        class_info = {
            'Intro to CSII': 'The final project is worth 20%.',
            'System Administration': 'The final exam is worth 20%.',
            'Info Security Policy & Awareness': 'The final project is worth 30%.',
            'Managing Database Environment': 'The final exam is worth 25%.',
            'Math Foundations of CS': 'The final exam is worth 25%.'
        }

        if selected_class in class_info:
            self.label_info.config(text=class_info[selected_class])
            self.label_first.config(text='Current Grade:')
            self.label_second.config(text='Desired Grade:')
        else:
            self.label_info.config(text='')

    def compute(self):
        try:
            current_grade = float(self.entry_first.get())
            desired_grade = float(self.entry_second.get())
            selected_class = self.class_var.get()

            # Final weights for each class
            final_weights = {
                'Intro to CSII': 0.2,
                'System Administration': 0.2,
                'Info Security Policy & Awareness': 0.3,
                'Managing Database Environment': 0.25,
                'Math Foundations of CS': 0.25
            }

            if selected_class in final_weights:
                final_weight = final_weights[selected_class]
                required_final = final_grade_calc(current_grade, desired_grade, final_weight)
                self.label_result.config(text=f'You need {required_final:.2f}% on the final.', fg='blue')
            else:
                self.label_result.config(text='No class selected.', fg='red')

        except ValueError:
            self.label_result.config(text='Enter valid numeric values.', fg='red')


if __name__ == '__main__':
    root = Tk()
    root.title('Grade Calculator')
    root.geometry('500x400')
    Gui(root)
    root.mainloop()