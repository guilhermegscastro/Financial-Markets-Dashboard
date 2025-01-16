from data_news import scraping_news
from data_fred import get_consumer_sentiment, get_durable_goods_orders, get_feds_funds_rate, get_gdp, get_housing_starts, get_industry_production_index, get_initial_jobless_claims, get_jolts, get_personal_income, get_producer_price_index, get_retail_sales, get_sp500, get_cpi, get_nonfarm_payroll, get_capacity_utilization, get_10_year_treasury, get_average_hourly_earnings, get_commercial_industrial_loans 
from data_ism_pmi import webscraping_ism_pmi
import time

while True:

    def atualizar_rotinas():

        webscraping_ism_pmi()
        get_cpi() 
        get_nonfarm_payroll() 
        get_initial_jobless_claims() 
        get_retail_sales() 
        get_consumer_sentiment() 
        get_personal_income() 
        get_gdp() 
        get_industry_production_index() 
        get_capacity_utilization() 
        get_durable_goods_orders() 
        get_housing_starts() 
        get_producer_price_index() 
        get_feds_funds_rate() 
        get_10_year_treasury() 
        get_jolts() 
        get_sp500() 
        get_average_hourly_earnings() 
        get_commercial_industrial_loans() 
        scraping_news()

    atualizar_rotinas()

    time.sleep(86400)