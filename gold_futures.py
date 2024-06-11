# Extract the OHLC data from the DataFrame
df = df[['Open', 'High', 'Low', 'Close']]

# Calculate the 30-day moving average of the OHLC data
df_mean = df.rolling(window=30).mean()
# Calculate the 30-day and 90-day moving averages of the OHLC data
df_mean_30 = df.rolling(window=30).mean()
df_mean_90 = df.rolling(window=90).mean()

# Calculate the difference between the OHLC data and the moving average
df_diff = df.subtract(df_mean, axis=0)
# Calculate the difference between the OHLC data and the moving averages
df_diff_30 = df.subtract(df_mean_30, axis=0)
df_diff_90 = df.subtract(df_mean_90, axis=0)

# Plot the mean reversion
plt.figure(figsize=(10,5))
plt.plot(df_diff)
plt.axhline(y=0, color='black', linestyle='--')
plt.title(f'Mean Reversion of {symbol} from {start_date} to {end_date} (30-day Moving Average)')
plt.xlabel('Date')
plt.ylabel('Difference')
fig, ax = plt.subplots(figsize=(10,5))

# Plot the OHLC data
ax.plot(df.index, df['Close'], label='Close', color='black')
ax.fill_between(df.index, df['Low'], df['High'], alpha=0.2, label='Range', color='grey')

# Plot the moving averages
ax.plot(df_mean_30.index, df_mean_30['Close'], label='30-day Moving Average', color='blue')
ax.plot(df_mean_90.index, df_mean_90['Close'], label='90-day Moving Average', color='green')

# Plot the differences between the OHLC data and the moving averages
ax.plot(df_diff_30.index, df_diff_30['Close'], label='Difference (30-day)', color='red')
ax.plot(df_diff_90.index, df_diff_90['Close'], label='Difference (90-day)', color='orange')

# Add a horizontal line at y=0
ax.axhline(y=0, color='black', linestyle='--')

# Add a title, axis labels, and legend
ax.set_title(f'Mean Reversion of {symbol} from {start_date} to {end_date} (30-day and 90-day Moving Averages)')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend(loc='best')

# Save the plot to a file
plt.savefig('mean_reversion_ma.png', dpi=300)

# Show the plot