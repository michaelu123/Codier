from tkinter import *
from tkinter.filedialog import askopenfilenames, askopenfilename
from tkinter.messagebox import *

import os
import locale
import codier

class ButtonEntry(Frame):
    def __init__(self, master, buttontext, stringtext, w, cmd):
        super().__init__(master)
        self.btn = Button(self, text=buttontext, bg="red", bd=4, width=15, height=0, relief=RAISED, command=cmd)
        self.svar = StringVar()
        self.svar.set(stringtext)
        self.entry = Entry(self, textvariable=self.svar, bd=4,
                           width=w, borderwidth=2)
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.btn.grid(row=0, column=0, sticky="w")
        self.entry.grid(row=0, column=1, sticky="we")

    def get(self):
        return self.svar.get()

    def set(self, s):
        return self.svar.set(s)

class LabelEntry(Frame):
    def __init__(self, master, labeltext, stringtext, w):
        super().__init__(master)
        self.label = Label(self, text=labeltext, bd=4, width=15, height=0, relief=RIDGE)
        self.svar = StringVar()
        self.svar.set(stringtext)
        self.entry = Entry(self, textvariable=self.svar, bd=4,
                           width=w, borderwidth=2)
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.label.grid(row=0, column=0, sticky="w")
        self.entry.grid(row=0, column=1, sticky="we")

    def get(self):
        return self.svar.get()

    def set(self, s):
        return self.svar.set(s)

class LabelOM(Frame):
    def __init__(self, master, labeltext, options, initVal, **kwargs):
        super().__init__(master)
        self.options = options
        self.label = Label(self, text=labeltext, bd=4, width=15, relief=RIDGE)
        self.svar = StringVar()
        self.svar.set(initVal)
        self.optionMenu = OptionMenu(self, self.svar, *options, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.label.grid(row=0, column=0, sticky="w")
        self.optionMenu.grid(row=0, column=1, sticky="w")

    def get(self):
        return self.svar.get()

    def set(self, s):
        self.svar.set(s)


class MyApp(Frame):
    def __init__(self, master):
        super().__init__(master)
        w = 50
        self.inputFileBE = ButtonEntry(master, "Eingabedatei", "", w, self.inpFilesSetter)
        self.outputLE = LabelEntry(master, "Ausgabedatei", "sortiertecodiertermine.ods", w)
        self.startBtn = Button(master, text="Start", bd=4, bg="red", width=15, command = self.starten)
        for x in range(1):
            Grid.columnconfigure(master, x, weight=1)
        for y in range(3):
            Grid.rowconfigure(master, y, weight=1)

        self.inputFileBE.grid(row=0, column=0, sticky="we")
        self.outputLE.grid(row=1, column=0, sticky="we")
        self.startBtn.grid(row=2, column=0, sticky="w")

    def inpFilesSetter(self):
        x = askopenfilename(title = "ODS Datei auswählen", defaultextension = ".ods", filetypes = [("ODS", ".ods")])
        self.inputFileBE.set(x)

    def starten(self):
        if self.inputFileBE.get() == "":
            showerror("Fehler", "keine Eingabedatei")
            return
        opath = self.outputLE.get()
        if opath == "":
            showerror("Fehler", "keine Ausgabedatei")
            return
        try:
            abspath = os.path.abspath(opath)
            codier.importods(self.inputFileBE.get(), opath)
            showinfo("Erfolg", f"\nAusgabe in Datei {abspath} erzeugt")
        except Exception as e:
            showerror("Fehler", str(e))

# locale.setlocale(locale.LC_ALL, "de_DE")
locale.setlocale(locale.LC_TIME, "German")
root = Tk()
app = MyApp(root)
app.master.title("Codiertermine")
app.mainloop()


