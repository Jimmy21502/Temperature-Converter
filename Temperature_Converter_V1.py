''' Version 1: Purpose of program is to convert C to F or vise versa.
Version 1 goal is: Setting up frames and making the C to F and F to C buttons work.'''

import tkinter as tk

class Converter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Temperature Converter")

        self.container = tk.Frame(self.root)
        self.container.pack()

        self.frames = {}
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_cFrame()
        self.frames["to_fFrame"] = self.create_to_fFrame()
        self.show_frame("MainFrame")
        
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

        self.to_c_button = tk.Button(frame, text = "to Centrigrade", bg = "yellow",
                                     font = "Verdana 12 bold",
                                     command = lambda: self.show_frame("to_cFrame"))
        self.to_c_button.grid(row = 1, column = 0, sticky = "NESW")

        self.to_f_button = tk.Button(frame, text = "to Fahrenheit", bg = "pink",
                                     font = "Verdana 12 bold",
                                     command = lambda: self.show_frame("to_fFrame"))
        self.to_f_button.grid(row = 1, column = 1, sticky = "NESW")        
        
        return frame
        
    def create_to_cFrame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        label = tk.Label(frame, text = "Enter the temperature in Fahrenheit")
        label.grid(row = 0, column = 0)

        self.temp_entry_c = tk.Entry(frame, justify = "center")
        self.temp_entry_c.grid(row = 1, column = 0)

        back_button = tk.Button(frame, text="Back", command=lambda: self.show_frame("MainFrame"))
        back_button.grid(row = 2, column = 0)

        return frame

    def create_to_fFrame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        label = tk.Label(frame, text = "Enter the temperature in Centigrade")
        label.grid(row = 0, column = 0)

        self.temp_entry_f = tk.Entry(frame, justify = "center")
        self.temp_entry_f.grid(row = 1, column = 0)

        back_button = tk.Button(frame, text = "Back", command = lambda: self.show_frame("MainFrame"))
        back_button.grid(row = 2, column = 0)

        return frame

if __name__ == "__main__":
    app = Converter()
    app.run()