import csv

from common.models import ValueObject, Reader, Printer
from crwaling_live.models import Crwaling_Live

class DbUploader():
    def __init__(self):
        pass
    def new_csv(self, payload:str):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'crwaling_live/data/'
        vo.fname = payload
        self.csvfile = reader.new_file(vo)
        return self.csvfile

    def insert_case(self):
        with open(self.new_csv('covid_case.csv') , newline='', encoding='utf8') as c:
            data_reader = csv.DictReader(c)
            for row in data_reader:
                Crwaling_Live.objects.create(death=row['death'],
                                    serious=row['serious'],
                                    new_hospitalization=row['new_hospitalization'],
                                    confirmed=row['confirmed'],)
