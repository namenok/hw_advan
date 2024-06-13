import plotly.express as px
import numpy as np

mu, sigma = 0, 0.1
dat = np.random.normal(mu, sigma, 1000)

df = px.data.tips()
fig = px.histogram(df, x="total_bill")
fig.show()