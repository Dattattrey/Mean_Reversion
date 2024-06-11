# Define the start and end dates for the data
start_date = '2021-01-01'
end_date = '2023-02-28'
end_date = '2023-01-01'

# Fetch the data from Yahoo Finance API
df = yf.download(symbol, start=start_date, end=end_date)

# Extract the OHLC data from the DataFrame
df = df[['Open', 'High', 'Low', 'Close']]

# Calculate the mean of the OHLC data
df_mean = df.mean(axis=1)
# Calculate the 30-day moving average of the OHLC data
df_mean = df.rolling(window=30).mean()

# Calculate the difference between the OHLC data and the mean
# Calculate the difference between the OHLC data and the moving average
df_diff = df.subtract(df_mean, axis=0)

# Plot the mean reversion
plt.figure(figsize=(10,5))
plt.plot(df_diff)
plt.axhline(y=0, color='black', linestyle='--')
plt.title(f'Mean Reversion of {symbol} from {start_date} to {end_date}')
plt.title(f'Mean Reversion of {symbol} from {start_date} to {end_date} (30-day Moving Average)')
plt.xlabel('Date')
plt.ylabel('Difference')
plt.savefig('mean_reversion.png', dpi=300)
plt.savefig('mean_reversion_ma.png', dpi=300)

# Show the plot
plt.show()