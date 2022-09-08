from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

def populate_list():
    items_list.delete(0,END)
    for row in db.fetch():
         items_list.insert(END, row)

def add_item():
    if item_text.get() == '' or quality_text.get() == '' or quantity_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields','Please include all the Fields')
        return
    db.insert(item_text.get(), quality_text.get(), quantity_text.get(), price_text.get())
    items_list.delete(0, END)
    items_list.insert(END, (item_text.get(), quality_text.get(), quantity_text.get(), price_text.get()))
    clear_item()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = items_list.curselection()[0]
        selected_item = items_list.get(index)
    

        item_entry.delete(0, END)
        item_entry.insert(END, selected_item[1])
        quality_entry.delete(0, END)
        quality_entry.insert(END, selected_item[2])
        quantity_entry.delete(0, END)
        quantity_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])

    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_item()
    populate_list()

def update_item():
    db.update(selected_item[0], item_text.get(), quality_text.get(), quantity_text.get(), price_text.get())
    populate_list()

def clear_item():
    item_entry.delete(0, END)
    quality_entry.delete(0, END)
    quantity_entry.delete(0, END)
    price_entry.delete(0, END)



#Create Window Object
app = Tk()

# Item
item_text = StringVar()
item_label = Label(app, text='Item Code', font={'bold', 20}, pady=20)
item_label.grid(row=0, column=0, sticky=W)
item_entry = Entry(app, textvariabl=item_text)
item_entry.grid(row=0, column=1)

# Quantity
quantity_text = StringVar()
quantity_label = Label(app, text='Quantiy', font={'bold', 20})
quantity_label.grid(row=0, column=2, sticky=W)
quantity_entry = Entry(app, textvariabl=quantity_text)
quantity_entry.grid(row=0, column=3)

# Quality
quality_text = StringVar()
quality_label = Label(app, text='Quality', font={'bold', 20})
quality_label.grid(row=0, column=4, sticky=W)
quality_entry = Entry(app, textvariabl=quality_text)
quality_entry.grid(row=0, column=5)


# Price
price_text = StringVar()
price_label = Label(app, text='Price', font={'bold', 20}, pady=20)
price_label.grid(row=1, column=4, sticky=W)
price_entry = Entry(app, textvariabl=price_text)
price_entry.grid(row=1, column=5)


# Items List (Listbox)
items_list = Listbox(app, height=20, width=70)
items_list.grid(row=4, column=0, columnspan=5, rowspan=6, pady=20, padx=20)
# Create Scrollbar
scrollbar = Scrollbar(app) 
scrollbar.grid(row=4, column=4)
# Set Scroll to Listbox
items_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=items_list.yview)
# Bind Select
items_list.bind('<<ListboxSelect>>', select_item)

# Button 
add_btn = Button(app, text='Add', width=12, command=add_item)
add_btn.grid(row=3, column=0, pady=20)

remove_btn = Button(app, text='Remove', width=12, command=remove_item)
remove_btn.grid(row=3, column=1)

update_btn = Button(app, text='Update', width=12, command=update_item)
update_btn.grid(row=3, column=2)

clear_btn = Button(app, text='Clear', width=12, command=clear_item)
clear_btn.grid(row=3, column=3)


app.title('Billing Software')
app.geometry('800x700')

# Populate Data 
populate_list()

# Start Program
app.mainloop()
