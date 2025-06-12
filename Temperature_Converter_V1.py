''' Version 1: Purpose of program is to convert C to F or vise versa.
Version 1 goal is: Setting up frames and making the C to F and F to C buttons work.
Version 2 goal is: Adding weight to widgets so that they adjust to the window size.
Version 3 goal is: Adding validation to inputs.'''

import tkinter as tk

class Converter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Temperature Converter")

        self.container = tk.Frame(self.root)
        self.container.grid(row = 0, column = 0, sticky = "NESW")
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)      
        

        self.frames = {}
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_cFrame()
        self.frames["to_fFrame"] = self.create_to_fFrame()

        self.show_frame("MainFrame")
        
        self.c_conversion_answer = tk.IntVar()
        self.f_conversion_answer = tk.IntVar()
        
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)      
        
    def run(self):
        self.root.mainloop()

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def create_main_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        main_label = tk.Label(frame, text = "Temperature Converter", font = "Verdana 22 bold")
        main_label.grid(row = 0, column = 0, columnspan = 2)

        self.to_c_button = tk.Button(frame, text = "to Centigrade", bg = "yellow",
                                     font = "Verdana 12 bold",
                                     command = lambda: self.show_frame("to_cFrame"))
        self.to_c_button.grid(row = 1, column = 0, sticky = "NESW")

        self.to_f_button = tk.Button(frame, text = "to Fahrenheit", bg = "pink",
                                     font = "Verdana 12 bold",
                                     command = lambda: self.show_frame("to_fFrame"))
        self.to_f_button.grid(row= 1, column = 1, sticky = "NESW")
        
        for i in range(2):
            frame.grid_rowconfigure(i, weight = 1)
        for j in range(2):
            frame.grid_columnconfigure(j, weight = 1)

        return frame
        
    def create_to_cFrame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        label = tk.Label(frame, text = "Enter the temperature in Centigrade", font = "Arial 12 bold")
        label.grid(row = 0, column = 0, columnspan = 3, sticky = "NESW")

        self.temp_entry_c = tk.Entry(frame, justify = "center")
        self.temp_entry_c.grid(row = 1, column = 0, sticky = "NSWE", columnspan = 3)
                
        calculate_button = tk.Button(frame, text = "Calculate", command = lambda: self.calculate_c_to_f())
        calculate_button.grid(row = 2, column = 0, sticky = "NSWE")
        
        back_button = tk.Button(frame, text = "Back", command = lambda: self.show_frame("MainFrame"))
        back_button.grid(row = 2, column = 1, sticky = "NSWE")
        
        reset_button = tk.Button(frame, text = "Reset", command = lambda: self.reset())
        reset_button.grid(row = 2, column = 2, sticky = "NSWE")
        
        self.c_conversion_label = tk.Label(frame, text = "Converted temperature goes here")
        self.c_conversion_label.grid(row = 3, column = 0, columnspan = 3, sticky = "NSEW")

        for i in range(4):
            frame.grid_rowconfigure(i, weight = 1)
        for j in range(3):
            frame.grid_columnconfigure(j, weight = 1)

        return frame

    def create_to_fFrame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        label = tk.Label(frame, text = "Enter the temperature in Fahrenheit", font = "Arial 12 bold")
        label.grid(row = 0, column = 0, columnspan = 3, sticky = "NESW")

        self.temp_entry_f = tk.Entry(frame, justify = "center")
        self.temp_entry_f.grid(row = 1, column = 0, columnspan = 3, sticky = "NSEW")

        calculate_button = tk.Button(frame, text = "Calculate", command = lambda: self.calculate_f_to_c())
        calculate_button.grid(row = 2, column = 0, sticky = "NESW")
        
        back_button = tk.Button(frame, text = "Back", command = lambda: self.show_frame("MainFrame"))
        back_button.grid(row = 2, column = 1, sticky = "NESW")
        
        reset_button = tk.Button(frame, text = "Reset", command = lambda: self.reset())
        reset_button.grid(row = 2, column = 2, sticky = "NESW")
        
        self.f_conversion_label = tk.Label(frame, text = "Converted temperature goes here")
        self.f_conversion_label.grid(row = 3, column = 0, columnspan = 3, sticky = "NESW")

        for i in range(4):
            frame.grid_rowconfigure(i, weight = 1)
        for j in range(3):
            frame.grid_columnconfigure(j, weight = 1)

        return frame

    def calculate_c_to_f(self):
        if not self.temp_entry_c.get().lstrip("-").isnumeric():
            self.c_conversion = "Invalid input, please enter a number"        
        elif float(self.temp_entry_c.get()) < -273.15:
            self.c_conversion = "Invalid temperature, can't go below absolute zero"
        elif float(self.temp_entry_c.get()) == -273.15:
            self.c_conversion = "Absolute zero, -459.67 Fahrenheit" 
        else:
            self.c_conversion = f"{round((float(self.temp_entry_c.get()) * 1.8) + 32, 2)} Fahrenheit"

        self.c_conversion_answer.set(self.c_conversion)

        self.c_conversion_label.config(text = self.c_conversion)

    def calculate_f_to_c(self):
        if not self.temp_entry_f.get().lstrip("-").isnumeric():
            self.f_conversion = "Invalid input, please enter a number"
        elif float(self.temp_entry_f.get()) < -459.67:
            self.f_conversion = "Invalid temperature, can't go below absolute zero"
        elif float(self.temp_entry_f.get()) == -459.67:
            self.f_conversion = "Absolute zero, -273.15 Centigrade"
        else:
            self.f_conversion = f"{round((float(self.temp_entry_f.get()) - 32) * 5 / 9, 2)} Centigrade"
        self.f_conversion_answer.set(self.f_conversion)

        self.f_conversion_label.config(text = self.f_conversion)
                                       
    def reset(self):
        self.temp_entry_c.delete(0, tk.END)
        self.temp_entry_f.delete(0, tk.END)
        self.c_conversion_label.config(text = "Converted temperature goes here")
        self.f_conversion_label.config(text = "Converted temperature goes here")

if __name__ == "__main__":
    app = Converter()
    app.run()