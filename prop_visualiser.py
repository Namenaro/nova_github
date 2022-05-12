from utils.logger import HtmlLogger
from prog_exemplar import ProgExemplar
from globals import globs
from messages import MsgExemplars, MsgUncertainty

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

    def _get_random_color(self):
        color = np.random.rand(3,)
        return color

    def _draw_many_prog_examples(self, examples, ax):
        for example in examples:
            color = self._get_random_color()
            self._draw_eids_points(example.events_exemplars, color, ax)

    def EVENT_and_hub_run(self, ID, left_pre_exemplars, right_pre_exemplars, exemplars):
        self.logger.add_text("AND-hub RUNNED: " +str(ID))
        pic = globs.pic
        fig, axs = plt.subplots(ncols=3,figsize=(18, 6), dpi=80)
        axs[0].imshow(pic, cmap='gray_r')
        axs[0].set_title('left pre_exemplars:')
        self._draw_many_prog_examples(left_pre_exemplars, axs[0])

        axs[1].imshow(pic, cmap='gray_r')
        axs[1].set_title('right pre_exemplars:')
        self._draw_many_prog_examples(right_pre_exemplars, axs[1])

        axs[2].imshow(pic, cmap='gray_r')
        axs[2].set_title('survived exemplars:')
        self._draw_many_prog_examples(exemplars, axs[2])

        self.logger.add_fig(fig)

    def EVENT_and_hub_received_incertainty_msg(self, ID, msg):
        self.logger.add_text("AND-hub obtained uncert msg: " + str(ID))
        pic = globs.pic
        fig, axs = plt.subplots(ncols=1, figsize=(6, 6), dpi=80)
        axs.imshow(pic, cmap='gray_r')
        axs.set_title('uncert:')
        strmarker = '$' + str(msg.eid) + '$'
        for point in msg.points:
            axs.scatter(point.x, point.y, marker=strmarker, color='skyblue',s=100)
        self.logger.add_fig(fig)

VIS = PropVisualiser()

