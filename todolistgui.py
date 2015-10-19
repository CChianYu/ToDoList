from tkinter import *

class ToDoListGUI(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

        self.todoCnt = 1
        
    def createWidgets(self):

        #Dead Line:
        self.timeText = Label(self, text="Dead Line:")
        self.timeText.grid(row=0, column=0)
        self.makeMonthMenu()
        self.makeDateMenu()
        self.makeHourMenu()
        self.makeMinuteMenu()

        #ToDo:
        self.todoText = Label(self)
        self.todoText["text"] = "ToDo:"
        self.todoText.grid(row=1, column=0)
        self.todoField = Entry(self)
        self.todoField["width"] = 50
        self.todoField.grid(row = 1, column=1, columnspan=6)

        #Add Button
        self.add = Button(self, command=self.addMethod)
        self.add["text"] = "Add"
        self.add.grid(row=2, column=0)

        #Remove Button
        self.remove = Button(self, text="Remove", command=self.removeMethod)
        self.remove.grid(row=2, column=1)

        #prompt message
        self.displayText = Label(self)
        self.displayText["text"] = ""
        self.displayText.grid(row=4, column=0, columnspan=7)

        #All To Do
        self.todoFrame = LabelFrame(self)
        self.todoFrame["text"] = "To Do List"
        self.todoFrame.grid(row=3, columnspan=7)
        self.todoFrame.columnconfigure(0, weight=1)
        self.todoList = Listbox(self.todoFrame, width=50)
        self.todoList.grid()
    
    def makeMonthMenu(self):
        self.monthVal = StringVar()
        self.monthVal.set("Month")
        self.monthMenu = Menubutton(self, text="Month", textvariable=self.monthVal)
        self.monthMenu.grid(row=0, column=1)
        self.month = Menu(self.monthMenu, tearoff=0)
        self.monthMenu["menu"] = self.month
        for i in range(1,13):
            self.month.add_radiobutton(label=str(i), variable=self.monthVal, value=str(i), command=self.whenMonthMenubuttonClicked)
  
    def makeDateMenu(self):
        self.dateVal = StringVar()
        self.dateVal.set("Date")
        self.DateMenu = Menubutton(self, text="Date", textvariable=self.dateVal)
        self.DateMenu.grid(row=0, column=2)
        self.Date = Menu(self.DateMenu, tearoff=0)
        self.DateMenu["menu"] = self.Date
        
        date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if self.monthVal.get() != "Month":
            for i in range(1,date[int(self.monthVal.get())-1]+1):
                self.Date.add_radiobutton(label=str(i), variable=self.dateVal, value=str(i))

    def makeHourMenu(self):
        self.hourVal = StringVar()
        self.hourVal.set("Hour")
        self.hourMenu = Menubutton(self, text="Hour", textvariable=self.hourVal)
        self.hourMenu.grid(row=0, column=3)
        self.hour = Menu(self.hourMenu)
        self.hourMenu["menu"] = self.hour

        for i in range(0, 24):
            self.hour.add_radiobutton(label=str(i), variable=self.hourVal, value=str(i))

    def makeMinuteMenu(self):
        self.minuteVal = StringVar()
        self.minuteVal.set("Minute")
        self.minuteMenu = Menubutton(self, text="Minute", textvariable=self.minuteVal)
        self.minuteMenu.grid(row=0, column=4)
        self.minute = Menu(self.minuteMenu)
        self.minuteMenu["menu"] = self.minute
        for i in range(0, 60, 30):
            self.minute.add_radiobutton(label=str(i), variable=self.minuteVal, value=str(i))

    def addMethod(self):

        #check if users done the form
        if self.monthVal.get()=="Month" or self.dateVal.get()=="Date" or self.hourVal.get()=="Hour" or self.minuteVal.get()=="Minute" or self.todoField.get()=="":
            self.displayText["text"] = "You need to complete the up forms first. ^^"
            return
        
        #add a task to my todoListbox
        todoText = "Dead Line: " + self.monthVal.get() + "/" + self.dateVal.get() + " " + self.hourVal.get() + ":" + self.minuteVal.get() + " Task: " + self.todoField.get()
        self.todoList.insert(0, todoText)
        self.displayText["text"] = "Add to ToDoList!!"

        #clear forms
        self.monthVal.set("Month")
        self.dateVal.set("Date")
        self.hourVal.set("Hour")
        self.minuteVal.set("Minute")
        self.todoField.delete(0, 50)
    
    def removeMethod(self):
        selection = self.todoList.curselection()
        
        #selection is a list, if len=0, then selection is empty
        #it's contain a string list
        if len(selection) == 0:
            self.displayText["text"] = "Choose a ToDo task to remove."
            return

        self.displayText["text"] = "Remove " + self.todoList.get(selection[0])
        self.todoList.delete(selection[0])

    def whenMonthMenubuttonClicked(self):
        self.DateMenu.destroy()
        self.makeDateMenu()

if __name__=='__main__':
    root = Tk()
    app = ToDoListGUI(master=root)
    app.mainloop()
