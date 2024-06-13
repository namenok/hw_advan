import matplotlib.pyplot as plt

x_values = range(-10, 10)
y_values = [(2 * x + 1) for x in x_values]

fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=5)

ax.set_title('Назва графіку', fontsize=24)

ax.set_xlabel('Вісь х')
ax.set_ylabel('Вісь у')

plt.show()
