start_date = '2021-01-01'
end_date = '2023-01-01'

# Define the trading signal parameters (assuming a simple strategy with fixed thresholds)
buy_threshold = -2  # buy when the difference between price and moving average is below this value
sell_threshold = 2  # sell when the difference between price and moving average is above this value
stop_loss = 0.05    # stop loss percentage to limit downside risk

# Define the function to generate the trading signal
def generate_signal(df):
    # Calculate the 30-day and 90-day moving averages of the OHLC data
    df_mean_30 = df['Close'].rolling(window=30).mean()
    df_mean_90 = df['Close'].rolling(window=90).mean()

    # Calculate the difference between the OHLC data and the moving averages
    df_diff_30 = df['Close'] - df_mean_30
    df_diff_90 = df['Close'] - df_mean_90

    # Initialize the signal column to hold the trading signals
    df.loc[:, 'Signal'] = 0

    # Generate the trading signals based on the mean reversion strategy
    for i in range(1, len(df)):
        if df_diff_30[i] < buy_threshold and df_diff_90[i] < buy_threshold:
            df.at[df.index[i], 'Signal'] = 1  # buy signal
        elif df_diff_30[i] > sell_threshold and df_diff_90[i] > sell_threshold:
            df.at[df.index[i], 'Signal'] = -1  # sell signal

        # Apply the stop loss rule
        if df.at[df.index[i], 'Signal'] == 1:
            if df['Close'][i] < (1 - stop_loss) * df['Close'][df.index[i-1]]:
                df.at[df.index[i], 'Signal'] = 0  # stop loss triggered

    return df

# Fetch the data from Yahoo Finance API
df = yf.download(symbol, start=start_date, end=end_date)

# Extract the OHLC data from the DataFrame
df = df[['Open', 'High', 'Low', 'Close']]

# Calculate the 30-day and 90-day moving averages of the OHLC data
df_mean_30 = df.rolling(window=30).mean()
df_mean_90 = df.rolling(window=90).mean()

# Calculate the difference between the OHLC data and the moving averages
df_diff_30 = df.subtract(df_mean_30, axis=0)
df_diff_90 = df.subtract(df_mean_90, axis=0)
# Generate the trading signal based on the mean reversion strategy
df = generate_signal(df)

# Plot the mean reversion
# Plot the mean reversion and trading signals
fig, ax = plt.subplots(figsize=(10,5))

# Plot the OHLC data
ax.plot(df.index, df['Close'], label='Close', color='black')
ax.fill_between(df.index, df['Low'], df['High'], alpha=0.2, label='Range', color='grey')

# Plot the moving averages
ax.plot(df_mean_30.index, df_mean_30['Close'], label='30-day Moving Average', color='blue')
ax.plot(df_mean_90.index, df_mean_90['Close'], label='90-day Moving Average', color='green')
df_mean_30 = df['Close'].rolling(window=30).mean()
df_mean_90 = df['Close'].rolling(window=90).mean()
ax.plot(df_mean_30.index, df_mean_30, label='30-day Moving Average', color='blue')
ax.plot(df_mean_90.index, df_mean_90, label='90-day Moving Average', color='green')

# Plot the differences between the OHLC data and the moving averages
ax.plot(df_diff_30.index, df_diff_30['Close'], label='Difference (30-day)', color='red')
ax.plot(df_diff_90.index, df_diff_90['Close'], label='Difference (90-day)', color='orange')
# Plot the trading signals
ax.plot(df[df['Signal'] == 1].index, df[df['Signal'] == 1]['Close'], marker='^', markersize=10, color='green', label='Buy')
ax.plot(df[df['Signal'] == -1].index, df[df['Signal'] == -1]['Close'], marker='v', markersize=10, color='red', label='Sell')

# Add a horizontal line at y=0
ax.axhline(y=0, color='black', linestyle='--')

# Add a title, axis labels, and legend
ax.set_title(f'Mean Reversion of {symbol} from {start_date} to {end_date} (30-day and 90-day Moving Averages)')
# Add plot labels and legend
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend(loc='best')
ax.set_title(f'{symbol} Mean Reversion Trading Strategy')
ax.legend()

# Save the plot to a file
plt.savefig('mean_reversion_ma.png', dpi=300)
fig.savefig('trading_signal.svg', format='svg', dpi=1200)

# Show the plot
# Display the plot
plt.show()

# Save the DataFrame to a CSV file
df.to_csv('gold_futures_OLHC.csv', index=True)