import openpyxl as xl

def load_excel(filepath, filename, sheetname):

    wb = xl.load_workbook(filename=f"{filepath}{filename}", read_only=False, data_only=True, keep_vba=True)
    ws = wb[sheetname]
    return wb, ws

if __name__ == "__main__":
    pass