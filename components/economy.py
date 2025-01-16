from app import *
from dash import Dash, html, dcc, dash_table, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from graph_dropdown import graph_ism_pmi, graph_retail_sales, graph_consumer_sentiment, graph_housing_starts, graph_nonfarm_payroll, graph_initial_jobless_claims, graph_personal_income, graph_industry_production_index, graph_capacity_utilization, graph_jolts, graph_cpi, graph_real_gdp, graph_durable_goods_orders, graph_producer_price_index, graph_feds_funds_rate, graph_10_year_treasury_yield, graph_sp500, graph_average_hourly_earnings, graph_commercial_industrial_loans
from table_dropdown import table_ism_pmi, table_retail_sales, table_consumer_sentiment, table_housing_starts, table_nonfarm_payroll, table_initial_jobless_claims, table_personal_income, table_industry_production_index, table_capacity_utilization, table_jolts, table_cpi, table_real_gdp, table_durable_goods_orders, table_producer_price_index, table_feds_funds_rate, table_10_year_treasury_yield, table_sp500, table_average_hourly_earnings, table_commercial_industrial_loans

list_indicators_leading = ['ISM Manufacturing PMI', 'Retail Sales', 'Consumer Sentiment', 'Housing Starts', 'SP500', 'Average Hourly Earnings']
list_indicators_coincident = ['Nonfarm Payroll', 'Initial Jobless Claims', 'Personal Income', 'Industry Production Index', 'Capacity Utilization', 'JOLTS']
list_indicators_lagging = ['CPI', 'Real GDP', 'Durable Goods Orders', 'Producer Price Index', 'Feds Funds Rate', '10 Year Treasury Yield', 'Commercial and Industrial Loans']
list_periods = ['1 year', '3 years', '5 years', '10 years']

layout_leading = [

            dbc.Row([

                dbc.Col([

                    dbc.Row([

                        dbc.Col(html.Div(dcc.Dropdown(list_indicators_leading, value = 'ISM Manufacturing PMI', id = 'indicator-leading-graph', className = 'dcc-default',
                                                                style = {"background-color": 'black', 'color': 'white'}))),
                        dbc.Col(dcc.Dropdown(list_periods, value = '3 years', id = 'indicator-leading-period', className = 'dcc-default',
                                                                style = {"background-color": 'black', 'color': 'white'}))

                    ]),
                    dbc.Row(dcc.Graph(style={"width": "100%", 'height': "302px", 'margin-top': '16px', 'width': '90%', 
                                                             'border-radius':'8px',
                                                             'background-color': '#131516', 'border': "2px solid #212946"}, 
                                                             id ='graph_leading'), style={'display': 'flex', 'justify-content': 'center'})
                ])
            ]),

            dbc.Row([

                html.H3(children="Statistics", className='category-dash', style = {'width': '96%'})

            ], style= {'display': 'flex', 'justify-content': 'center'}),

            dbc.Row([

                html.Div(dcc.Dropdown(list_indicators_leading, value = 'ISM Manufacturing PMI', id = 'indicator-leading-table', className = 'dcc-default',
                                                                style = {"background-color": 'black', 'color': 'white', 'margin-top': "9px"}),         
                                                                style = {"width": "50%"}),

                html.Div(id = 'leading-statistics', style= {'margin-top': "-10px"})
                                
            ], style= {'margin-top': '24px'})

            ]


@app.callback(Output('graph_leading', 'figure'),
              [Input('indicator-leading-graph', 'value'),
               Input('indicator-leading-period', 'value')]) 

def update_metrics(indicator, period):

    if indicator == "ISM Manufacturing PMI":

        fig = graph_ism_pmi(period)

    elif indicator == 'Retail Sales':

        fig = graph_retail_sales(period)

    elif indicator == 'Consumer Sentiment':

        fig = graph_consumer_sentiment(period)

    elif indicator == 'Housing Starts':

        fig = graph_housing_starts(period)

    elif indicator == 'SP500':

        fig = graph_sp500(period)

    elif indicator == 'Average Hourly Earnings':

        fig = graph_average_hourly_earnings(period)
        

    return fig

@app.callback(Output('leading-statistics', 'children'),
              Input('indicator-leading-table', 'value'))

def update_metrics(indicator):

    if indicator == "ISM Manufacturing PMI":

        table = table_ism_pmi()

    elif indicator == 'Retail Sales':

        table = table_retail_sales()

    elif indicator == 'Consumer Sentiment':

        table = table_consumer_sentiment()

    elif indicator == 'Housing Starts':

        table = table_housing_starts()

    elif indicator == 'SP500':

        table = table_sp500()

    elif indicator == 'Average Hourly Earnings':

        table = table_average_hourly_earnings()


    return [dash_table.DataTable(columns=[{"name": i, "id": i} for i in table.columns],
                                 data = table.to_dict('records'),
                                    style_header={'display': 'none'},
                                    style_cell={'textAlign': 'center',
                                                'padding': '12px 8px',
                                                'backgroundColor': '#333E66',
                                                'color': '#D3D6DF'
                                                },

                                    style_data={ 'border': '0px',
                                                'font-size': "12px" },

                                                style_table={
                                                
                                                'borderRadius': '0px',
                                                'overflow': 'hidden'
                                            },
                                    style_data_conditional=[
                                        {
                                            'if': {
                                                'column_id': 'ignore_1',
                                            },
                                            'backgroundColor': '#212946',
                                            'fontWeight': 'bold',
                                            'borderRadius': '0px',
                                            'font-size': "12px",
                                            'color': '#D3D6DF'
                                        }]
                                                                                )]


layout_coincident = [
    
            dbc.Row([

                dbc.Col([

                    dbc.Row([

                        dbc.Col(html.Div(dcc.Dropdown(list_indicators_coincident, value = 'Nonfarm Payroll', id = 'indicator-coincident-graph', className = 'dcc-default',
                                                                style = {"background-color": 'black', 'color': 'white'}))),
                        dbc.Col(dcc.Dropdown(list_periods, value = '3 years', id = 'indicator-coincident-period', className = 'dcc-default',
                                                                style = {"background-color": 'black', 'color': 'white'}))

                    ]),
                    dbc.Row(dcc.Graph(style={"width": "100%", 'height': "302px", 'margin-top': '16px', 'width': '90%', 
                                                             'border-radius':'8px',
                                                             'background-color': '#131516', 'border': "2px solid #212946"}, 
                                                             id ='graph_coincident'), style={'display': 'flex', 'justify-content': 'center'})
                ])
            ]),

            dbc.Row([

                html.H3(children="Statistics", className='category-dash', style = {'width': '96%'})

            ], style= {'display': 'flex', 'justify-content': 'center'}),

            dbc.Row([

                html.Div(dcc.Dropdown(list_indicators_coincident, value = 'Nonfarm Payroll', id = 'indicator-coincident-table', className = 'dcc-default',
                                                                style = {"background-color": 'black', 'color': 'white', 'margin-top': "9px"}),         
                                                                style = {"width": "50%"}),

                html.Div(id = 'coincident-statistics', style= {'margin-top': "-10px"})
                                
            ], style= {'margin-top': '24px'})

            ]

@app.callback(Output('graph_coincident', 'figure'),
              [Input('indicator-coincident-graph', 'value'),
               Input('indicator-coincident-period', 'value')]) 

def update_metrics(indicator, period):

    if indicator == "Nonfarm Payroll":

        fig = graph_nonfarm_payroll(period)

    elif indicator == 'Initial Jobless Claims':

        fig = graph_initial_jobless_claims(period)

    elif indicator == 'Personal Income':

        fig = graph_personal_income(period)

    elif indicator == 'Industry Production Index':

        fig = graph_industry_production_index(period)

    elif indicator == 'Capacity Utilization':

        fig = graph_capacity_utilization(period)

    elif indicator == 'JOLTS':

        fig = graph_jolts(period)
        

    return fig

@app.callback(Output('coincident-statistics', 'children'),
              Input('indicator-coincident-table', 'value'))

def update_metrics(indicator):

    if indicator == "Nonfarm Payroll":

        table = table_nonfarm_payroll()

    elif indicator == 'Initial Jobless Claims':

        table = table_initial_jobless_claims()

    elif indicator == 'Personal Income':

        table = table_personal_income()

    elif indicator == 'Industry Production Index':

        table = table_industry_production_index()
    
    elif indicator == 'Capacity Utilization':

        table = table_capacity_utilization()

    elif indicator == 'JOLTS':

        table = table_jolts()


    return [dash_table.DataTable(columns=[{"name": i, "id": i} for i in table.columns],
                                 data = table.to_dict('records'),
                                    style_header={'display': 'none'},
                                    style_cell={'textAlign': 'center',
                                                'padding': '12px 8px',
                                                'backgroundColor': '#333E66',
                                                'color': '#D3D6DF'
                                                },

                                    style_data={ 'border': '0px',
                                                'font-size': "12px" },

                                                style_table={
                                                
                                                'borderRadius': '0px',
                                                'overflow': 'hidden'
                                            },
                                    style_data_conditional=[
                                        {
                                            'if': {
                                                'column_id': 'ignore_1',
                                            },
                                            'backgroundColor': '#212946',
                                            'fontWeight': 'bold',
                                            'borderRadius': '0px',
                                            'font-size': "12px",
                                            'color': '#D3D6DF'
                                        }]
                                                                                )]


layout_lagging = [
    

            dbc.Row([

                dbc.Col([

                    dbc.Row([

                        dbc.Col(html.Div(dcc.Dropdown(list_indicators_lagging, value = 'CPI', id = 'indicator-lagging-graph', className = 'dcc-default',
                                                                style = {"background-color": 'black', 'color': 'white'}))),
                        dbc.Col(dcc.Dropdown(list_periods, value = '3 years', id = 'indicator-lagging-period', className = 'dcc-default',
                                                                style = {"background-color": 'black', 'color': 'white'}))

                    ]),
                    dbc.Row(dcc.Graph(style={"width": "100%", 'height': "302px", 'margin-top': '16px', 'width': '90%', 
                                                             'border-radius':'8px',
                                                             'background-color': '#131516', 'border': "2px solid #212946"}, 
                                                             id ='graph_lagging'), style={'display': 'flex', 'justify-content': 'center'})
                ])
            ]),

            dbc.Row([

                html.H3(children="Statistics", className='category-dash', style = {'width': '96%'})

            ], style= {'display': 'flex', 'justify-content': 'center'}),

            dbc.Row([

                html.Div(dcc.Dropdown(list_indicators_lagging, value = 'CPI', id = 'indicator-lagging-table', className = 'dcc-default',
                                                                style = {"background-color": 'black', 'color': 'white', 'margin-top': "9px"}),         
                                                                style = {"width": "50%"}),

                html.Div(id = 'lagging-statistics', style= {'margin-top': "-10px"})
                                
            ], style= {'margin-top': '24px'})

            ]

@app.callback(Output('graph_lagging', 'figure'),
              [Input('indicator-lagging-graph', 'value'),
               Input('indicator-lagging-period', 'value')]) 

def update_metrics(indicator, period):

    if indicator == "CPI":

        fig = graph_cpi(period)

    elif indicator == 'Real GDP':

        fig = graph_real_gdp(period)

    elif indicator == 'Durable Goods Orders':

        fig = graph_durable_goods_orders(period)

    elif indicator == 'Producer Price Index':

        fig = graph_producer_price_index(period)

    elif indicator == 'Feds Funds Rate':

        fig = graph_feds_funds_rate(period)

    elif indicator == '10 Year Treasury Yield':

        fig = graph_10_year_treasury_yield(period)

    elif indicator == 'Commercial and Industrial Loans':

        fig = graph_commercial_industrial_loans(period)
        

    return fig

@app.callback(Output('lagging-statistics', 'children'),
              Input('indicator-lagging-table', 'value'))

def update_metrics(indicator):

    if indicator == "CPI":

        table = table_cpi()

    elif indicator == 'Real GDP':    

        table = table_real_gdp()

    elif indicator == 'Durable Goods Orders':

        table = table_durable_goods_orders()

    elif indicator == 'Producer Price Index':

        table = table_producer_price_index()

    elif indicator == 'Feds Funds Rate':

        table = table_feds_funds_rate()

    elif indicator == '10 Year Treasury Yield':
 
        table = table_10_year_treasury_yield()

    elif indicator == 'Commercial and Industrial Loans':
 
        table = table_commercial_industrial_loans()


    return [dash_table.DataTable(columns=[{"name": i, "id": i} for i in table.columns],
                                 data = table.to_dict('records'),
                                    style_header={'display': 'none'},
                                    style_cell={'textAlign': 'center',
                                                'padding': '12px 8px',
                                                'backgroundColor': '#333E66',
                                                'color': '#D3D6DF'
                                                },

                                    style_data={ 'border': '0px',
                                                'font-size': "12px" },

                                                style_table={
                                                
                                                'borderRadius': '0px',
                                                'overflow': 'hidden'
                                            },
                                    style_data_conditional=[
                                        {
                                            'if': {
                                                'column_id': 'ignore_1',
                                            },
                                            'backgroundColor': '#212946',
                                            'fontWeight': 'bold',
                                            'borderRadius': '0px',
                                            'font-size': "12px",
                                            'color': '#D3D6DF'
                                        }]
                                                                                )]




















