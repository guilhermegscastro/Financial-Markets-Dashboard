import pandas as pd
import datetime
import plotly.graph_objects as go
import plotly.io as pio

def table_ism_pmi():
    
    data = pd.read_csv('ism_manufacturing_pmi.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Release Date')
    data.index = pd.to_datetime(data.index)
    data = data.sort_index()
    
    data = data.iloc[-13:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"   

    df = pd.DataFrame({"ignore_1": ['Actual', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df


def table_retail_sales():

    data = pd.read_csv('retail_sales.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = '$' + str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"   

    df = pd.DataFrame({"ignore_1": ['Actual (Millions USD)', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df


def table_consumer_sentiment():

    data = pd.read_csv('consumer_sentiment.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"  

    df = pd.DataFrame({"ignore_1": ['Actual', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_housing_starts():

    data = pd.read_csv('housing_starts.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"  

    df = pd.DataFrame({"ignore_1": ['Actual (Thousands of Units)', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_nonfarm_payroll():

    data = pd.read_csv('nonfarm_payroll.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"   

    df = pd.DataFrame({"ignore_1": ['Actual (Thousands of Persons)', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_initial_jobless_claims():

    data = pd.read_csv('initial_jobless_claims.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-53:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-5, 0]) - 1) * 100), 2)) + "%"   

    df = pd.DataFrame({"ignore_1": ['Actual', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_personal_income():

    data = pd.read_csv('personal_income.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = '$' + str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"  

    df = pd.DataFrame({"ignore_1": ['Actual (Billions USD)', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_industry_production_index():

    data = pd.read_csv('industry_production_index.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"  

    df = pd.DataFrame({"ignore_1": ['Actual', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_capacity_utilization():

    data = pd.read_csv('capacity_utilization.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1    
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2)) + "%"
    VAR_12M = str(round(((data.iloc[-1, 0] - data.iloc[1, 0])), 2)) + "%"  
    VAR_YEAR = str(round(((data.iloc[-1, 0] - (data.loc[f'{last_year}']).iloc[-1, 0])), 2)) + "%"   
    VAR_MONTH = str(round(((data.iloc[-1, 0] - data.iloc[-2, 0])), 2)) + "%" 

    df = pd.DataFrame({"ignore_1": ['Actual', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_jolts():

    data = pd.read_csv('jolts.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"   

    df = pd.DataFrame({"ignore_1": ['Actual (Thousands)', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_cpi():

    data = pd.read_csv('cpi.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"   

    df = pd.DataFrame({"ignore_1": ['Actual', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_real_gdp():

    data = pd.read_csv('gdp.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-5:, :]

    ACTUAL = '$' + str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_QUARTER = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"   

    df = pd.DataFrame({"ignore_1": ['Actual (Billions USD)', 'Δ 12M', 'Δ Year', 'Δ Quarter'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_QUARTER]})

    return df

def table_durable_goods_orders():

    data = pd.read_csv('durable_goods_orders.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = '$' + str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%" 

    df = pd.DataFrame({"ignore_1": ['Actual (Millions USD)', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_producer_price_index():

    data = pd.read_csv('producer_price_index.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"  

    df = pd.DataFrame({"ignore_1": ['Actual', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df  

def table_feds_funds_rate():

    data = pd.read_csv('feds_funds_rate.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2)) + "%"
    VAR_12M = str(round(((data.iloc[-1, 0] - data.iloc[1, 0])), 2)) + "%"  
    VAR_YEAR = str(round(((data.iloc[-1, 0] - (data.loc[f'{last_year}']).iloc[-1, 0])), 2)) + "%"   
    VAR_MONTH = str(round(((data.iloc[-1, 0] - data.iloc[-2, 0])), 2)) + "%"  

    df = pd.DataFrame({"ignore_1": ['Actual', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_10_year_treasury_yield():

    data = pd.read_csv('10_year_treasury.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-253:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2)) + "%"
    VAR_12M = str(round(((data.iloc[-1, 0] - data.iloc[1, 0])), 2)) + "%"  
    VAR_YEAR = str(round(((data.iloc[-1, 0] - (data.loc[f'{last_year}']).iloc[-1, 0])), 2)) + "%"   
    VAR_MONTH = str(round(((data.iloc[-1, 0] - data.iloc[-22, 0])), 2)) + "%"   

    df = pd.DataFrame({"ignore_1": ['Actual', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_sp500():

    data = pd.read_csv('sp500.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-253:, :]

    ACTUAL = str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-22, 0]) - 1) * 100), 2)) + "%"  

    df = pd.DataFrame({"ignore_1": ['Actual', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_average_hourly_earnings():

    data = pd.read_csv('average_hourly_earnings.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = '$' + str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"  

    df = pd.DataFrame({"ignore_1": ['Actual', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

def table_commercial_industrial_loans():

    data = pd.read_csv('commercial_industrial_loans.csv')
    today = datetime.datetime.now()
    last_year = today.year - 1
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    
    data = data.iloc[-13:, :]

    ACTUAL = '$' + str(round((data.iloc[-1, 0]), 2))    
    VAR_12M = str(round((((data.iloc[-1, 0]/data.iloc[1, 0]) - 1) * 100), 2)) + "%" 
    VAR_YEAR = str(round((((data.iloc[-1, 0] / data.loc[f'{last_year}'].iloc[-1, 0]) - 1) * 100), 2)) + "%"   
    VAR_MONTH = str(round((((data.iloc[-1, 0]/data.iloc[-2, 0]) - 1) * 100), 2)) + "%"  

    df = pd.DataFrame({"ignore_1": ['Actual (Billions USD)', 'Δ 12M', 'Δ Year', 'Δ Month'], 'ignore_2': [ACTUAL, VAR_12M, VAR_YEAR, VAR_MONTH]})

    return df

