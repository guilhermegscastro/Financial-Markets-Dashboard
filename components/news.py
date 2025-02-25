from app import *
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, callback
import pandas as pd
from dash.dependencies import Input, Output

list_usa_journals = ['CNBC', 'Fortune 500', 'CNN']
list_world_journals = ['Valor Internacional', 'Financial Times', 'China Daily']

layout_usa = [
                    dbc.Row([

                        dbc.Col([

                            html.H1('USA Journals', className='local-news')

                        ]),
                        dbc.Col([]),

                    ]),
                    dbc.Row([

                        dbc.Col([html.Img(id = 'image-journal', style = {'max-width': '50px'})]
                                , style = {'margin-top': '24px'}, md = 1),
                        dbc.Col([html.Div(dcc.Dropdown(list_usa_journals, value = 'CNBC', id = 'choose-journal-usa', className = 'dcc-dafault',
                                                        style = {"background-color": 'black', 'color': 'white', 'margin': '12px 0px 0px 0px'}
                                                                 ), style = {'width': "25%"})], style = {'margin-top': '24px'})

                    ]),
                    dbc.Row([

                        html.H1('Economy', className='class-news')

                    ]),

                    
                    html.Div(id = 'economy-us', style = {'display': 'flex', 'flex-wrap': "wrap", 'gap': '12px'}),

                    
                    dbc.Row([

                        dbc.Col(html.H1('Technology', className='class-news'), md = 4, style = {'margin-left': '-14px'}),
                        dbc.Col(dcc.RadioItems(['AI (Fortune 500)'], id = 'button-special-edition-1'), style={'display': 'flex', 'justify-content': 'left', 'margin-top': "30px"})
                

                    ]),

                    html.Div(id = 'tech-us', style = {'display': 'flex', 'flex-wrap': "wrap", 'gap': '12px'}),
                    
                    ]


layout_world = [
                    dbc.Row([

                        dbc.Col([

                            html.H1('WORLD Journals', className='local-news')

                        ]),
                        dbc.Col([]),

                    ]),
                    dbc.Row([

                        dbc.Col([html.Img(id = 'image-journal-world', style = {'max-width': '50px'})]
                                , style = {'margin-top': '24px'}, md = 2),
                        dbc.Col([html.Div(dcc.Dropdown(list_world_journals, value = 'Valor Internacional', id = 'choose-journal-world', className = 'dcc-dafault',
                                                        style = {"background-color": 'black', 'color': 'white', 'margin': '12px 0px 0px 0px'}
                                                                 ), style = {'width': "25%"})], style = {'margin-top': '24px'})

                    ]),
                    dbc.Row([

                        html.H1('Economy', className='class-news')

                    ]),

                    
                    html.Div(id = 'economy-wd', style = {'display': 'flex', 'flex-wrap': "wrap", 'gap': '12px'}),

                    
                    dbc.Row([

                        dbc.Col(html.H1('Technology', className='class-news'), md = 4, style = {'margin-left': '-14px'}),
                        dbc.Col(dcc.RadioItems(['Deep Dive (Financial Times)'], id = 'button-special-edition-2'), style={'display': 'flex', 'justify-content': 'left', 'margin-top': "30px"})

                    ]),

                    html.Div(id = 'tech-wd', style = {'display': 'flex', 'flex-wrap': "wrap", 'gap': '12px'}),
                    
                    ]

def get_table_news(news, journal, theme):

    if journal == 'China Daily':

        news = news[(news['journal'] == 'china_daily') & (news['title'] == theme)]
        
    elif journal == 'CNBC':

        news = news[(news['journal'] == 'cnbc') & (news['title'] == theme)]

    elif journal == 'Valor Internacional':

        news = news[(news['journal'] == 'valor_internacional') & (news['title'] == theme)]

    elif journal == 'CNN':

        news = news[(news['journal'] == 'cnn') & (news['title'] == theme)]            

    elif journal == 'Financial Times':

        news = news[(news['journal'] == 'ft') & (news['title'] == theme)]

    elif journal == 'Fortune 500':

        news = news[(news['journal'] == 'fortune') & (news['title'] == theme)]

    news = news.fillna("-")

    layout_tabela = [dbc.Row([

                           dbc.Col([
                               
                               html.A(children=[

                                html.P(children=news['subhead'].iloc[0], className='h3-news'),
                                html.H3(children=news['headline'].iloc[0], className='headline')

                            ], href= news['link'].iloc[0], target= "_blank", className= 'links-news'),


                           ], style={'width': '375px'}),
                           dbc.Col([
                               
                               html.A(children=[

                                html.P(children=news['subhead'].iloc[1], className='h3-news'),
                                html.H3(children=news['headline'].iloc[1], className='headline')

                            ], href= news['link'].iloc[1], target= "_blank", className= 'links-news'),

                           ], style={'width': '375px'}),
                          
                           ]),

                    dbc.Row([

                           dbc.Col([
                               
                               html.A(children=[

                                html.P(children=news['subhead'].iloc[2], className='h3-news'),
                                html.H3(children=news['headline'].iloc[2], className='headline')

                            ], href= news['link'].iloc[2], target= "_blank", className= 'links-news'),


                           ], style={'width': '375px'}),
                           dbc.Col([
                               
                               html.A(children=[

                                html.P(children=news['subhead'].iloc[3], className='h3-news'),
                                html.H3(children=news['headline'].iloc[3], className='headline')

                            ], href= news['link'].iloc[3], target= "_blank", className= 'links-news'),

                           ], style={'width': '375px'}),
                          
                           ]),

                    dbc.Row([

                           dbc.Col([
                               
                               html.A(children=[

                                html.P(children=news['subhead'].iloc[4], className='h3-news'),
                                html.H3(children=news['headline'].iloc[4], className='headline')

                            ], href= news['link'].iloc[4], target= "_blank", className= 'links-news'),


                           ], style={'width': '375px'}),
                           dbc.Col([
                               
                               html.A(children=[

                                html.P(children=news['subhead'].iloc[5], className='h3-news'),
                                html.H3(children=news['headline'].iloc[5], className='headline')

                            ], href= news['link'].iloc[5], target= "_blank", className= 'links-news'),

                           ], style={'width': '375px'}),
                          
                           ]),
                        ]

    return layout_tabela

@app.callback(
    Output('image-journal', 'src'),
    Input('choose-journal-usa', 'value')
)
def update_options(journal):

    if journal == 'CNN':

        src = 'assets/cnn.png'

    elif journal == 'CNBC':

        src = 'assets/cnbc.png'

    elif journal == 'Fortune 500':

        src = 'assets/fortune.png'

    return src

@app.callback(
    Output('image-journal-world', 'src'),
    Input('choose-journal-world', 'value')
)
def update_options(journal):

    if journal == 'China Daily':

        src = 'assets/china_daily.png'

    elif journal == 'Financial Times':

        src = 'assets/ft.png'

    elif journal == 'Valor Internacional':

        src = 'assets/valor-economico.png'

    return src


@app.callback(
    Output('economy-us', 'children'),
    Input('choose-journal-usa', 'value')
)
def update_options(journal):

    news = pd.read_csv('csv_files/news.csv')
    news['headline'] = news['headline'].str.strip()

    layout_table = get_table_news(news, journal, 'economy')
    
    return layout_table

@app.callback(
    Output('economy-wd', 'children'),
    Input('choose-journal-world', 'value')
)
def update_options(journal):

    news = pd.read_csv('csv_files/news.csv')
    news['headline'] = news['headline'].str.strip()

    layout_table = get_table_news(news, journal, 'economy')
    
    return layout_table

@app.callback(
    Output('tech-wd', 'children'),
    [Input('choose-journal-world', 'value'),
     Input('button-special-edition-2', 'value')]
)
def update_options(journal, button):

    news = pd.read_csv('csv_files/news.csv')
    news['headline'] = news['headline'].str.strip()

    if button == 'Deep Dive (Financial Times)':

        layout_table = get_table_news(news, journal, 'deep_dive')

    else:

        layout_table = get_table_news(news, journal, 'tech')
    
    return layout_table

@app.callback(
    Output('tech-us', 'children'),
    [Input('choose-journal-usa', 'value'),
     Input('button-special-edition-1', 'value')]
)
def update_options(journal, button):

    news = pd.read_csv('csv_files/news.csv')
    news['headline'] = news['headline'].str.strip()

    if button == 'AI (Fortune 500)':

        layout_table = get_table_news(news, journal, 'ai')

    else:

        layout_table = get_table_news(news, journal, 'tech')
    
    return layout_table













