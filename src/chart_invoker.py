import datetime as dt
import inquirer as inq
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import pendulum
import plotly.graph_objects as go
import yfinance as yf
from datetime import date, timedelta
import src.helpers.formatter as fmt

fmt.get_my_name()

# build the user choice input choice prompt
choiceList = [
    inq.List('choose',
             message="Choose the option you would like to run:",
             choices=['A) Traditional','B) Charted: Gauge','C) Charted: Bullet', 'D) Charted: Candlestick'],
             ),
]
answers = inq.prompt(choiceList)
print("Choice: ", answers["choose"],"\n")


def run_execution_option(option):
    msg = option
    if option == "A) Traditional":
        do_ticker_hl_lookup()
    elif option == "B) Charted: Gauge":
        do_gauge_chart2()
    elif option == "C) Charted: Bullet":
        do_bullet_chart2()
    elif option == "D) Charted: Candlestick":
        do_candlestick_chart()
    else:
        print("Invalid Choice")


# retrieve the single ticker simple format based on most recent valid weekday
def do_ticker_hl_lookup():
    day_now = fmt.get_most_recent_weekday()
    tomorrow = day_now + timedelta(days=1)
    print("Results for: ", day_now.strftime("%c"))
    data = yf.download("COF", start=day_now, end=tomorrow,group_by="ticker")
    #df_pd = pd.DataFrame(pd)
    df_data = pd.DataFrame(data)
    df_data['Open'].round(decimals = 2)
    df_data['High'].round(decimals = 2)
    print(df_data)


def do_gauge_chart2():
    start = dt.datetime(2019,1,1)
    end = dt.datetime.now()
    stocks = web.DataReader(['COF','FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'],
                            'yahoo', start, end)
    stocks_close = pd.DataFrame(web.DataReader(['COF','FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'],
                                               'yahoo', start, end)['Close'])
    gauge = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        #value = int(stocks_close['COF'].tail(1)),
        value = int(50),
        mode = "gauge+number+delta",
        title = {'text':"<b>Ingress Rule Change Risk</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 'font': {"size": 20}},
        delta = {'reference': int(stocks_close['COF'].tail(2)[0])},
        gauge = {
            'axis': {'range': [None, 100]},
            'steps' : [
                {'range': [0, 75], 'color': "lightgray"},
                {'range': [75, 100], 'color': "gray"}],
            'threshold' : {'line': {'color': "red", 'width': 4},
                           'thickness': 0.75,
                           'value': 90}}))
    gauge.show()


# retrieve the multi-ticker complex format
def do_gauge_chart():
    start = dt.datetime(2019,1,1)
    end = dt.datetime.now()
    stocks = web.DataReader(['COF','FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'],
                            'yahoo', start, end)
    stocks_close = pd.DataFrame(web.DataReader(['COF','FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'],
                                               'yahoo', start, end)['Close'])
    gauge = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = int(stocks_close['COF'].tail(1)),
        mode = "gauge+number+delta",
        title = {'text':"<b>Capital One Day Range</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 'font': {"size": 20}},
        delta = {'reference': int(stocks_close['COF'].tail(2)[0])},
        gauge = {
            'axis': {'range': [None, 300]},
            'steps' : [
                {'range': [0, 200], 'color': "lightgray"},
                {'range': [200, 300], 'color': "gray"}],
            'threshold' : {'line': {'color': "red", 'width': 4},
                           'thickness': 0.75,
                           'value': 276}}))
    gauge.show()
    gauge.write_html(r'/Users/robert.mcroy/dev/projects/python/Ticker/graph.html')


def do_bullet_chart():
    # Customized Bullet chart
    start = dt.datetime(2019,1,1)
    end = dt.datetime.now()
    stocks = web.DataReader(['COF','FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'],
                            'yahoo', start, end)
    stocks_close = pd.DataFrame(web.DataReader(['COF','FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'],
                                               'yahoo', start, end)['Close'])
    c_bullet = go.Figure()

    c_bullet.add_trace(go.Indicator(
        mode = "number+gauge+delta",
        value = int(stocks_close['NFLX'].tail(1)),
        delta = {'reference': int(stocks_close['NFLX'].tail(2)[0])},
        domain = {'x': [0.25, 1],
                  'y': [0.08, 0.25]},
        title = {'text':"<b>NETFLIX DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>",
                 'font': {"size": 14}},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 550]},
            'threshold': {
                'line': {'color': "Red", 'width': 2},
                'thickness': 0.75,
                'value': 505},
            'steps': [
                {'range': [0, 350], 'color': "gray"},
                {'range': [350, 550], 'color': "lightgray"}],
            'bar': {'color': 'black'}}))

    c_bullet.add_trace(go.Indicator(
        mode = "number+gauge+delta",
        value = int(stocks_close['GOOGL'].tail(1)),
        delta = {'reference': int(stocks_close['GOOGL'].tail(2)[0])},
        domain = {'x': [0.25, 1],
                  'y': [0.4, 0.6]},
        title = {'text':"<b>GOOGLE DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>",
                 'font': {"size": 14}},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 1800]},
            'threshold': {
                'line': {'color': "red", 'width': 2},
                'thickness': 0.75,
                'value': 1681},
            'steps': [
                {'range': [0, 1300], 'color': "gray"},
                {'range': [1300, 1800], 'color': "lightgray"}],
            'bar': {'color': 'black'}}))

    c_bullet.add_trace(go.Indicator(
        mode = "number+gauge+delta",
        value = int(stocks_close['MSFT'].tail(1)),
        delta = {'reference': int(stocks_close['MSFT'].tail(2)[0])},
        domain = {'x': [0.25, 1],
                  'y': [0.7, 0.9]},
        title = {'text':"<b>MICROSOFT DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>",
                 'font': {"size": 14}},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 250]},
            'threshold': {
                'line': {'color': "red", 'width': 2},
                'thickness': 0.75,
                'value': 208},
            'steps': [
                {'range': [0, 150], 'color': "gray"},
                {'range': [150, 250], 'color': "lightgray"}],
            'bar': {'color': "black"}}))

    c_bullet.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})
    c_bullet.show()


def do_bullet_chart2():
    # Customized Bullet chart
    percent_value = 20
    base_range = 0
    low_range = 33
    mid_range = 67
    ceiling_range = 100
    percent_delta = 100 - ((percent_value / low_range) * 100)
    print("% Delta: ", percent_delta, "% Value: ", percent_value)

    c_bullet = go.Figure()

    bar_color = fmt.get_threshold_color(percent_value)
    status_clr = fmt.get_status_color(percent_value)
    c_bullet.add_trace(go.Indicator(
        mode = "number+gauge+delta",
        value = int(percent_value),
        delta = {'reference': int(low_range)},
        domain = {'x': [0.25, 1],
                  'y': [0.08, 0.25]},
        title = {'text':"<b>INGRESS<br>RISK SCORE<br><span style='color: status_color; font-size:0.8em'>HIGH</span>",
                 'font': {"size": 14}},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color': 'black', 'width': 2},
                'thickness': 0.75,
                'value': 20},
            'steps': [
                {'range': [base_range, low_range], 'color': "green"},
                {'range': [low_range, mid_range], 'color': "orange"},
                {'range': [mid_range, ceiling_range], 'color': "red"}],
            'bar': {'color': 'black'}}))

    bar_color = fmt.get_threshold_color(80)
    status_clr = fmt.get_status_color(percent_value)
    c_bullet.add_trace(go.Indicator(
        mode = "number+gauge+delta",
        value = int(60),
        delta = {'reference': int(70)},
        domain = {'x': [0.25, 1],
                  'y': [0.4, 0.6]},
        title = {'text':"<b>EGRESS<br>RISK SCORE<br><span style='color: status_color; font-size:0.8em'>LOW</span>",
                 'font': {"size": 14}},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color':'black', 'width': 2},
                'thickness': 0.75,
                'value': 60},
            'steps': [
                {'range': [base_range, low_range], 'color': "green"},
                {'range': [low_range, mid_range], 'color': "orange"},
                {'range': [mid_range, ceiling_range], 'color': "red"}],
            'bar': {'color': 'black'}}))

    mycolor = "purple"
    bar_color = fmt.get_threshold_color(percent_value)
    status_clr = fmt.get_status_color(percent_value)
    c_bullet.add_trace(go.Indicator(
        mode = "number+gauge+delta",
        value = int(80),
        delta = {'reference': int(70)},
        domain = {'x': [0.25, 1],
                  'y': [0.7, 0.9]},
        #title = {'text':"<b>PORT<br>RISK SCORE<br><span style='color: orange; font-size:0.8em'>MEDIUM</span>",
        #         'font': {"size": 14}},
        title = {'text':"<b>PORT<br>RISK SCORE<br><span style='color: mycolor; font-size:0.8em'>MEDIUM</span>",
                 'font': {"size": 14}},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color':'black', 'width': 2},
                'thickness': 0.75,
                'value': 80},
            'steps': [
                {'range': [base_range, low_range], 'color': "green"},
                {'range': [low_range, mid_range], 'color': "orange"},
                {'range': [mid_range, ceiling_range], 'color': "red"}],
            'bar': {'color': 'black'}}))

    c_bullet.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})
    c_bullet.write_html(r'./../bullet.html')
    c_bullet.show()


def do_candlestick_chart():
    # Customized Candlestick
    start = dt.datetime(2019,1,1)
    end = dt.datetime.now()
    stocks = web.DataReader(['COF','FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'],
                            'yahoo', start, end)
    stocks_close = pd.DataFrame(web.DataReader(['COF','FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'],
                                               'yahoo', start, end)['Close'])
    c_candlestick = go.Figure(data = [go.Candlestick(x = stocks.index,
                                                     open = stocks[('Open',    'COF')],
                                                     high = stocks[('High',    'COF')],
                                                     low = stocks[('Low',    'COF')],
                                                     close = stocks[('Close',    'COF')])])

    c_candlestick.update_xaxes(
        title_text = 'Date',
        rangeslider_visible = True,
        rangeselector = dict(
            buttons = list([
                dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
                dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
                dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
                dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
                dict(step = 'all')])))

    c_candlestick.update_layout(
        title = {
            'text': 'Capital One Share Price (2013-2020)',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    c_candlestick.update_yaxes(title_text = 'COF Close Price', tickprefix = '$')
    c_candlestick.show()


def chart_ticker():
    price_history = yf.Ticker('CHEK').history(period='2y', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                              interval='1wk', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                              actions=False)
    time_series = list(price_history['Open'])
    dt_list = [pendulum.parse(str(dt)).float_timestamp for dt in list(price_history.index)]
    plt.style.use('dark_background')
    plt.plot(dt_list, time_series, linewidth=2)


# determine user choice and call applicable method
run_execution_option(answers["choose"])
