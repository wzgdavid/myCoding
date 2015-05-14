# encoding: utf-8
from excel_app import app

class Model(object):
    pass



class Bar(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    

    print app.sheet.cell(0, 0).value
    print app.sheet.row_values(0)