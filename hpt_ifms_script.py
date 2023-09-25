from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time, schedule, sqlite3
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime


def scrapping(from_date, to_date):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    url = 'https://himkosh.nic.in/eHPOLTIS/PublicReports/wfrmBudgetAllocationbyFD.aspx'
    driver.get(url)

    time.sleep(5)
    # Select the financial year you want to scrape data for
    financial_from_date_input = driver.find_element(By.ID, 'txtFromDate')
    financial_from_date_input.clear()
    financial_from_date_input.send_keys(from_date)

    financial_to_date_input = driver.find_element(By.ID, 'txtQueryDate')
    financial_to_date_input.clear()
    financial_to_date_input.send_keys(to_date)

    # Rupees Radio Button Select
    radio_button = driver.find_element(By.ID, 'MainContent_rbtUnit_0')
    radio_button.click()


    # Clicking the "View Data" button to generate the report
    view_button = driver.find_element(By.ID, 'btnGetdata')
    view_button.click()

    # Wait for the report to load (you might need to adjust the sleep time based on your internet speed)
    time.sleep(20)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')
    table = soup.find('table', class_='table table-responsive table-striped')
    rows = table.find_all('tr')
    col_names = [item.text for item in rows[2]]
    df = pd.DataFrame(columns = col_names)

    for row in rows[3:]:
        curr_row = [item.text for item in row]
        length = len(df)
        df.loc[length] = curr_row

    driver.quit()

    df['DmdCd'].replace('', np.NaN, inplace=True)

    df['DmdCd'].ffill(inplace=True)

    df1 = df.drop(0)

    df_ = df1.copy()
    for i, r in df_.iterrows():
        if r['HOA'] == 'Total':
            df_.drop(i, inplace=True)
            continue

    df_[['DemandCode', 'Demand']] = df_['DmdCd'].str.split('-', n=1, expand=True)

    df_[['MajorHead', 'SubMajorHead', 'MinorHead', 'SubMinorHead', 'DetailHead', 'SubDetailHead', 'BudgetHead', 'PlanNonPlan', 'VotedCharged', 'StatementofExpenditure']] = df_['HOA'].str.split('-', n=9, expand=True)

    df_ = df_.drop(['DmdCd', 'HOA'], axis=1)

    new_cols = ['DemandCode', 'Demand', 'MajorHead', 'SubMajorHead', 'MinorHead', 'SubMinorHead', 'DetailHead', 'SubDetailHead', 'BudgetHead', 'PlanNonPlan', 'VotedCharged', 'StatementofExpenditure', 'Sanction Budget(April)', 'Addition', 'Saving',	'Revised Budget(A)', 'Expenditure(within selected period) (B)',	'Balance(A-B)']
    df_=df_.reindex(columns=new_cols)

    dateTime = datetime.now()
    conn = sqlite3.connect('hpt_ifms_scripted.sqlite')
    df_.to_sql(f"Sanctioned Budget Additionality, Saving and Revised with Expenditure {dateTime}", conn, if_exists='replace', index=False)
    conn.close()

schedule.every(30).day.at("10:30").do(scrapping, from_date = '01/04/2018', to_date = '31/03/2022')
#schedule.every(1).minutes.do(scrapping, from_date = '01/04/2018', to_date = '31/03/2022') #Testing

while True:
    schedule.run_pending()
    print("script running")
    time.sleep(1)
