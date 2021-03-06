from propagator import *
import matplotlib.pyplot as plt
from prop_visualiser import VIS

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

def exp():
    show_hardcoded_examples()
    #points = [Point(13, 15), Point(14, 15)] # for eid=6
    points = [Point(14, 22), Point(13, 22)]
    exemplars = make_propagation(eid=19, points=points)
    print("Result exemplars are " + str(exemplars))
    VIS.close()
    print("No errors occured")

def exp1(): # это если хочется, чтобы визуальный лог сохранился даже не смотря на падение кода..
    try:
        exp()
    except:
        VIS.close()

exp()


