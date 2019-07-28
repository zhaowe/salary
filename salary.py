from Tkinter import *
import ttk
import glob
from openpyxl import load_workbook

def get_books(path):
    books = []
    for book in glob.glob(path+'/*.xlsx'):
        books.append(book.split('/')[-1])
    return books

def get_sheets(path, book):
    workbook = load_workbook(path + '/' + book)
    return workbook.worksheets

config_path = '/Users/zhaoweien/workspace/python/tkinter/salary-report'
root = Tk()
root.title('工资管理器')
tree = ttk.Treeview(root)
for year in get_books(config_path):
    print type(year)
    tree.insert('', 'end', year, text=year)
    for month in get_sheets(config_path, year):
        tree.insert(year, 'end', month.title, text=month.title)
tree.pack(side='left', fill='y')
frame = ttk.Frame(root)
frame.pack(side='right', expand=1, fill='both')

rows = 5
columns = 5
for row in range(rows):
    for column in range(columns):
        cell = ttk.Label(frame, text=row)
        cell.grid(row=row, column=column)


root.mainloop()
