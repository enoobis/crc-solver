import tkinter as tk

# Define the color codes and their corresponding values
color_codes = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4,
               'green':5, 'blue':6, 'violet':7, 'gray':8, 'white':9,
               'gold':-1, 'silver':-2}

# Define the tolerance values for each tolerance band color
tolerance_values = {'brown':1, 'red':2, 'green':0.5, 'blue':0.25, 'violet':0.1,
                    'gray':0.05, 'gold':5, 'silver':10}

# Define the colors for the dark theme
bg_color = '#1e1e1e'
fg_color = '#c5c5c5'
hl_color = '#404040'
err_color = '#ff5e5e'
button_bg_color = '#424242'

class ResistorApp:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title('Resistor Color Code Calculator')
        self.root.geometry('500x200')
        self.root.config(bg=bg_color)

        # Create the color band input fields
        self.band1 = tk.Entry(self.root, width=10, bg=bg_color, fg=fg_color, highlightbackground=hl_color, highlightcolor=hl_color, highlightthickness=1)
        self.band1.grid(row=0, column=0, padx=5, pady=5)
        self.band2 = tk.Entry(self.root, width=10, bg=bg_color, fg=fg_color, highlightbackground=hl_color, highlightcolor=hl_color, highlightthickness=1)
        self.band2.grid(row=0, column=1, padx=5, pady=5)
        self.band3 = tk.Entry(self.root, width=10, bg=bg_color, fg=fg_color, highlightbackground=hl_color, highlightcolor=hl_color, highlightthickness=1)
        self.band3.grid(row=0, column=2, padx=5, pady=5)
        self.band4 = tk.Entry(self.root, width=10, bg=bg_color, fg=fg_color, highlightbackground=hl_color, highlightcolor=hl_color, highlightthickness=1)
        self.band4.grid(row=0, column=3, padx=5, pady=5)

        # Create the labels for the input fields
        tk.Label(self.root, text='Band 1', bg=bg_color, fg=fg_color).grid(row=1, column=0)
        tk.Label(self.root, text='Band 2', bg=bg_color, fg=fg_color).grid(row=1, column=1)
        tk.Label(self.root, text='Band 3', bg=bg_color, fg=fg_color).grid(row=1, column=2)
        tk.Label(self.root, text='Band 4', bg=bg_color, fg=fg_color).grid(row=1, column=3)


        # Create the labels for the resistance value and tolerance
        self.resistance_label = tk.Label(self.root, text='', bg=bg_color, fg=fg_color, font=('Helvetica', 16, 'bold'))
        self.resistance_label.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
        self.tolerance_label = tk.Label(self.root, text='', bg=bg_color, fg=fg_color)
        self.tolerance_label.grid(row=5, column=1, columnspan=2, padx=5, pady=5)
    
        # Create the label for error messages
        self.error_label = tk.Label(self.root, text='', bg=bg_color, fg=err_color)
        self.error_label.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

        # Create the button to calculate the resistance value
        self.calculate_button = tk.Button(self.root, text='Calculate', command=self.calculate_resistance, bg=button_bg_color, fg=fg_color, font=('Helvetica', 14))
        self.calculate_button.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
    
        # Start the main event loop
        self.root.mainloop()
    
    def calculate_resistance(self):
        # Get the color bands from the input fields
        band1_color = self.band1.get().lower()
        band2_color = self.band2.get().lower()
        band3_color = self.band3.get().lower()
        band4_color = self.band4.get().lower()
    
        # Check that the colors are valid
        if band1_color not in color_codes or band2_color not in color_codes or band3_color not in color_codes or band4_color not in tolerance_values:
            self.error_label.config(text='Invalid color code')
            self.resistance_label.config(text='')
            self.tolerance_label.config(text='')
            return
    
        # Calculate the resistance value
        resistance_value = (color_codes[band1_color]*10 + color_codes[band2_color])*10**color_codes[band3_color]
        resistance_suffix = ''
        if resistance_value >= 1000000:
            resistance_value /= 1000000
            resistance_suffix = 'M'
        elif resistance_value >= 1000:
            resistance_value /= 1000
            resistance_suffix = 'k'
        resistance_string = f'{resistance_value:g}{resistance_suffix}'
    
        # Calculate the tolerance
        tolerance_value = tolerance_values[band4_color]
        if tolerance_value >= 1:
            tolerance_string = f'±{tolerance_value}%'
        else:
            tolerance_string = f'±{tolerance_value*1000:g}m%'
        
        # Update the labels
        self.error_label.config(text='')
        self.resistance_label.config(text=resistance_string)
        self.tolerance_label.config(text=tolerance_string)

app = ResistorApp()
