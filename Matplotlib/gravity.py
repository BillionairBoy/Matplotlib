import matplotlib.pyplot as plt
import numpy as np

gravity = 9.81

def drop():
    velocity = 0
    start_height = 100
    height = start_height
    time = 0
    displacment = 0
    xpoints = []
    ypoints = []
    while height > 0:
        print(time)
        print(height)
        displacment =(0.5 * gravity * (time**2))
        height = start_height - displacment

        xpoints.append(time)
        ypoints.append(displacment)
        time += 0.1
    xpoints = np.array(xpoints)
    ypoints = np.array(ypoints)

    plt.plot(xpoints, ypoints)
    plt.show()


drop()