from tkinter import *

def clicked(color):
    label.configure(text=color[0])
    enter.delete(first=0, last=END)
    enter.insert(0, color[1])

root = Tk()
root.geometry('500x200')

label = Label(root, font=('Arial', 16))
enter = Entry(root, font=('Arial', 16))
main_frame = Frame(borderwidth=0, relief=SOLID, pady=20)

red = Button(main_frame, bg='#FF0000', command=lambda: clicked(["красный", '#FF0000']), width=8, height=4)
ogange = Button(main_frame, bg='#FF7B00', command=lambda: clicked(["оранжевый", '#FF7B00']), width=8, height=4)
yellow = Button(main_frame, bg='#FFF600', command=lambda: clicked(["жёлтый", '#FFF600']), width=8, height=4)
green = Button(main_frame, bg='#00FF00', command=lambda: clicked(["зелёный", '#00FF00']), width=8, height=4)
light_blue = Button(main_frame, bg='#00D5FF', command=lambda: clicked(["голубой", '#00D5FF']), width=8, height=4)
blue = Button(main_frame, bg='#0000FF', command=lambda: clicked(["синий", '#0000FF']), width=8, height=4)
purple = Button(main_frame, bg='#C300FF', command=lambda: clicked(["фиолетовый", '#C300FF']), width=8, height=4)

spacer1 = Label(main_frame, width=1)
spacer2 = Label(main_frame, width=1)
spacer3 = Label(main_frame, width=1)
spacer4 = Label(main_frame, width=1)
spacer5 = Label(main_frame, width=1)
spacer6 = Label(main_frame, width=1)

label.pack(side=TOP)
enter.pack(side=TOP)

red.pack(side=LEFT)
spacer1.pack(side=LEFT)

ogange.pack(side=LEFT)
spacer2.pack(side=LEFT)

yellow.pack(side=LEFT)
spacer3.pack(side=LEFT)

green.pack(side=LEFT)
spacer4.pack(side=LEFT)

light_blue.pack(side=LEFT)
spacer5.pack(side=LEFT)

blue.pack(side=LEFT)
spacer6.pack(side=LEFT)

purple.pack(side=LEFT)

main_frame.pack(anchor='n')

root.title('First task')
root.mainloop()
