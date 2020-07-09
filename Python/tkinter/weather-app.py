import tkinter as tk

WIDTH = 600
HEIGHT = 500

def get_weather(entry):
    label.configure(text='Prototype!!! Weather not available yet!\nEntry: {}'.format(entry))

window = tk.Tk()
window.title('Weather Application')
window.geometry('{}x{}'.format(WIDTH, HEIGHT))

background_image = tk.PhotoImage(file='sunset.png')
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Get Weather', font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(window, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12))
label.place(relwidth=1, relheight=1)

window.mainloop()