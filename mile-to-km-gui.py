from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# Text Entry 
my_entry = Entry(width=7)
my_entry.grid(column=2, row=2)


#Label
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=2)


#Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=3)

#Label
km_result_label = Label(text="0")
km_result_label.grid(column=2, row=3)


#Label
km_label = Label(text="Km")
km_label.grid(column=3, row=3)


def convert():
    miles = float(my_entry.get())
    km = round(miles*1.60934)
    km_result_label.config(text=km)

#Button
cal_button = Button(text="Calculate", command=convert)
cal_button.grid(column=2,row=4)


window.mainloop()