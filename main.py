import tkinter as tk
from tkinter import messagebox

CONVERSION_RATES = {
    ('Miles', 'Kilometers'): 1.60934,
    ('Kilometers', 'Miles'): 0.621371,
    ('Pounds', 'Kilograms'): 0.453592,
    ('Kilograms', 'Pounds'): 2.20462,
    ('Inches', 'Centimeters'): 2.54,
    ('Centimeters', 'Inches'): 0.393701,
}

UNITS = [u[0] for u in CONVERSION_RATES.keys()]

if __name__=='__main__':
    root = tk.Tk()
    root.title('Unit Converter')

    left_padding = (10, 0)
    top_padding = (5, 0)
    right_padding = (0, 10)
    bottom_padding = (0, 10)
    outer_top_padding = (10, 0)

    # Value components
    input_label = tk.Label(root, text='Value:')
    input_label.grid(row=1, column=1, padx=left_padding, pady=outer_top_padding)

    input_entry = tk.Entry(root)
    input_entry.grid(row=1, column=2, padx=right_padding, pady=outer_top_padding)

    # From components
    from_label = tk.Label(root, text='From:')
    from_label.grid(row=2, column=1, padx=left_padding, pady=top_padding)
    
    from_clicked = tk.StringVar()
    from_clicked.set(UNITS[0])

    from_drop = tk.OptionMenu(root, from_clicked, *UNITS)
    from_drop.grid(row=2, column=2, sticky='nesw', padx=right_padding, pady=top_padding)

    # To components
    to_label = tk.Label(root, text='to:')
    to_label.grid(row=3, column=1, padx=left_padding, pady=top_padding)
    
    to_clicked = tk.StringVar()
    to_clicked.set(UNITS[1])

    to_drop = tk.OptionMenu(root, to_clicked, *UNITS)
    to_drop.grid(row=3, column=2, sticky='nesw', padx=right_padding, pady=top_padding)


    answer_label = tk.Label(root)
    x = 0
    def convert_units():
        value = 0

        try:
            value = float(input_entry.get())
        except ValueError:
            messagebox.showerror(title='Error Value', icon=messagebox.ERROR, message=f'Enter valid number')
            return

        from_value = from_clicked.get()
        to_value = to_clicked.get()

        if (from_value, to_value) not in CONVERSION_RATES.keys():
            messagebox.showerror(title='Error Conversion Units', icon=messagebox.ERROR, message=f'Can not convert {from_value} to {to_value}')
            return

        answer = CONVERSION_RATES[(from_value, to_value)] * value
        answer_label.config(text='Answer: ' + str(answer))

    convert_btn = tk.Button(root, text='Convert', command=convert_units)
    convert_btn.grid(row=4, column=1, columnspan=2)
    answer_label.grid(row=5, column=1, columnspan=2, pady=bottom_padding)

    root.mainloop()
