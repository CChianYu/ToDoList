from tkinter import *

class ToDoListGUI(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

        self.todoCnt = 1
        
    def createWidgets(self):
        self.timeText = Label(self)
        self.timeText["text"] = "Time:"
        self.timeText.grid(row=0, column=0)

        self.monthVal = StringVar()
        self.monthVal.set("Year")
        self.monthMenu = Menubutton(self, text="Year", textvariable=self.monthVal)
        self.monthMenu.grid(row=0, column=1, columnspan=3)
        self.month = Menu(self.monthMenu, tearoff=0)
        self.monthMenu["menu"] = self.month
        self.month.add_radiobutton(label="1", variable=self.monthVal, value="1")
        self.month.add_radiobutton(label="2", variable=self.monthVal, value="2")
        #self.makeMonthMenu()


        self.todoText = Label(self)
        self.todoText["text"] = "ToDo:"
        self.todoText.grid(row=1, column=0)
        self.todoField = Entry(self)
        self.todoField["width"] = 50
        self.todoField.grid(row = 1, column=1, columnspan=6)

        self.add = Button(self, command=self.addMethod)
        self.add["text"] = "Add"
        self.add.grid(row=2, column=0)

        self.remove = Button(self, text="Remove", command=self.removeMethod)
        self.remove.grid(row=2, column=1)

        self.displayText = Label(self)
        self.displayText["text"] = "Message"
        self.displayText.grid(row=4, column=0, columnspan=7)

        self.todoFrame = LabelFrame(self)
        self.todoFrame["text"] = "To Do List"
        self.todoFrame.grid(row=3, columnspan=7, sticky=N)
        self.todoFrame.columnconfigure(0, weight=1)
        self.todoList = Listbox(self.todoFrame)
        self.todoList.grid(sticky=N)

    def addMethod(self):
        self.todoList.insert(0, self.timeField.get() + "\n" + self.todoField.get())
        self.todoCnt+=1
        self.displayText["text"] = "Add to ToDoList!!"
    
    def removeMethod(self):
        selection = self.todoList.curselection()
        
        #selection is a list, if len=0, then selection is empty
        #it's contain a string list
        if len(selection) == 0:
            self.displayText["text"] = "Choose a ToDo task to remove."
            return

        self.todoList.delete(selection[0])

if __name__=='__main__':
    root = Tk()
    app = ToDoListGUI(master=root)
    app.mainloop()
