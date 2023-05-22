import time
from binance.client import Client

api_key = '#######'
api_secret = '######'

client = Client(api_key, api_secret)

# начальное значение цены и времени
initial_price = None
start_time = time.time()

# порог изменения цены в процентах
price_change_threshold = 1.0

while True:
    try:
        ticker = client.get_symbol_ticker(symbol='ETHUSDT')
        current_price = float(ticker['price'])

        if initial_price is None:
            initial_price = current_price

        # процент изменения цены
        price_change_percent = (current_price - initial_price) / initial_price * 100

        # если процент изменения цены превышает порог то вывести сообщение
        if abs(price_change_percent) >= price_change_threshold:
            print(f"Цена изменилась на: {price_change_percent:.2f}%")

        # Подождите 1 минуту перед следующим запросом
        time.sleep(60)
    # в случае ошибки подождать 10 секунд и попробовать снова
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(10)
