import openpyxl

class ExcelUtility:

    @staticmethod
    def read_cell(path, sheet, row, col):
        workbook = openpyxl.load_workbook(path)
        sheet = workbook[sheet]
        return sheet.cell(row=row, column=col).value

    @staticmethod
    def write_cell(path, sheet, row, col, value):
        workbook = openpyxl.load_workbook(path)
        sheet = workbook[sheet]
        sheet.cell(row=row, column=col).value = value
        workbook.save(path)
