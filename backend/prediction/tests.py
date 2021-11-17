import os
import django
import csv
import pandas as pd
import sys

from icecream import ic

from common.models import ValueObject, Printer, Reader

class test():
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'data/'
        vo.fname = 'Case.csv'
        self.csvfile = reader.new_file(vo)


    def case_norminal(self):
        case = pd.read_csv(self.csvfile)
        case = case.drop(columns=['latitude','longitude'],axis=1)
        case.loc[case['city'] =='-','city'] = 'unknown'
        case.loc[case['city'] == 'from other city', 'city'] = 'othercity'
        ic(case)
        case.to_csv('data/new_case.csv', encoding='utf8', index=False)
        ic(case['city'])

if __name__ == '__main__':
    test().case_norminal()