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
# print(listcrypto)



def get_data(crypto):
    finnhub_client = finnhub.Client(api_key="c7j7g52ad3if6uehd9ng")
    data=finnhub_client.quote(stocks)
    data=data['c']
    return data
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
    update()

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
options=listcrypto
selectcrypto=Select(title='Crypto Pair', value='BINANCE:BTCUSDT',options=options,max_width=180)
selectcrypto.on_change('value',update_intermed_crypto)

# Second Graph
pcrypto1=figure(x_axis_type='datetime', width=500, height=300)
sourcecrypto2=ColumnDataSource(dict(x=[], y=[]))
pcrypto1.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=sourcecrypto2)
pcrypto1.line(x='x', y='y', source= sourcecrypto2)


def update_crypto2():
    new_datacrypto2=dict(x=[datetime.now()],y=[get_data(selectcrypto2.value)])
    sourcecrypto2.stream(new_datacrypto2,rollover=200)
    pcrypto1.title.text='Now Streaming %s Price' % selectcrypto2.value
    # print(select2.value)

# Callback Function
def update_intermed_crypto2(attrname,old,new):
    sourcecrypto2.data=dict(x=[],y=[])
    update_crypto2()

date_pattern=['%Y-%m-%d\n%H:%M:%S']

pcrypto1.xaxis.formatter=DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern,
)
pcrypto1.xaxis.major_label_orientation=radians(60)
pcrypto1.xaxis.axis_label='Date'
pcrypto1.yaxis.axis_label='Price'
selectcrypto2=Select(title='Stocks', value='BINANCE:BNBUSDT',options=options,max_width=180)
selectcrypto2.on_change('value',update_intermed_crypto2)


#Third Graph
pcrypto2=figure(x_axis_type='datetime', width=500, height=300)
sourcecrypto3=ColumnDataSource(dict(x=[], y=[]))
pcrypto2.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=sourcecrypto3)
pcrypto2.line(x='x', y='y', source= sourcecrypto3)


def update_crypto3():
    new_datacrypto3=dict(x=[datetime.now()],y=[get_data(selectcrypto3.value)])
    sourcecrypto3.stream(new_datacrypto3,rollover=200)
    pcrypto2.title.text='Now Streaming %s Price' % selectcrypto3.value
    # print(select3.value)

# Callback Function
def update_intermed_crypto3(attrname,old,new):
    sourcecrypto3.data=dict(x=[],y=[])
    update_crypto3()

date_pattern=['%Y-%m-%d\n%H:%M:%S']

pcrypto2.xaxis.formatter=DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern,
)
pcrypto2.xaxis.major_label_orientation=radians(60)
pcrypto2.xaxis.axis_label='Date'
pcrypto2.yaxis.axis_label='Price'
selectcrypto3=Select(title='Crypto Pair', value='BINANCE:XRPUSDT',options=options,max_width=180)
selectcrypto3.on_change('value',update_intermed_crypto3)


#Fourth Graph
pcrypto3=figure(x_axis_type='datetime', width=500, height=300)
sourcecrypto4=ColumnDataSource(dict(x=[], y=[]))
pcrypto3.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=sourcecrypto4)
pcrypto3.line(x='x', y='y', source= sourcecrypto4)


def update_crypto4():
    new_datacrypto4=dict(x=[datetime.now()],y=[get_data(selectcrypto4.value)])
    sourcecrypto4.stream(new_datacrypto4,rollover=200)
    pcrypto3.title.text='Now Streaming %s Price' % selectcrypto4.value

# Callback Function
def update_intermed_crypto4(attrname,old,new):
    sourcecrypto4.data=dict(x=[],y=[])
    update_crypto4()

date_pattern=['%Y-%m-%d\n%H:%M:%S']

pcrypto3.xaxis.formatter=DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern,
)
pcrypto3.xaxis.major_label_orientation=radians(60)
pcrypto3.xaxis.axis_label='Date'
pcrypto3.yaxis.axis_label='Price'
selectcrypto4=Select(title='Crypto Pair', value='BINANCE:ALICEUSDT',options=options,max_width=180)
selectcrypto4.on_change('value',update_intermed_crypto4)



# Get Nasdaq Stock List
nasdaq=pd.read_csv('nasdaq.csv')
nasdaq=nasdaq['Symbol']
nasdaqlist=[]
for item in nasdaq:
    nasdaqlist.append((item,item))


def get_data(stocks):
    finnhub_client = finnhub.Client(api_key="c7j7g52ad3if6uehd9ng")
    data=finnhub_client.quote(stocks)
    data=data['c']
    return data
# Create Figure
p=figure(x_axis_type='datetime', width=500, height=300)

#Create Data
def create_value():
    data=0
    return data

# Create data source
source=ColumnDataSource(dict(x=[], y=[]))
p.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=source)
p.line(x='x', y='y', source= source)


def update():
    new_data=dict(x=[datetime.now()],y=[get_data(select.value)])
    source.stream(new_data,rollover=200)
    # print(new_data)
    p.title.text='Now Streaming %s Price' % select.value
    # print(select.value)

# Callback Function
def update_intermed(attrname,old,new):
    source.data=dict(x=[],y=[])
    update()

date_pattern=['%Y-%m-%d\n%H:%M:%S']

p.xaxis.formatter=DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern,
)
p.xaxis.major_label_orientation=radians(60)
p.xaxis.axis_label='Date'
p.yaxis.axis_label='Value'

#Create Selection Widget
options=nasdaqlist
select=Select(title='Stocks', value='AAPL',options=options,max_width=100)
select.on_change('value',update_intermed)

# Second Graph
p1=figure(x_axis_type='datetime', width=500, height=300)
source2=ColumnDataSource(dict(x=[], y=[]))
p1.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=source2)
p1.line(x='x', y='y', source= source2)


def update2():
    new_data2=dict(x=[datetime.now()],y=[get_data(select2.value)])
    source2.stream(new_data2,rollover=200)
    p1.title.text='Now Streaming %s Price' % select2.value
    # print(select2.value)

# Callback Function
def update_intermed2(attrname,old,new):
    source2.data=dict(x=[],y=[])
    update2()

date_pattern=['%Y-%m-%d\n%H:%M:%S']

p1.xaxis.formatter=DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern,
)
p1.xaxis.major_label_orientation=radians(60)
p1.xaxis.axis_label='Date'
p1.yaxis.axis_label='Value'
options=nasdaqlist
select2=Select(title='Stocks', value='TSLA',options=options,max_width=100)
select2.on_change('value',update_intermed2)


#Third Graph
p2=figure(x_axis_type='datetime', width=500, height=300)
source3=ColumnDataSource(dict(x=[], y=[]))
p2.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=source3)
p2.line(x='x', y='y', source= source3)


def update3():
    new_data3=dict(x=[datetime.now()],y=[get_data(select3.value)])
    source3.stream(new_data3,rollover=200)
    p2.title.text='Now Streaming %s Price' % select3.value
    # print(select3.value)

# Callback Function
def update_intermed3(attrname,old,new):
    source3.data=dict(x=[],y=[])
    update3()

date_pattern=['%Y-%m-%d\n%H:%M:%S']

p2.xaxis.formatter=DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern,
)
p2.xaxis.major_label_orientation=radians(60)
p2.xaxis.axis_label='Date'
p2.yaxis.axis_label='Value'
options=nasdaqlist
select3=Select(title='Stocks', value='GOOG',options=options,max_width=100)
select3.on_change('value',update_intermed3)


#Fourth Graph
p3=figure(x_axis_type='datetime', width=500, height=300)
source4=ColumnDataSource(dict(x=[], y=[]))
p3.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=source4)
p3.line(x='x', y='y', source= source4)


def update4():
    new_data4=dict(x=[datetime.now()],y=[get_data(select4.value)])
    source4.stream(new_data4,rollover=200)
    p3.title.text='Now Streaming %s Price' % select4.value

# Callback Function
def update_intermed4(attrname,old,new):
    source4.data=dict(x=[],y=[])
    update4()

date_pattern=['%Y-%m-%d\n%H:%M:%S']

p3.xaxis.formatter=DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern,
)
p3.xaxis.major_label_orientation=radians(60)
p3.xaxis.axis_label='Date'
p3.yaxis.axis_label='Value'
options=nasdaqlist
select4=Select(title='Stocks', value='MSFT',options=options,max_width=100)
select4.on_change('value',update_intermed4)




# Config Layout
lay_outcrypto=layout(gridplot([[pcrypto,selectcrypto,pcrypto1,selectcrypto2],[pcrypto2,selectcrypto3,pcrypto3,selectcrypto4]]))

#Because finnhub api is limited we set the update for 5 sec
curdoc().add_periodic_callback(update_crypto,8000)
curdoc().add_periodic_callback(update_crypto2,8000)
curdoc().add_periodic_callback(update_crypto3,8000)
curdoc().add_periodic_callback(update_crypto4,8000)
lay_outstocks=layout(gridplot([[p,select,p1,select2],[p2,select3,p3,select4]]))

#Because finnhub api is limited we set the update for 8 sec
curdoc().add_periodic_callback(update,8000)
curdoc().add_periodic_callback(update2,8000)
curdoc().add_periodic_callback(update3,8000)
curdoc().add_periodic_callback(update4,8000)

#tab 1
tab1=Panel(child=lay_outcrypto,title='Crypto Price')
tab2=Panel(child=lay_outstocks,title='Stocks Price')
tabs=Tabs(tabs=[tab1,tab2])

curdoc().add_root(tabs)