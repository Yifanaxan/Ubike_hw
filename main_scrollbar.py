import datasource
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        topFrame = ttk.LabelFrame(self,text="台北市行政區")
        topFrame.pack()

        length = len(datasource.sarea_list)
        self.radioStringVar = tk.StringVar()

        for i in range(length):
            cols = i % 3
            rows = i // 3
            ttk.Radiobutton(topFrame,text=datasource.sarea_list[i],value=datasource.sarea_list[i],variable=self.radioStringVar,command=self.radio_Event).grid(column=cols, row=rows, sticky=tk.W, padx=10, pady=10)

        self.radioStringVar.set("士林區")
        self.area_Alldata = datasource.getInfoFromArea(self.radioStringVar.get())

#建立 Treeview------------------------------------------------
        self.bottomFrame = ttk.LabelFrame(self,text=self.radioStringVar.get(),labelanchor="n")
        self.bottomFrame.pack(pady=20)

        columns = ('#1','#2','#3','#4','#5','#6','#7')
        self.tree = ttk.Treeview(self.bottomFrame,columns=columns, show='headings')
        self.tree.heading('#1',text='站點')
        self.tree.column("#1",minwidth=0, width=180)
        self.tree.heading('#2',text='時間')
        self.tree.column("#2",minwidth=0, width=150, anchor='center')
        self.tree.heading('#3',text='總車數')
        self.tree.column("#3",minwidth=0, width=50, anchor='center')
        self.tree.heading('#4',text='可借')
        self.tree.column("#4",minwidth=0, width=50, anchor='center')
        self.tree.heading('#5',text='可還')
        self.tree.column("#5",minwidth=0, width=50, anchor='center')
        self.tree.heading('#6',text='地址')
        self.tree.column("#6",minwidth=0, width=260)
        self.tree.heading('#7',text='狀態')
        self.tree.column("#7",minwidth=0, width=35, anchor='center')
        self.tree.pack(side=tk.LEFT)

        for item in self.area_Alldata:
            self.tree.insert('',tk.END,values=[item['sna'][11:],item['mday'],item['tot'],item['sbi'],item['bemp'],item['ar'],item['act']])

#幫treeview加scrollbar
        scrollbar = ttk.Scrollbar(self.bottomFrame,command=self.tree.yview) 
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

    def radio_Event(self):
        # Clear the treeview
        for child in self.tree.get_children():
            self.tree.delete(child)

        # Get the selected district
        self.area_Alldata = datasource.getInfoFromArea(self.radioStringVar.get())

        # Update the label
        self.bottomFrame.config(text=self.radioStringVar.get())

        # Populate the treeview with the info for the selected district
        for item in self.area_Alldata:
            self.tree.insert('',tk.END,values=[item['sna'][11:],item['mday'],item['tot'],item['sbi'],item['bemp'],item['ar'],item['act']])

def main():
    window=Window()
    window.title("台北市Ubike2.0即時資訊")
    window.mainloop()
    print(Window.area_Alldata)

if __name__ == "__main__":
    main()