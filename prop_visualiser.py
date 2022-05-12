from utils.logger import HtmlLogger

import numpy as np
import matplotlib.pyplot as plt

class PropVisualiser:
    def __init__(self):
        self.file_name = 'test'
        self.logger = HtmlLogger(self.file_name)

    def close(self):
        self.logger.close()
        print("visual log of propagation is saved to file: " + self.file_name + ".html")

    def _draw_eids_points(self, eids_points, color, ax):
        for eid, point in eids_points.items():
            strmarker = '$' + str(eid) + '$'
            ax.scatter(point.x, point.y, s=100, c=[color], marker=strmarker, alpha=0.9)

    def _before_after(self, pic, eids_points_before, eids_points_after):
        fig, axs = plt.subplots(ncols=2)
        axs[0].imshow(pic, cmap='gray_r')
        axs[0].set_title('before')
        axs[0].imshow(pic, cmap='gray_r')
        self._draw_eids_points(eids_points_before, 'skyblue', axs[0])

        axs[1].imshow(pic, cmap='gray_r')
        axs[1].set_title('after')
        axs[1].imshow(pic, cmap='gray_r')
        self._draw_eids_points(eids_points_after, 'red', axs[1])
        return fig


pr_vis = PropVisualiser()

