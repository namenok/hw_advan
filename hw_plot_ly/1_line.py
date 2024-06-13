
import plotly.express as px
import pandas as pd

df = pd.DataFrame(dict(
    x=range(-10, 10),
    y=[(3 * x + 2) for x in range(-10, 10)]
))

fig = px.line(df, x="x", y="y", title="Unsorted Input")
fig.show()

df = df.sort_values(by="x")
fig = px.line(df, x="x", y="y", title="Sorted Input")
fig.show()
