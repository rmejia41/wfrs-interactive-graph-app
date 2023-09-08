import dash
from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly
import pandas as pd

df = pd.read_csv('https://github.com/rmejia41/open_datasets/raw/main/wfrs_app_yearly_scatter.csv')
# Save the minimum and maximum values of the gdp column: xmin, xmax
xmin, xmax = min(df.pop_cws), max(df.pop_cws)
# Save the minimum and maximum values of the co2 column: ymin, ymax
ymin, ymax = min(df.pop_fl_water), max(df.pop_fl_water)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])  # BOOTSTRAP
server=app.server
# ---------------------------------------------------------------
# App layout
app.layout = html.Div([
    html.Br(),
    html.H2('WFRS Surveillance Dashboard', style={'textAlign': 'center'}),
    html.H3('Division of Oral Health, Centers for Disease Control', style={'textAlign': 'center'}),
    html.Br(),
    html.H3('Interactive Graph', style={'textAlign': 'left'}),
    html.Br(),
    dcc.Graph(figure=px.scatter(df, x="pop_cws", y="pop_fl_water", animation_frame="year", animation_group="state",
                                color="region",
                                labels={
                                    "pop_cws": "CWS Population",
                                    "pop_fl_water": "Fluoridated Water Population",
                                    "region": "Region",
                                    "state": "State"
                                },
                                hover_name="state", facet_col="region", width=1000, height=400,
                                log_x=True, size_max=45, range_x=[xmin, xmax], range_y=[ymin, ymax])),

    dbc.Tab([
        html.Ul([
            html.Br(),
            html.Li(['Source: Fluoridation Statistics ',
                     html.A('https://www.cdc.gov/fluoridation/statistics/reference_stats.htm',
                            href='https://www.cdc.gov/fluoridation/statistics/reference_stats.htm')])
        ]),
    ]),
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8071)