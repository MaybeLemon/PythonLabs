from tkinter import *
from tkinter.ttk import *
from know import Know
from kolvo import Kolvo
from name import Name
from tomatoes import Tomatos


def main():
    root = Tk()
    root.geometry('1024x768')

    know_frame = Know()
    know_frame.start()

    kolvo_frame = Kolvo(root, lambda: name_frame.start())
    name_frame = Name(root, lambda: tomatoes_frame.start(kolvo_frame.get_vvod(), name_frame.get_vvod()))
    kolvo_frame.start()

    tomatoes_frame = Tomatos(root)

    root.title('a')
    root.mainloop()


if __name__ == '__main__':
    main()
