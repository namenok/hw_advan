import csv
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline

FILE_NAME = 'world_fires_7_day.csv'

with open(FILE_NAME, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    lons, lats = [], []

    for row in reader:
        lons.append(row[1])
        lats.append(row[0])

    print(lons, lats)

layout = Layout(title='графік пожеж')

data = [
    {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
        }
    }
]

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='pract_fires.html')



