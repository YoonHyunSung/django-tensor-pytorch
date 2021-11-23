import os
import django
import csv
import pandas as pd
import sys

from icecream import ic

from common.models import ValueObject, Printer, Reader

class Norminal():
    def start_norminal(self):
        Norminal().case_norminal()
        Norminal().policy_norminal()
        Norminal().daily_confirmd()
    def __init__(self):
        pass
    def new_model(self, payload)->object:
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'data/'
        vo.fname = payload
        self.csvfile = reader.new_file(vo)
        return self.csvfile


    def case_norminal(self):
        case = pd.read_csv(self.new_model('Case.csv'))
        case = case.drop(columns=['latitude','longitude'],axis=1)
        case.loc[case['city'] =='-','city'] = 'unknown'
        case.loc[case['city'] == 'from other city', 'city'] = 'othercity'
        #ic(case)
        case.to_csv('data/Ncase.csv', encoding='utf8', index=False)
        #ic(case['city'])

    def policy_norminal(self):
        policy = pd.read_csv(self.new_model('Policy.csv'))
        policy['end_date'] = policy['end_date'].fillna('unknown')
        ic(policy)
        policy.to_csv('data/Npolicy.csv', encoding='utf8', index=False)
    def daily_confirmd(self):
        confirmed = pd.read_csv(self.new_model('time_series_covid19_confirmed_global.csv'))
        korea = confirmed[confirmed['Country/Region'] == 'Korea, South'].iloc[:, 4:].T
        korea.rename(columns={157:'daily_confirm'}, inplace=True)
        ic(korea)
        korea.index = pd.to_datetime(korea.index)
        korea.diff()
        daily_cases = korea.diff().fillna(korea.iloc[0]).astype('int')
        daily_cases.insert(0, "date", korea.index, True)
        daily_cases.to_csv('data/norminal_data/Korea.csv', encoding='utf8', index=False)




if __name__ == '__main__':
    Norminal().start_norminal()
