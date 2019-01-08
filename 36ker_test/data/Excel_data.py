import xlrd


class ExcelUti(object):
    def __init__(self, path, sheet_name):
        self.execl = xlrd.open_workbook(path)
        self.table = self.execl.sheet_by_name(sheet_name)
        self.keys = self.table.row_values(0)
        self.rows = self.table.nrows
        self.col = self.table.ncols
        self.data = []

    def get_data(self):
        if self.rows <= 1:
            print("没有数据")
        else:
            for i in range(1, self.rows):
                item = {}
                for j in range(self.col):
                    ctype = self.table.cell(i, j).ctype
                    value = self.table.cell_value(i, j)
                    if ctype == 2:
                        value = int(value)
                    item[self.keys[j]] = value
                self.data.append(item)
            return self.data


if __name__ == '__main__':
    e = ExcelUti('E:\\frame\\测试\\test\\36ker_test\\data\execl\\login.xlsx', 'Sheet1')
    print(e.get_data())
