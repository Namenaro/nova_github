from globals import *
from utils.get_pictures import *
from tables import *
from propagate import *

import matplotlib.pyplot as plt

def show_hardcoded_examples():
    x = get_numbers_of_type(3)
    img = x[0]
    implot = plt.imshow(img, cmap='gray_r')
    plt.scatter([15, 17], [13, 12], c="red")
    plt.scatter([19, 20], [11, 9], c="blue")
    plt.scatter([14, 16, 18], [22, 20, 18], c="green")
    plt.scatter([14, 17], [21, 18], c="yellow")
    plt.show()

    reds = [img[13][15], img[12][17]]
    blues = [img[11][19], img[9][20]]

    greens = [img[22][14], img[20][16], img[18][18]]
    yellows = [img[21][14], img[18][17]]


PIC = get_numbers_of_type(3)[0]
ltm = LongTermMemory()
points = [Point(4,5), Point(4,6)]
exemplars = make_propagation(eid=4, points = points)
print (exemplars)


