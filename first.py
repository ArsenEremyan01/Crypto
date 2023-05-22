import pandas as pd

cols = ['open_time', 'close']
eth_data = pd.read_csv('ETHUSDT-15m-2023-05-20.csv', usecols=cols)
btc_data = pd.read_csv('BTCUSDT-15m-2023-05-20.csv', usecols=cols)

merged_data = pd.merge(eth_data, btc_data, on='open_time', suffixes=('_eth', '_btc'))

# Нахождение кореляции
window_size = 5
merged_data['cor'] = merged_data['close_eth'].rolling(window_size, min_periods=window_size).corr(
    merged_data['close_btc'])

# Исключение коррелированных случаев
correlation_threshold = 0.5
filtered_data = merged_data[abs(merged_data['cor']) < correlation_threshold]

print(filtered_data.to_csv('filtered_data'))

"""Использован метод кореляции, потому что он показывает зависимость одной монеты от другой.
   Были взяты тестовые исторические данные 15 минутных свечей за 20 мая."""
