import numpy as np

dates = pd.date_range('20240101', periods=10)
stocks = pd.DataFrame({'Date': dates, 'Price': np.random.rand(10) * 100})
stocks.set_index('Date', inplace=True)
