import os
import django
import csv
import sys

import pandas as pd
from icecream import ic

from common.models import ValueObject, Printer, Reader
from prediction.models import Case, Policy


class DbUploader():
    def __init__(self):
        pass
    def new_csv(self, payload:str):
        vo = ValueObject()
        reader = Reader()
        self.printer =Printer()
        vo.context = 'data/'
        vo.fname = payload
        self.csvfile = reader.new_file(vo)
        return self.csvfile

    def insert_data(self):
        self.insert_case()
    def insert_case(self):
        with open(self.new_csv('Ncase.csv'), newline='', encoding='utf8') as c:
            data_reader = csv.DictReader(c)
            for row in data_reader:
                Case.objects.create(policy_id =row['policy_id'],
                                    country =row['country'],
                                    type =row['type'],
                                    gov_policy =row['gov_policy'],
                                    detail =row['detail'],
                                    start_date =row['start_date'],
                                    end_date =row['end_date'])