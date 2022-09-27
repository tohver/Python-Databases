def findTickerId(ticker):
    tickerIdQuery = f'SELECT id FROM ticker WHERE name = "{ticker}";'
    executeQuery(tickerIdQuery)
    return cursor.fetchall()

def createInsertQuery(ticker_id, record):
    ticker_id = ticker_id
    time = record[0]
    openPrice = record[1]
    high = record[2]
    low = record[3]
    close = record[4]
    volume = record[5]
    return f"INSERT IGNORE INTO price_volume (ticker_id, time, open, high, low, close, volume) VALUES ({ticker_id}, '{time}', {openPrice}, {high}, {low}, {close}, {volume});"


def executeInsertquery(records):
#     counter = 1
    for record in records:
#         if counter%1000000 == 0:
#             print('-', end='')
        query = createInsertQuery(ticker_id, record)
        executeQuery(query)
#         counter +=1
    connection.commit()
