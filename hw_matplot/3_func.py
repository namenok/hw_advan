import numpy as np
import matplotlib.pyplot as plt


x_sin = np.arange(0, 2*np.pi, 0.1)
y_sin = np.sin(x_sin)


x_cos = np.arange(0, 2 * np.pi, 0.1)
y_cos = np.cos(x_cos)


fig, ax = plt.subplots(2)
ax[0].plot(x_sin, y_sin, color='green')
ax[1].plot(x_cos, y_cos, color='red')


ax[0].set_title('Графік синус', fontsize=14)
ax[0].set_xlabel('Вісь х')
ax[0].set_ylabel('Вісь у')

ax[1].set_title('Графік косинус', fontsize=14)
ax[1].set_xlabel('Вісь х')
ax[1].set_ylabel('Вісь у')

plt.show()





