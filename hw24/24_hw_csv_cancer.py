import csv
import matplotlib.pyplot as plt


FILE_NAME = 'cancer.csv'

with open(FILE_NAME, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    rad, tex = [], []
    for row in reader:
        rad.append(row[3])
        tex.append(row[2])

fig, ax = plt.subplots()
ax.plot(rad)
ax.plot(tex)

plt.title('Радіус та текстура', fontsize=24)

plt.show()


