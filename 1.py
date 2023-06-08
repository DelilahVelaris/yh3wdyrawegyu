from tkinter import*
import random

root = Tk()
root.title("List")
root.geometry("400x400")

random_label = Label(root)
sorted_label = Label(root)

def generate():
    random_list = random.sample(range(9, 90), 9)
    random_label["text"] = "Random list : "+ str(random_list)
    random_list.sort()
    sorted_label["text"] = "Sorted list : "+ str(random_list)

btn = Button(root, text = "Generate List", command = generate)

btn.place(relx=0.5, rely=0.3, anchor=CENTER)
random_label.place(relx=0.5, rely=0.4, anchor=CENTER)
sorted_label.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()