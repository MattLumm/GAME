import dash
import dash_core_components as dcc
import dash_html_components as html
import gdax
import plotly
from dash.dependencies import Input, Output, Event
import gdax
import datetime
import pytz
import random
from timezonefinder import TimezoneFinder
import pytz
from pytz import timezone, utc
from pytz.exceptions import UnknownTimeZoneError
import pandas as pd
import plotly
import plotly.graph_objs as go
from collections import deque
import json
mapbox_access_token = "pk.eyJ1IjoiamFja3AiLCJhIjoidGpzN0lXVSJ9.7YK6eRwUNFwd3ODZff6JvA"

# dealing with nan
# https://youtu.be/-NR-ynQg0YM?t=1h5m58s


state_to_code = {
    # # Other
    # 'District of Columbia': 'DC',
    
    # States
    'Alabama': 'AL',
    'Montana': 'MT',
    'Alaska': 'AK',
    'Nebraska': 'NE',
    'Arizona': 'AZ',
    'Nevada': 'NV',
    'Arkansas': 'AR',
    'New Hampshire': 'NH',
    'California': 'CA',
    'New Jersey': 'NJ',
    'Colorado': 'CO',
    'New Mexico': 'NM',
    'Connecticut': 'CT',
    'New York': 'NY',
    'Delaware': 'DE',
    'North Carolina': 'NC',
    'Florida': 'FL',
    'North Dakota': 'ND',
    'Georgia': 'GA',
    'Ohio': 'OH',
    'Hawaii': 'HI',
    'Oklahoma': 'OK',
    'Idaho': 'ID',
    'Oregon': 'OR',
    'Illinois': 'IL',
    'Pennsylvania': 'PA',
    'Indiana': 'IN',
    'Rhode Island': 'RI',
    'Iowa': 'IA',
    'South Carolina': 'SC',
    'Kansas': 'KS',
    'South Dakota': 'SD',
    'Kentucky': 'KY',
    'Tennessee': 'TN',
    'Louisiana': 'LA',
    'Texas': 'TX',
    'Maine': 'ME',
    'Utah': 'UT',
    'Maryland': 'MD',
    'Vermont': 'VT',
    'Massachusetts': 'MA',
    'Virginia': 'VA',
    'Michigan': 'MI',
    'Washington': 'WA',
    'Minnesota': 'MN',
    'West Virginia': 'WV',
    'Mississippi': 'MS',
    'Wisconsin': 'WI',
    'Missouri': 'MO',
    'Wyoming': 'WY',
}

monthes = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August','September','October','November','December']

code_to_state = {v: k for k, v in state_to_code.items()}


df = pd.read_csv('nics-firearm-background-checks.csv')

year_month = []

month_list = ['-01','-02', '-03', '-04', '-05', '-06', '-07','-08','-09','-10','-11','-12' ]

year = '2004'
for i in month_list:
    curr = year + i
    year_month.append(curr)
    # print(curr)

dx = df[(df.month.isin(year_month)) & (df.state == 'Connecticut')]

# reverse df
dx = dx.iloc[::-1]

print(dx['month'])
# for i in range(0,df.shape[0]):

# year_month [:] = []
test = list(range(1,13))

app = dash.Dash()

# creating data
# np.random.seed(42)
# random_x = np.random.randint(1,101,100)
# random_y = np.random.randint(1,101,100)

app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = {'data': [
                        go.Scatter(
                            x=monthes,
                            y=test,
                            mode='markers',
                            marker = {
                                'size' :12,
                                'color': 'rgb(51,204,153)',
                                'line':{'width':1},
                            }
                        )],
                    'layout': go.Layout(title='My Scatterplot',
                                        xaxis= {'title':'Month'})}
                    ),
                    
])


if __name__ == '__main__':
    app.run_server()



#     print( str([df.loc[i, 'month ']]) + ' ' + str([df.loc[i, 'state']]) )
    
    


