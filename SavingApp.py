#!/usr/bin/env python
import tkinter as tk
import random

#template from :
#https://stackoverflow.com/questions/11047803/creating-a-table-look-a-like-tkinter/11049650#11049650

class SavingApp(tk.Tk):
    PLAYER_COLUMN = 0
    MODIFIER_COLUMN = 1
    ROLL_COLUMN = 2
    TOTAL_COLUMN = 3

    def __init__(self):
        tk.Tk.__init__(self)
        #self.minsize(width=700, height=400)
        self.title("Saving App")
        self.characters = 10

        #The character table
        output_headers = ["Player", "Modifier", "Roll", "Total"]
        self.t2 = SimpleTable(self, rows=self.characters, columns=len(output_headers), headers=output_headers)
        self.t2.pack(pady=20, padx=20)
        
        #Roll button
        self.b = tk.Button(self, text = "Saving Roll", width=10, command=self.savingRoll)
        self.b.pack(pady=10)
        
    def rolld20(self):
        return random.randint(1,20)
        
    def isInt(self,value):
        #return False if the field does not contain a number
        try:
            int(value)
            return True
        except ValueError:
            return False
        
    def savingRoll(self):
        #start at 1 to avoid header
        for row in range(1, self.characters):
            #only roll if there is a character name
            if self.t2.get(row,SavingApp.PLAYER_COLUMN):
                modifier = self.t2.get(row, SavingApp.MODIFIER_COLUMN)
                d20 = self.rolld20()
                #default modifier is zero, calculate the total
                total = d20 + (int(modifier) if self.isInt(modifier) else 0)
                
                #write the results to the gui
                self.t2.set(row,SavingApp.ROLL_COLUMN,"%s" % (d20,))
                self.t2.set(row,SavingApp.TOTAL_COLUMN,"%s" % (total,))
        

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=10, columns=2, headers=None):
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                if row == 0:
                    h = headers[column] if headers else "header%s" % (column,)
                    label = tk.Label(self, width=20, text=h, borderwidth=0)
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(label)
                else:
                    entry = tk.Entry(self, width=20)
                    #entry.insert(0, "%s/%s" % (row, column))
                    entry.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(entry)
            self._widgets.append(current_row)
            
        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)
            
    def set(self, row, column, value):
        #Entry rows start at 1 b/c of table header
        widget = self._widgets[row][column]
        widget.delete(0, tk.END)
        widget.insert(0, value)
        
    def get(self, row, column):
        widget = self._widgets[row][column]
        return widget.get()
        
if __name__ == "__main__":
    app=SavingApp()
    app.mainloop()