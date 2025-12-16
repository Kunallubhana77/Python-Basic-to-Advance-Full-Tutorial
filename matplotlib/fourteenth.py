import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np

# 14. Time Series Plot
base = datetime.today()
dates = [base - timedelta(days=x) for x in range(30)]
dates.sort() # Sort dates to be in chronological order
values = np.random.randint(10, 50, size=30)

plt.figure(figsize=(12, 6))
plt.plot(dates, values, marker='o', linestyle='-')

# Formatting Date Axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.gcf().autofmt_xdate() # Rotate date labels

plt.title("Time Series Data")
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid(True)
plt.show()
