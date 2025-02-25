import pandas as pd
import datetime
import plotly.graph_objects as go
import plotly.io as pio

def graph_ism_pmi(years):

    pio.templates.default = "simple_white"
    
    ism_pmi = pd.read_csv('csv_files/ism_manufacturing_pmi.csv')
    ism_pmi = ism_pmi.set_index('Release Date')
    ism_pmi.index = pd.to_datetime(ism_pmi.index)
    ism_pmi = ism_pmi.sort_index()

    if years == '1 year':

        ism_pmi = ism_pmi.iloc[-12:, :]

    elif years == '3 years':

        ism_pmi = ism_pmi.iloc[-36:, :]
    
    elif years == '5 years':

        ism_pmi = ism_pmi.iloc[-60:, :]

    elif years == '10 years':

        ism_pmi = ism_pmi.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".1f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_ism_pmi = go.Figure(data=[
        go.Scatter(name='Actual', x=ism_pmi.index, y=ism_pmi['Actual'], marker_color='firebrick'),
        go.Scatter(name='Forecast', x=ism_pmi.index, y=ism_pmi['Forecast'], marker_color='royalblue')
    ], layout=layout)

    fig_ism_pmi.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )
    fig_ism_pmi.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_ism_pmi.layout.plot_bgcolor = '#131516'
    fig_ism_pmi.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_ism_pmi.update_xaxes(tickcolor = '#131516')
    fig_ism_pmi.update_yaxes(tickcolor = '#131516')

    fig_ism_pmi.add_annotation(
    text="(Index)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)
    
    return fig_ism_pmi

def graph_retail_sales(years):

    pio.templates.default = "simple_white"
    
    retail_sales = pd.read_csv('csv_files/retail_sales.csv')
    retail_sales = retail_sales.set_index('Date')
    retail_sales.index = pd.to_datetime(retail_sales.index)

    if years == '1 year':

        retail_sales = retail_sales.iloc[-12:, :]

    elif years == '3 years':

        retail_sales = retail_sales.iloc[-36:, :]
    
    elif years == '5 years':

        retail_sales = retail_sales.iloc[-60:, :]

    elif years == '10 years':

        retail_sales = retail_sales.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".0f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_retail_sales = go.Figure(data=[
        go.Scatter(name='Ratail Sales', x=retail_sales.index, y=retail_sales['retail_sales'], marker_color='firebrick'),
    ], layout=layout)

    fig_retail_sales.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )
    fig_retail_sales.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_retail_sales.layout.plot_bgcolor = '#131516'
    fig_retail_sales.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_retail_sales.update_xaxes(tickcolor = '#131516')
    fig_retail_sales.update_yaxes(tickcolor = '#131516')

    fig_retail_sales.add_annotation(
    text="(Millions USD / Monthly)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)
    
    return fig_retail_sales

def graph_consumer_sentiment(years):

    pio.templates.default = "simple_white"
    
    consumer_sentiment = pd.read_csv('csv_files/consumer_sentiment.csv')
    consumer_sentiment = consumer_sentiment.set_index('Date')
    consumer_sentiment.index = pd.to_datetime(consumer_sentiment.index)

    if years == '1 year':

        consumer_sentiment = consumer_sentiment.iloc[-12:, :]

    elif years == '3 years':

        consumer_sentiment = consumer_sentiment.iloc[-36:, :]
    
    elif years == '5 years':

        consumer_sentiment = consumer_sentiment.iloc[-60:, :]

    elif years == '10 years':

        consumer_sentiment = consumer_sentiment.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".1f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_consumer_sentiment = go.Figure(data=[
        go.Scatter(name='Consumer Sentiment', x=consumer_sentiment.index, y=consumer_sentiment['consumer_sentiment'], marker_color='firebrick'),
    ], layout=layout)

    fig_consumer_sentiment.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )
    fig_consumer_sentiment.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_consumer_sentiment.layout.plot_bgcolor = '#131516'
    fig_consumer_sentiment.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_consumer_sentiment.update_xaxes(tickcolor = '#131516')
    fig_consumer_sentiment.update_yaxes(tickcolor = '#131516')

    fig_consumer_sentiment.add_annotation(
    text="(Index)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)
    return fig_consumer_sentiment

def graph_housing_starts(years):

    pio.templates.default = "simple_white"
    
    housing_starts = pd.read_csv('csv_files/housing_starts.csv')
    housing_starts = housing_starts.set_index('Date')
    housing_starts.index = pd.to_datetime(housing_starts.index)

    if years == '1 year':

        housing_starts = housing_starts.iloc[-12:, :]

    elif years == '3 years':

        housing_starts = housing_starts.iloc[-36:, :]
    
    elif years == '5 years':

        housing_starts = housing_starts.iloc[-60:, :]

    elif years == '10 years':

        housing_starts = housing_starts.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".0f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_housing_starts = go.Figure(data=[
        go.Scatter(name='Housing Starts', x=housing_starts.index, y=housing_starts['housing_starts'], marker_color='firebrick'),
    ], layout=layout)

    fig_housing_starts.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )
    fig_housing_starts.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_housing_starts.layout.plot_bgcolor = '#131516'
    fig_housing_starts.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_housing_starts.update_xaxes(tickcolor = '#131516')
    fig_housing_starts.update_yaxes(tickcolor = '#131516')

    fig_housing_starts.add_annotation(
    text="(Thousands of Units / Monthly)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_housing_starts

def graph_nonfarm_payroll(years):

    pio.templates.default = "simple_white"
    
    nonfarm_payroll = pd.read_csv('csv_files/nonfarm_payroll.csv')
    nonfarm_payroll = nonfarm_payroll.set_index('Date')
    nonfarm_payroll.index = pd.to_datetime(nonfarm_payroll.index)

    if years == '1 year':

        nonfarm_payroll = nonfarm_payroll.iloc[-12:, :]

    elif years == '3 years':

        nonfarm_payroll = nonfarm_payroll.iloc[-36:, :]
    
    elif years == '5 years':

        nonfarm_payroll = nonfarm_payroll.iloc[-60:, :]

    elif years == '10 years':

        nonfarm_payroll = nonfarm_payroll.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".0f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_nonfarm_payroll = go.Figure(data=[
        go.Scatter(name='Nonfarm Payroll', x=nonfarm_payroll.index, y=nonfarm_payroll['nonfarm_payroll'], marker_color='firebrick'),    
    ], layout=layout)    

    fig_nonfarm_payroll.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )
    fig_nonfarm_payroll.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_nonfarm_payroll.layout.plot_bgcolor = '#131516'
    fig_nonfarm_payroll.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_nonfarm_payroll.update_xaxes(tickcolor = '#131516')
    fig_nonfarm_payroll.update_yaxes(tickcolor = '#131516')

    fig_nonfarm_payroll.add_annotation(
    text="(Thousands of Persons)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_nonfarm_payroll

def graph_initial_jobless_claims(years):

    pio.templates.default = "simple_white"
    
    initial_jobless_claims = pd.read_csv('csv_files/initial_jobless_claims.csv')
    initial_jobless_claims = initial_jobless_claims.set_index('Date')
    initial_jobless_claims.index = pd.to_datetime(initial_jobless_claims.index)

    if years == '1 year':

        initial_jobless_claims = initial_jobless_claims.iloc[-52:, :]

    elif years == '3 years':

        initial_jobless_claims = initial_jobless_claims.iloc[-(52 * 3):, :]   

    elif years == '5 years':

        initial_jobless_claims = initial_jobless_claims.iloc[-(52 * 5):, :]

    elif years == '10 years':       

        initial_jobless_claims = initial_jobless_claims.iloc[-(52 * 10):, :]

    layout = go.Layout(yaxis=dict(tickformat=".0f", tickfont=dict(color="#D3D6DF"), showline = False),  
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_initial_jobless_claims = go.Figure(data=[
        go.Scatter(name='Initial Jobless Claims', x=initial_jobless_claims.index, y=initial_jobless_claims['initial_jobless_claims'], marker_color='firebrick'),
    ], layout=layout)

    fig_initial_jobless_claims.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )
    fig_initial_jobless_claims.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_initial_jobless_claims.layout.plot_bgcolor = '#131516'
    fig_initial_jobless_claims.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_initial_jobless_claims.update_xaxes(tickcolor = '#131516')
    fig_initial_jobless_claims.update_yaxes(tickcolor = '#131516')

    fig_initial_jobless_claims.add_annotation(
    text="(Units / Weekly)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_initial_jobless_claims

def graph_personal_income(years):

    pio.templates.default = "simple_white"
    
    personal_income = pd.read_csv('csv_files/personal_income.csv')
    personal_income = personal_income.set_index('Date')
    personal_income.index = pd.to_datetime(personal_income.index)

    if years == '1 year':

        personal_income = personal_income.iloc[-12:, :]

    elif years == '3 years':

        personal_income = personal_income.iloc[-36:, :]
    
    elif years == '5 years':

        personal_income = personal_income.iloc[-60:, :]

    elif years == '10 years':

        personal_income = personal_income.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".1f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_personal_income = go.Figure(data=[
        go.Scatter(name='Personal Income', x=personal_income.index, y=personal_income['personal_income'], marker_color='firebrick'),
    ], layout=layout)   

    fig_personal_income.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )       

    fig_personal_income.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_personal_income.layout.plot_bgcolor = '#131516'
    fig_personal_income.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_personal_income.update_xaxes(tickcolor = '#131516')
    fig_personal_income.update_yaxes(tickcolor = '#131516')

    fig_personal_income.add_annotation(
    text="(Billions USD / Monthly)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_personal_income

def graph_industry_production_index(years):

    pio.templates.default = "simple_white"
    
    industry_production_index = pd.read_csv('csv_files/industry_production_index.csv')
    industry_production_index = industry_production_index.set_index('Date')
    industry_production_index.index = pd.to_datetime(industry_production_index.index)

    if years == '1 year':

        industry_production_index = industry_production_index.iloc[-12:, :]

    elif years == '3 years':

        industry_production_index = industry_production_index.iloc[-36:, :]
    
    elif years == '5 years':

        industry_production_index = industry_production_index.iloc[-60:, :]

    elif years == '10 years':

        industry_production_index = industry_production_index.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".2f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_industry_production_index = go.Figure(data=[
        go.Scatter(name='Industry Production Index', x=industry_production_index.index, y=industry_production_index['industry_production_index'], marker_color='firebrick'),
    ], layout=layout)

    fig_industry_production_index.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_industry_production_index.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_industry_production_index.layout.plot_bgcolor = '#131516'
    fig_industry_production_index.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_industry_production_index.update_xaxes(tickcolor = '#131516')
    fig_industry_production_index.update_yaxes(tickcolor = '#131516')

    fig_industry_production_index.add_annotation(
    text="(Index)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_industry_production_index

def graph_capacity_utilization(years):

    pio.templates.default = "simple_white"
    
    capacity_utilization = pd.read_csv('csv_files/capacity_utilization.csv')
    capacity_utilization = capacity_utilization.set_index('Date')
    capacity_utilization.index = pd.to_datetime(capacity_utilization.index)

    if years == '1 year':

        capacity_utilization = capacity_utilization.iloc[-12:, :]

    elif years == '3 years':

        capacity_utilization = capacity_utilization.iloc[-36:, :]
    
    elif years == '5 years':

        capacity_utilization = capacity_utilization.iloc[-60:, :]

    elif years == '10 years':

        capacity_utilization = capacity_utilization.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".2f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_capacity_utilization = go.Figure(data=[
        go.Scatter(name='Capacity Utilization', x=capacity_utilization.index, y=capacity_utilization['capacity_utilization'], marker_color='firebrick'),
    ], layout=layout)

    fig_capacity_utilization.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_capacity_utilization.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_capacity_utilization.layout.plot_bgcolor = '#131516'
    fig_capacity_utilization.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_capacity_utilization.update_xaxes(tickcolor = '#131516')
    fig_capacity_utilization.update_yaxes(tickcolor = '#131516')

    fig_capacity_utilization.add_annotation(
    text="(Percent)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_capacity_utilization

def graph_jolts(years):

    pio.templates.default = "simple_white"
    
    jolts = pd.read_csv('csv_files/jolts.csv')
    jolts = jolts.set_index('Date')
    jolts.index = pd.to_datetime(jolts.index)

    if years == '1 year':

        jolts = jolts.iloc[-12:, :]

    elif years == '3 years':

        jolts = jolts.iloc[-36:, :]
    
    elif years == '5 years':

        jolts = jolts.iloc[-60:, :]

    elif years == '10 years':

        jolts = jolts.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".0f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_jolts = go.Figure(data=[
        go.Scatter(name='Jolts', x=jolts.index, y=jolts['jolts'], marker_color='firebrick'),
    ], layout=layout)

    fig_jolts.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_jolts.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_jolts.layout.plot_bgcolor = '#131516'
    fig_jolts.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_jolts.update_xaxes(tickcolor = '#131516')
    fig_jolts.update_yaxes(tickcolor = '#131516')

    fig_jolts.add_annotation(
    text="(Level in Thousands / Monthly)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_jolts

def graph_cpi(years):

    pio.templates.default = "simple_white"
    
    cpi = pd.read_csv('csv_files/cpi.csv')
    cpi = cpi.set_index('Date')
    cpi.index = pd.to_datetime(cpi.index)

    if years == '1 year':

        cpi = cpi.iloc[-12:, :]

    elif years == '3 years':

        cpi = cpi.iloc[-36:, :]
    
    elif years == '5 years':

        cpi = cpi.iloc[-60:, :]

    elif years == '10 years':

        cpi = cpi.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".2f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_cpi = go.Figure(data=[
        go.Scatter(name='CPI', x=cpi.index, y=cpi['cpi'], marker_color='firebrick'),
    ], layout=layout)

    fig_cpi.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,   
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_cpi.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_cpi.layout.plot_bgcolor = '#131516'
    fig_cpi.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_cpi.update_xaxes(tickcolor = '#131516')
    fig_cpi.update_yaxes(tickcolor = '#131516')

    fig_cpi.add_annotation(
    text="(Index)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_cpi

def graph_real_gdp(years):

    pio.templates.default = "simple_white"
    
    gdp = pd.read_csv('csv_files/gdp.csv')
    gdp = gdp.set_index('Date')
    gdp.index = pd.to_datetime(gdp.index)

    if years == '1 year':

        gdp = gdp.iloc[-4:, :]

    elif years == '3 years':

        gdp = gdp.iloc[-12:, :]
    
    elif years == '5 years':

        gdp = gdp.iloc[-20:, :]

    elif years == '10 years':

        gdp = gdp.iloc[-40:, :]

    layout = go.Layout(yaxis=dict(tickformat=".2f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_gdp = go.Figure(data=[
        go.Scatter(name='GDP', x=gdp.index, y=gdp['gdp'], marker_color='firebrick'),
    ], layout=layout)

    fig_gdp.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,   
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_gdp.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_gdp.layout.plot_bgcolor = '#131516'
    fig_gdp.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_gdp.update_xaxes(tickcolor = '#131516')
    fig_gdp.update_yaxes(tickcolor = '#131516')

    fig_gdp.add_annotation(
    text="(Billions USD / Quarterly)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_gdp

def graph_durable_goods_orders(years):

    pio.templates.default = "simple_white"
    
    durable_goods = pd.read_csv('csv_files/durable_goods_orders.csv')
    durable_goods = durable_goods.set_index('Date')
    durable_goods.index = pd.to_datetime(durable_goods.index)

    if years == '1 year':

        durable_goods = durable_goods.iloc[-12:, :]

    elif years == '3 years':

        durable_goods = durable_goods.iloc[-36:, :]
    
    elif years == '5 years':

        durable_goods = durable_goods.iloc[-60:, :]

    elif years == '10 years':

        durable_goods = durable_goods.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".0f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_durable_goods = go.Figure(data=[
        go.Scatter(name='Durable Goods Orders', x=durable_goods.index, y=durable_goods['durable_goods_orders'], marker_color='firebrick'),
    ], layout=layout)

    fig_durable_goods.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,   
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_durable_goods.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_durable_goods.layout.plot_bgcolor = '#131516'
    fig_durable_goods.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_durable_goods.update_xaxes(tickcolor = '#131516')
    fig_durable_goods.update_yaxes(tickcolor = '#131516')

    fig_durable_goods.add_annotation(
    text="(Millions USD / Monthly)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_durable_goods

def graph_producer_price_index(years):

    pio.templates.default = "simple_white"
    
    producer_price_index = pd.read_csv('csv_files/producer_price_index.csv')
    producer_price_index = producer_price_index.set_index('Date')
    producer_price_index.index = pd.to_datetime(producer_price_index.index)

    if years == '1 year':

        producer_price_index = producer_price_index.iloc[-12:, :]

    elif years == '3 years':

        producer_price_index = producer_price_index.iloc[-36:, :]
    
    elif years == '5 years':

        producer_price_index = producer_price_index.iloc[-60:, :]

    elif years == '10 years':

        producer_price_index = producer_price_index.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".0f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_producer_price_index = go.Figure(data=[
        go.Scatter(name='Producer Price Index', x=producer_price_index.index, y=producer_price_index['producer_price_index'], marker_color='firebrick'),
    ], layout=layout)

    fig_producer_price_index.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,   
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_producer_price_index.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_producer_price_index.layout.plot_bgcolor = '#131516'
    fig_producer_price_index.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_producer_price_index.update_xaxes(tickcolor = '#131516')
    fig_producer_price_index.update_yaxes(tickcolor = '#131516')

    fig_producer_price_index.add_annotation(
    text="(Index)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_producer_price_index

def graph_feds_funds_rate(years):

    pio.templates.default = "simple_white"
    
    feds_funds = pd.read_csv('csv_files/feds_funds_rate.csv')
    feds_funds = feds_funds.set_index('Date')
    feds_funds.index = pd.to_datetime(feds_funds.index)

    if years == '1 year':

        feds_funds = feds_funds.iloc[-12:, :]

    elif years == '3 years':

        feds_funds = feds_funds.iloc[-36:, :]
    
    elif years == '5 years':

        feds_funds = feds_funds.iloc[-60:, :]

    elif years == '10 years':

        feds_funds = feds_funds.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".2f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_feds_funds = go.Figure(data=[
        go.Scatter(name='FEDS Funds', x=feds_funds.index, y=feds_funds['feds_funds_rate'], marker_color='firebrick'),
    ], layout=layout)

    fig_feds_funds.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,   
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_feds_funds.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_feds_funds.layout.plot_bgcolor = '#131516'
    fig_feds_funds.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_feds_funds.update_xaxes(tickcolor = '#131516')
    fig_feds_funds.update_yaxes(tickcolor = '#131516')

    fig_feds_funds.add_annotation(
    text="(Percent per Year)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_feds_funds

def graph_10_year_treasury_yield(years):

    pio.templates.default = "simple_white" 

    ten_year_treasury_yield = pd.read_csv('csv_files/10_year_treasury.csv')
    ten_year_treasury_yield = ten_year_treasury_yield.set_index('Date')
    ten_year_treasury_yield.index = pd.to_datetime(ten_year_treasury_yield.index)

    if years == '1 year':

        ten_year_treasury_yield = ten_year_treasury_yield.iloc[-252:, :]

    elif years == '3 years':

        ten_year_treasury_yield = ten_year_treasury_yield.iloc[-(252 * 3):, :]
    
    elif years == '5 years':

        ten_year_treasury_yield = ten_year_treasury_yield.iloc[-(252 * 5):, :]

    elif years == '10 years':

        ten_year_treasury_yield = ten_year_treasury_yield.iloc[-(252 * 10):, :]

    layout = go.Layout(yaxis=dict(tickformat=".2f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_10_year_treasury_yield = go.Figure(data=[
        go.Scatter(name='10 Year Treasury Yield', x=ten_year_treasury_yield.index, y=ten_year_treasury_yield['10_year_treasury'], marker_color='firebrick'),
    ], layout=layout)

    fig_10_year_treasury_yield.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,   
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_10_year_treasury_yield.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_10_year_treasury_yield.layout.plot_bgcolor = '#131516'
    fig_10_year_treasury_yield.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_10_year_treasury_yield.update_xaxes(tickcolor = '#131516')
    fig_10_year_treasury_yield.update_yaxes(tickcolor = '#131516')

    fig_10_year_treasury_yield.add_annotation(
    text="(Percent per Year)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_10_year_treasury_yield

def graph_sp500(years):

    pio.templates.default = "simple_white"
    
    sp500 = pd.read_csv('csv_files/sp500.csv')
    sp500 = sp500.set_index('Date')
    sp500.index = pd.to_datetime(sp500.index)

    if years == '1 year':

        sp500 = sp500.iloc[-252:, :]

    elif years == '3 years':

        sp500 = sp500.iloc[-(252 * 3):, :]
    
    elif years == '5 years':

        sp500 = sp500.iloc[-(252 * 5):, :]

    elif years == '10 years':

        sp500 = sp500.iloc[-(252 * 10):, :]

    layout = go.Layout(yaxis=dict(tickformat=".2f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_sp500 = go.Figure(data=[
        go.Scatter(name='SP500', x=sp500.index, y=sp500['sp500'], marker_color='firebrick'),
    ], layout=layout)

    fig_sp500.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,   
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_sp500.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_sp500.layout.plot_bgcolor = '#131516'
    fig_sp500.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_sp500.update_xaxes(tickcolor = '#131516')
    fig_sp500.update_yaxes(tickcolor = '#131516')

    fig_sp500.add_annotation(
    text="(Index)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_sp500

def graph_average_hourly_earnings(years):

    pio.templates.default = "simple_white"
    
    average_hourly_earnings = pd.read_csv('csv_files/average_hourly_earnings.csv')
    average_hourly_earnings = average_hourly_earnings.set_index('Date')
    average_hourly_earnings.index = pd.to_datetime(average_hourly_earnings.index)

    if years == '1 year':

        average_hourly_earnings = average_hourly_earnings.iloc[-12:, :]

    elif years == '3 years':

        average_hourly_earnings = average_hourly_earnings.iloc[-36:, :]
    
    elif years == '5 years':

        average_hourly_earnings = average_hourly_earnings.iloc[-60:, :]

    elif years == '10 years':

        average_hourly_earnings = average_hourly_earnings.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".2f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_average_hourly_earnings = go.Figure(data=[
        go.Scatter(name='Average Hourly Earnings', x=average_hourly_earnings.index, y=average_hourly_earnings['average_hourly_earnings'], marker_color='firebrick'),
    ], layout=layout)

    fig_average_hourly_earnings.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_average_hourly_earnings.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_average_hourly_earnings.layout.plot_bgcolor = '#131516'
    fig_average_hourly_earnings.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_average_hourly_earnings.update_xaxes(tickcolor = '#131516')
    fig_average_hourly_earnings.update_yaxes(tickcolor = '#131516')

    fig_average_hourly_earnings.add_annotation(
    text="(USD per Hour)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_average_hourly_earnings

def graph_commercial_industrial_loans(years):

    pio.templates.default = "simple_white"
    
    commercial_industrial_loans = pd.read_csv('csv_files/commercial_industrial_loans.csv')
    commercial_industrial_loans = commercial_industrial_loans.set_index('Date')
    commercial_industrial_loans.index = pd.to_datetime(commercial_industrial_loans.index)

    if years == '1 year':

        commercial_industrial_loans = commercial_industrial_loans.iloc[-12:, :]

    elif years == '3 years':

        commercial_industrial_loans = commercial_industrial_loans.iloc[-36:, :]
    
    elif years == '5 years':

        commercial_industrial_loans = commercial_industrial_loans.iloc[-60:, :]

    elif years == '10 years':

        commercial_industrial_loans = commercial_industrial_loans.iloc[-120:, :]

    layout = go.Layout(yaxis=dict(tickformat=".2f", tickfont=dict(color="#D3D6DF"), showline = False),
                        xaxis=dict(tickfont=dict(color="#D3D6DF"), showline = False))

    fig_commercial_industrial_loans = go.Figure(data=[
        go.Scatter(name='Commercial Industrial Loans', x=commercial_industrial_loans.index, y=commercial_industrial_loans['commercial_industrial_loans'], marker_color='firebrick'),
    ], layout=layout)

    fig_commercial_industrial_loans.add_shape( # add a horizontal "target" line
        type="line", line_color="white", line_width=3, opacity=1,
        x0=0, x1=1, xref="paper", y0=0, y1=0, yref="y"
    )

    fig_commercial_industrial_loans.update_layout(font = dict(color = "#D3D6DF"), margin=dict(l=24, r=45, t=31, b=23))
    
    fig_commercial_industrial_loans.layout.plot_bgcolor = '#131516'
    fig_commercial_industrial_loans.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    
    fig_commercial_industrial_loans.update_xaxes(tickcolor = '#131516')
    fig_commercial_industrial_loans.update_yaxes(tickcolor = '#131516')

    fig_commercial_industrial_loans.add_annotation(
    text="(Billions USD)",
    x=0.5,  # Center horizontally (relative to the figure)
    y=0.05,    # Bottom of the figure (relative to the figure)
    xref='paper',  # Use paper coordinates for relative positioning
    yref='paper',
    font=dict(color="#D3D6DF"),
    showarrow=False,
)

    return fig_commercial_industrial_loans