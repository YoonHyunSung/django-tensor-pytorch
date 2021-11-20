import os

from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from icecream import ic
from common.models import ValueObject
import schedule



def covid_scraper():
    vo = ValueObject()
    vo.context = 'data/'
    vo.url = 'http://ncov.mohw.go.kr/'
    driver = webdriver.Chrome(f'{vo.context}chromedriver')
    driver.get(vo.url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tables = soup.select('table')
    table = tables[0]
    table_html = str(table)
    table_df_list = pd.read_html(table_html)
    # ic(table_df_list)
    table_df = table_df_list[0]
    # ic(table_df[0])
    table_df = table_df.loc[:, ['구분', '사망', '재원 위중증', '신규 입원', '확진']]

    ic(table_df)
    table_df = table_df.iloc[0:,1:]
    ic(table_df)
    table_df.rename(columns={'구분':'sortation','사망':'death','재원 위중증':'serious','신규 입원':'new_hospitalization','확진':'confirmed'},inplace=True)
    table_df.to_csv(vo.context + 'covid_case.csv', index=False)
    driver.close()

def live():
    schedule.every().day.at("00:00").do(covid_scraper())
