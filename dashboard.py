from ctypes import sizeof
import requests
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource,DatetimeTickFormatter,Select
from bokeh.layouts import layout
from bokeh.plotting import figure
from datetime import datetime
from math import radians # Rotate axis ticks
import numpy as np
import finnhub
from bokeh.layouts import gridplot,row
import pandas as pd
from bokeh.models.widgets import Tabs, Panel


# Get Crypto List
finnhub_client = finnhub.Client(api_key="c7j7g52ad3if6uehd9ng")
listcrypto=[]
crypto=finnhub_client.crypto_symbols('BINANCE')
for item in crypto:
    listcrypto.append((item['symbol'],item['symbol']))

# Get Nasdaq Stock List
nasdaq=pd.read_csv('nasdaq.csv')
nasdaq=nasdaq['Symbol']
nasdaqlist=[]
for item in nasdaq:
    nasdaqlist.append((item,item))

# Get Data
def get_data(stocks):
        finnhub_client = finnhub.Client(api_key="c7j7g52ad3if6uehd9ng")
        data=finnhub_client.quote(stocks)
        data=data['c']
        return data


# Function to create Crypto Graph
def crypto(x,y):
    # Create Figure
    pcrypto=figure(x_axis_type='datetime', width=500, height=300)

    #Create Data
    def create_value():
        data=0
        return data

    # Create data source
    sourcecrypto=ColumnDataSource(dict(x=[], y=[]))
    pcrypto.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=sourcecrypto)
    pcrypto.line(x='x', y='y', source= sourcecrypto)


    def update_crypto():
        new_datacrypto=dict(x=[datetime.now()],y=[get_data(selectcrypto.value)])
        sourcecrypto.stream(new_datacrypto,rollover=200)
        # print(new_data)
        pcrypto.title.text='Now Streaming %s Price' % selectcrypto.value
        # print(select.value)

    # Callback Function
    def update_intermed_crypto(attrname,old,new):
        sourcecrypto.data=dict(x=[],y=[])
        update_crypto()

    date_pattern=['%Y-%m-%d\n%H:%M:%S']

    pcrypto.xaxis.formatter=DatetimeTickFormatter(
        seconds=date_pattern,
        minsec=date_pattern,
        minutes=date_pattern,
        hourmin=date_pattern,
        hours=date_pattern,
        days=date_pattern,
        months=date_pattern,
        years=date_pattern,
    )
    pcrypto.xaxis.major_label_orientation=radians(60)
    pcrypto.xaxis.axis_label='Date'
    pcrypto.yaxis.axis_label='Price'

    #Create Selection Widget
    options=y
    selectcrypto=Select(title='Crypto Pair', value=x,options=options,max_width=180)
    selectcrypto.on_change('value',update_intermed_crypto)
    return selectcrypto,pcrypto,update_crypto







#Crypto Tab
graph1=crypto('BINANCE:BTCUSDT',listcrypto)
graph2=crypto('BINANCE:XRPUSDT',listcrypto)
graph3=crypto('BINANCE:BNBUSDT',listcrypto)
graph4=crypto('BINANCE:ALICEUSDT',listcrypto)

#Nasdaq Tab
graph5=crypto('AAPL',nasdaqlist)
graph6=crypto('MSFT',nasdaqlist)
graph7=crypto('TSLA',nasdaqlist)
graph8=crypto('DIS',nasdaqlist)


# Config Layout
lay_out_crypto=layout(gridplot([[graph1[1],graph1[0],graph2[1],graph2[0]],[graph3[1],graph3[0],graph4[1],graph4[0]]]))
lay_out_stocks=layout(gridplot([[graph5[1],graph5[0],graph6[1],graph6[0]],[graph7[1],graph7[0],graph8[1],graph8[0]]]))


#Because finnhub api is limited we set the update for 5 sec
curdoc().add_periodic_callback(graph1[2],8000)
curdoc().add_periodic_callback(graph2[2],8000)
curdoc().add_periodic_callback(graph3[2],8000)
curdoc().add_periodic_callback(graph4[2],8000)
curdoc().add_periodic_callback(graph5[2],8000)
curdoc().add_periodic_callback(graph6[2],8000)
curdoc().add_periodic_callback(graph7[2],8000)
curdoc().add_periodic_callback(graph8[2],8000)

#Tab
tab1=Panel(child=lay_out_crypto,title='Crypto Price')
tab2=Panel(child=lay_out_stocks,title='Stocks Price')
tabs=Tabs(tabs=[tab1,tab2])

curdoc().add_root(tabs)
