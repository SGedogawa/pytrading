import logging
import sys
from threading import Thread

import settings
from app.controllers.streamdate import stream
from app.controllers.webserver import start
from app.models.dfcandle import DataFrameCandle

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == "__main__":
    # api_client = APIClient(settings.access_token, settings.account_id)

    '''
    order = Order(
        side="BUY",
        units=100,
        product_code=settings.product_code,
    )

    api_client.send_order(order)
    '''

    '''
    trades = api_client.get_open_trade()
    for t in trades:
        api_client.trade_close(t.trade_id)
    '''

    '''streamThread = Thread(target=stream.stream_ingestion_data)
    streamThread.start()
    streamThread.join()
    '''

    '''
    df = DataFrameCandle(settings.product_code, settings.trade_duration)
    df.set_all_candles(settings.past_period)
    print(df.value)
    '''

    serverThread = Thread(target=start)
    serverThread.start()
    serverThread.join()
