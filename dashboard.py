import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, callback
from components import news
from app import *

tab_news =  dbc.Row(

    [
        dbc.Col(news.layout_usa, style= {'margin': '24px 0px 0px 150px'}),
        dbc.Col(news.layout_world, style= {'margin': '24px 0px 0px 0px'})
    ]
)



app.layout = dbc.Container(

    dbc.Row(
        dbc.Col(
            dbc.Tabs([

                dbc.Tab(tab_news, label = 'News')

                      ]), style = {'margin': '8px'}
        )
    ), fluid = True, style = {'height': '100vh', 'width': '100%', 'padding': "25px 25px 0px 25px", 'background-color': '#131516'}
)



if __name__ == "__main__":
    app.run_server(debug = True, port = 8051)























