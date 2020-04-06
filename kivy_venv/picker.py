import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
canvas = fig.canvas
ax.plot(np.random.rand(100), 'o', picker=5)  # 5 points tolerance

def on_pick(event):
    line = event.artist
    xdata, ydata = line.get_data()
    ind = event.ind
    print('on pick line:', np.array([xdata[ind], ydata[ind]]).T)

cid = fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()