import os
import django
import csv

import icecream
import pandas as pd
import sys

from icecream import ic

from common.models import ValueObject, Printer, Reader

class CaseDb():
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'predction/data/'
        vo.fname = 'Case.csv'
        self.csvfile = reader.new_file(vo)
    def case_norminal(self):
        case = pd.read_csv(self.csvfile)
        case['city'] = case['city'].fillna('unkwon')
        ic(case)


    def insert_case(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                print(row)
                CaseDb.




