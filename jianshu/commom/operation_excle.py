import xlrd
from xlutils3 import copy


# f = xlrd.open_workbook('')
# tabel =f.sheets()[0]


class OperationExcle(object):
    def __init__(self, path=None, index=0):
        if path:
            self.path = path
            self.index = index
        else:
            self.path = '../data/test.xls'
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

    # 根据case_id 获取对应行的内容
    def get_case_id_to_value(self, case_id):
        row = self.get_case_id_row(case_id)
        return self.get_row_value(row)

    # 根据 行号获取对应的内容
    def get_row_value(self, row):
        return self.table.row_values(row)

    # 根据 case_id 获取行号
    def get_case_id_row(self, case_id):
        cols = self.get_cols_data()
        nomber = 0
        for col in cols:
            if case_id in col:
                return nomber
            nomber += 1
        return nomber

    # 根据 列号 获取对应列的数据
    def get_cols_data(self, col=None):
        if col:
            cols = self.table.col_values(col)
        else:
            cols = self.table.col_values(0)
        return cols


if __name__ == '__main__':
    # path = 'D:\\测试\\project\\jianshu\\data\\test2.xlsx'
    file = OperationExcle()
    # file.write_sheet(3, 8, 'pass')
