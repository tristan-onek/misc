from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import random

window = Tk()
window.title("Startup Idea Generator")

fontStyle = tkFont.Font(family="Arial", size=12)

window.geometry('1000x200')
window.configure(bg="#F0EBD8")

def clicked():
    verb1 = ["Revolutionizing", "Optimizing", "Pivoting", "Unpacking", "Rethinking", "Disrupting", "Synergizing", "Awakening"]
    adjective = ["ironic", "leveraged", "volatile", "cutting-edge", "late-breaking", "as-a-service", "multi-cloud",
                 "blockchain", "5G", "actionable", "interactive", "IoT"] # bending the definition of adjective a little, it's whatever
    noun1 = ["gentrified burger bars", "organic kombucha", "synthetic meat", "dog racing tracks",
             "horse breeders", "tapir sanctuaries", "SPACs", "ICOs", "stick-and-poke tattoos", "sushi burrito joints",
             "vinyl collections", "Bigfoot deniers", "keto recipes", "cultural influencers", "slam poetry sessions",
             "asbestos removal", "failing downtown bookstores"]
    location = ["Palo Alto", "San Jose", "San Francisco", "Los Angeles", "Austin", "Portland", "Seattle", "New York",
               "Boston", "Cambridge", "Vancouver", "Toronto"]
    verb2 = ["revitalize", "actualize", "harmonize", "re-imagine", "synthesize", "transform"]
    noun2 = ["distressed real estate markets", "amateur magician's associations", "anime conventions",
             "the local water polo team", "the former glory of the Mongol Empire", "clown colleges", "free-form jazz",
             "healing crystal collections", "whatever's going on in Ohio", "warehouse unionization efforts",
             "corporate mindfulness seminars for middle managers", "pretentious startup founders", "your annoying roommate's startup idea"]

    lbl2.configure(text=random.choice(verb1))
    lbl3.configure(text=random.choice(adjective))
    lbl4.configure(text=random.choice(noun1))
    lbl5.configure(text="in")
    lbl6.configure(text=random.choice(location))
    lbl7.configure(text="to")
    lbl8.configure(text=random.choice(verb2))
    lbl9.configure(text=random.choice(noun2))


btn = Button(window, text="GENERATE NEW STARTUP", command=clicked, bg="#748CAB", height = 3, width = 25)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

lbl2 = Label(window, text="")
lbl2.grid(column=1, row=3)
lbl2.config( height=2, bg = "#F0EBD8", font=fontStyle)

lbl3 = Label(window, text="")
lbl3.grid(column=2, row=3)
lbl3.config(height=2, bg = "#F0EBD8", font=fontStyle)

lbl4 = Label(window, text="")
lbl4.grid(column=3, row=3)
lbl4.config(height=2, bg = "#F0EBD8", font=fontStyle)

lbl5 = Label(window, text="")
lbl5.grid(column=4, row=3)
lbl5.config(height=2, bg = "#F0EBD8", font=fontStyle)

lbl6 = Label(window, text="")
lbl6.grid(column=5, row=3)
lbl6.config(height=2, bg = "#F0EBD8", font=fontStyle)

lbl7 = Label(window, text="")
lbl7.grid(column=6, row=3)
lbl7.config(height=2, bg = "#F0EBD8", font=fontStyle)

lbl8 = Label(window, text="")
lbl8.grid(column=7, row=3)
lbl8.config(height=2, bg = "#F0EBD8", font=fontStyle)

lbl9 = Label(window, text="")
lbl9.grid(column=8, row=3)
lbl9.config(height=2, bg = "#F0EBD8", font=fontStyle)

window.mainloop()
