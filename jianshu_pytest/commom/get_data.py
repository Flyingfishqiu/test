from commom.operation_excle import OperationExcle
from commom.Operation_json import Operation_Json
from config import data_config


class Get_data(object):
    def __init__(self):
        self.execl = OperationExcle()
        self.json_ = Operation_Json()

    def get_case_count(self):
        return self.execl.get_row_line()

    def get_case_id(self, row):
        col = data_config.get_Case_Id()
        Id = self.execl.get_call_value(row, col)
        return Id

    def get_case_name(self, row):
        col = data_config.get_Case_name()
        name = self.execl.get_call_value(row, col)
        return name

    def get_case_Url(self, row):
        col = data_config.get_Case_url()
        url = self.execl.get_call_value(row, col)
        return url

    def get_case_headers(self, row):
        col = data_config.get_Case_headers()
        headers = self.execl.get_call_value(row, col)
        if headers:
            return data_config.get_headers_value()
        else:
            return None

    def get_is_run(self, row):
        col = data_config.get_is_run()
        run_mode = self.execl.get_call_value(row, col)
        if run_mode == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def get_data(self, row):
        col = data_config.get_Case_data()
        data = self.execl.get_call_value(row, col)
        if data:
            return self.json_.get_value(data)
        else:
            return None

    def get_case_data(self, row):
        col = data_config.get_Case_data()
        data = self.execl.get_call_value(row, col)
        if data:
            return data
        else:
            return None

    def get_methods(self, row):
        col = data_config.get_request_methods()
        return self.execl.get_call_value(row, col)

    def get_expect(self, row):
        col = data_config.get_expect()
        return self.execl.get_call_value(row, col)

    def write_data(self, row, value):
        col = data_config.get_result()
        self.execl.write_sheet(row, col, value)

    def get_depend_data(self, row):
        col = data_config.get_depend_data()
        depend_data = self.execl.get_call_value(col, row)
        if depend_data:
            return depend_data
        else:
            return None

    def is_dependent(self, row):
        col = data_config.get_depend_field()
        depen_field = self.execl.get_call_value(col, row)
        if depen_field:
            return depen_field
        else:
            return None

if __name__ == '__main__':
    print(Get_data().get_is_run(2))


