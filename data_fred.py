from fredapi import Fred
import os
from datetime import timedelta
from datetime import datetime
import pandas as pd

def get_cpi():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    cpi = fred.get_series('CPIAUCSL', observation_start=start_date)

    cpi = pd.DataFrame(cpi, columns=['cpi'])

    cpi.index.name = 'Date'

    cpi.to_csv('csv_files/cpi.csv')

def get_nonfarm_payroll():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    payems = fred.get_series('PAYEMS', observation_start=start_date)

    payems = pd.DataFrame(payems, columns=['nonfarm_payroll'])

    payems.index.name = 'Date'

    payems.to_csv('csv_files/nonfarm_payroll.csv')

def get_initial_jobless_claims():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    icsa = fred.get_series('ICSA', observation_start=start_date)

    icsa = pd.DataFrame(icsa, columns=['initial_jobless_claims'])

    icsa.index.name = 'Date'

    icsa.to_csv('csv_files/initial_jobless_claims.csv')

def get_retail_sales():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    retail_sales = fred.get_series('RSXFS', observation_start=start_date)

    retail_sales = pd.DataFrame(retail_sales, columns=['retail_sales'])

    retail_sales.index.name = 'Date'

    retail_sales.to_csv('csv_files/retail_sales.csv')

def get_consumer_sentiment():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    consumer_sentiment = fred.get_series('UMCSENT', observation_start=start_date)

    consumer_sentiment = pd.DataFrame(consumer_sentiment, columns=['consumer_sentiment'])

    consumer_sentiment.index.name = 'Date'

    consumer_sentiment.to_csv('csv_files/consumer_sentiment.csv')

def get_personal_income():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    personal_income = fred.get_series('PI', observation_start=start_date)

    personal_income = pd.DataFrame(personal_income, columns=['personal_income'])

    personal_income.index.name = 'Date'

    personal_income.to_csv('csv_files/personal_income.csv')

def get_gdp():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    gdp = fred.get_series('GDP', observation_start=start_date)

    gdp = pd.DataFrame(gdp, columns=['gdp'])

    gdp.index.name = 'Date'

    gdp.to_csv('csv_files/gdp.csv')

def get_industry_production_index():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    indpro = fred.get_series('INDPRO', observation_start=start_date)

    indpro = pd.DataFrame(indpro, columns=['industry_production_index'])

    indpro.index.name = 'Date'

    indpro.to_csv('csv_files/industry_production_index.csv')

def get_capacity_utilization():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    tcu = fred.get_series('TCU', observation_start=start_date)

    tcu = pd.DataFrame(tcu, columns=['capacity_utilization'])

    tcu.index.name = 'Date'

    tcu.to_csv('csv_files/capacity_utilization.csv')

def get_durable_goods_orders():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    dgo = fred.get_series('DGORDER', observation_start=start_date)

    dgo = pd.DataFrame(dgo, columns=['durable_goods_orders'])

    dgo.index.name = 'Date'

    dgo.to_csv('csv_files/durable_goods_orders.csv')

def get_housing_starts():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    housing_starts = fred.get_series('HOUST', observation_start=start_date)

    housing_starts = pd.DataFrame(housing_starts, columns=['housing_starts'])

    housing_starts.index.name = 'Date'

    housing_starts.to_csv('csv_files/housing_starts.csv')

def get_producer_price_index():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    ppi = fred.get_series('PPIACO', observation_start=start_date)

    ppi = pd.DataFrame(ppi, columns=['producer_price_index'])

    ppi.index.name = 'Date'

    ppi.to_csv('csv_files/producer_price_index.csv')

def get_feds_funds_rate():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    ffr = fred.get_series('FEDFUNDS', observation_start=start_date)

    ffr = pd.DataFrame(ffr, columns=['feds_funds_rate'])

    ffr.index.name = 'Date'

    ffr.to_csv('csv_files/feds_funds_rate.csv')

def get_10_year_treasury():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    ten_year_treasury = fred.get_series('DGS10', observation_start=start_date)

    ten_year_treasury = pd.DataFrame(ten_year_treasury, columns=['10_year_treasury'])

    ten_year_treasury.index.name = 'Date'

    ten_year_treasury = ten_year_treasury.dropna()

    ten_year_treasury.to_csv('csv_files/10_year_treasury.csv')

def get_jolts():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    jolts = fred.get_series('JTSJOL', observation_start=start_date)

    jolts = pd.DataFrame(jolts, columns=['jolts'])

    jolts.index.name = 'Date'

    jolts.to_csv('csv_files/jolts.csv')


def get_sp500():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    sp500 = fred.get_series('SP500', observation_start=start_date)

    sp500 = pd.DataFrame(sp500, columns=['sp500'])

    sp500.index.name = 'Date'

    sp500 = sp500.dropna()

    sp500.to_csv('csv_files/sp500.csv')

def get_average_hourly_earnings():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    ahe = fred.get_series('CES0500000003', observation_start=start_date)

    ahe = pd.DataFrame(ahe, columns=['average_hourly_earnings'])

    ahe.index.name = 'Date'

    ahe.to_csv('csv_files/average_hourly_earnings.csv')

def get_commercial_industrial_loans():

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    fred = Fred(os.getenv("API_FRED"))

    cil = fred.get_series('BUSLOANS', observation_start=start_date)

    cil = pd.DataFrame(cil, columns=['commercial_industrial_loans'])

    cil.index.name = 'Date'

    cil.to_csv('csv_files/commercial_industrial_loans.csv')


if __name__ == "__main__":

    get_cpi() #lagging
    get_nonfarm_payroll() #coincident
    get_initial_jobless_claims() #coincident
    get_retail_sales() #leading
    get_consumer_sentiment() #leading
    get_personal_income() #coincident
    get_gdp() #lagging
    get_industry_production_index() #coincident
    get_capacity_utilization() #coincident
    get_durable_goods_orders() #lagging
    get_housing_starts() #leading
    get_producer_price_index() #lagging
    get_feds_funds_rate() #lagging
    get_10_year_treasury() #lagging
    get_jolts() #coincident
    get_sp500() #leading
    get_average_hourly_earnings() #leading
    get_commercial_industrial_loans() #lagging