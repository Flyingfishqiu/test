from jsonpath_rw import parse
from commom.operation_excle import OperationExcle
from commom.Request import Menstent
from commom.get_data import Get_data


class DependdentData(object):
    def __init__(self, case_id):
        self.case_id = case_id
        self.excle = OperationExcle()
        self.run = Menstent()
        self.data = Get_data()

    def get_case_line_data(self):
        row_date = self.excle.get_case_id_to_value(self.case_id)
        return row_date

    def run_depent(self):
        row = self.excle.get_case_id_row(self.case_id)
        url = self.data.get_case_Url(row)
        method = self.data.get_methods(row)
        req_data = self.data.get_data(row)
        headers = self.data.get_case_headers(row)
        return self.run.run_man(url, method,req_data, headers)

    def get_data_depend_data(self, row):
        depend_data = self.data.get_depend_data(row)
        res_data = self.run_depent()
        json_re = parse(depend_data)
        masle = json_re.find(res_data)
        return [math.value for math in masle][0]
