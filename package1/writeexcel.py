import openpyxl
path="C:\\Users\Chandan Ghosh\Desktop\pythonexcel.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook.active

for r in range(4,9):
    for c in range(1,4):
        sheet.cell(r,c).value="Welcome"

workbook.save(path)


