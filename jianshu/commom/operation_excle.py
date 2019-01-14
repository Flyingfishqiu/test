import xlrd
from xlutils3 import copy


# f = xlrd.open_workbook('')
# tabel =f.get_sheet()[0]
# tabel.cell_value()


class OperationExcle(object):
    def __init__(self, path=None, index=0):
        if path:
            self.path = path
            self.index = index
        else:
            self.path = 'D:\\测试\\project\\jianshu\\data\\test.xlsx'
            self.index = 0
        self.table = self.get_table()

    def get_table(self):
        file = xlrd.open_workbook(self.path)
        table = file.sheets()[self.index]
        return table

    def get_call_value(self, rowx, colx):
        return self.table.cell_value(rowx, colx)

    def get_row_line(self):
        return self.table.nrows

    def write_sheet(self, row, col, value):
        data = xlrd.open_workbook(self.path)
        copy_data = copy.copy(data)
        table = copy_data.get_sheet(0)
        table.write(row, col, value)
        copy_data.save(self.path)


if __name__ == '__main__':
    path = 'D:\\测试\\project\\jianshu\\data\\test2.xlsx'
    file = OperationExcle(path)
    file.write_sheet(3, 8, 'pass')