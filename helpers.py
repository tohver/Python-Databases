import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import mplfinance as mpf



def createMultiIndex(df):
    df.reset_index(inplace = True)
    df.set_index(['day', 'minutes'], inplace = True)
    return df

def plotChart(df, width = 20, height = 9):
    ''' simple plot '''
    plt.figure(figsize = (width, height))
    if type(df) == list:
        for i in df:
            plt.plot(i.index, i.close)
    else:
        plt.plot(df.index, df.close, 'g')
    plt.show()


def dateTime(data):
	data['time'] = pd.to_datetime(data['time'])
	data['day'] = data.time.dt.floor('D')
	data['minutes'] = data.time.dt.time
	data.set_index('time', inplace =True)
	data.head(3)
	return data


def createSessions(data):
	cashSession = data.between_time('9:30', '16:00')
	postMarket = data.between_time('16:00', '19:00')
	preMarket = data.between_time('00:01', '9:30')
	return cashSession, postMarket, preMarket


def selectQuery(stock, datum):
	return f'SELECT * FROM price_volume WHERE ticker_id = (SELECT id FROM ticker WHERE name = "{stock}") AND DATE(time) > "{datum}";'

def convertToFloat(df):
	df.open = df.open.astype(float)
	df.close = df.close.astype(float)
	df.high = df.high.astype(float)
	df.low = df.low.astype(float)
	df.volume = df.volume.astype(float)
	return df
