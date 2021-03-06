from commom.Request import Menstent
from commom.get_data import Get_data
from commom.is_content import is_contents
from commom.operation_excle import OperationExcle
from data.dependdent_data import DependdentData


class Run_Test(object):
    def __init__(self):
        self.men = Menstent()
        self.getdata = Get_data()
        self.excle = OperationExcle()


    def go_on_run(self):
        for i in range(1, self.getdata.get_case_count()):
            methods = self.getdata.get_methods(i)
            url = self.getdata.get_case_Url(i)
            data = self.getdata.get_data(i)
            expect = self.getdata.get_expect(i)
            case_id = self.getdata.get_case_id(i)
            depend = DependdentData(case_id)

            if self.getdata.is_dependent(i):
                depend_data = depend.get_data_depend_data(i)
                depend_key = self.getdata.is_dependent(i)
                data[depend_key] = depend_data

            ret = self.men.run_man(rev_method=methods, url=url, data=data)
            if is_contents(expect, ret):
                self.getdata.write_data(i, 'pass')
            else:
                self.getdata.write_data(i, 'fail')


if __name__ == '__main__':
    run = Run_Test()
    run.go_on_run()
