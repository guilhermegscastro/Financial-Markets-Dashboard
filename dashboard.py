import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, callback
from components import  economy, news
from app import *

tab_macroeconomics =  html.Div([

    dbc.Row(

        [dbc.Col(html.H2(children = "Leading Indicators", className='subtitle-dash'), md = 4),
         dbc.Col(html.H2(children = "Coincident Indicators", className='subtitle-dash'), md = 4),
        dbc.Col(html.H2(children = "Lagging Indicators", className='subtitle-dash'), md = 4)]
    ),

    dbc.Row(

    [
        dbc.Col(economy.layout_leading, md = 4),
        dbc.Col(economy.layout_coincident, md = 4),
        dbc.Col(economy.layout_lagging, md = 4)
    ]

    ),
])

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

                dbc.Tab(tab_macroeconomics, label = 'Macroeconomics'),
                dbc.Tab(tab_news, label = 'News')

                      ]), style = {'margin': '8px'}
        )
    ), fluid = True, style = {'height': '100vh', 'width': '100%', 'padding': "25px 25px 0px 25px", 'background-color': '#131516'}
)





if __name__ == "__main__":
    app.run_server(debug = True, port = 8051)























