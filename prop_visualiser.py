from utils.logger import HtmlLogger
from prog_exemplar import ProgExemplar
from globals import globs
from messages import MsgExemplars, MsgUncertainty

import numpy as np
import matplotlib.pyplot as plt

# Для целей отладки алгоритма распространения информации по сети
# хабов написан "визуализатор" этого процесса. Все интересные события
# в ести регистрируются (см. методы def EVENT_...(self, ID,...)) и
# соотвествующие этим событиям картинки с подписями заносятся
# в хтмл-файл. Который сохраняется потом в папку проекта. Его можно
# открыть в любом браузере.
#
# Все логгирование ведется через глобальный объект по имени VIS.


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

    def _draw_uncert_msg(self, uncert_msg, ax):
        strmarker = '$' + str(uncert_msg.eid) + '$'
        for point in uncert_msg.points:
            ax.scatter(point.x, point.y, marker=strmarker, color='skyblue', s=100)

    def _draw_many_prog_examples(self, examples, ax):
        for example in examples:
            color = self._get_random_color()
            self._draw_eids_points(example.events_exemplars, color, ax)

######## EVENTS OF AND HUB #########################################
    def EVENT_and_hub_run(self, ID, siganture_name, left_pre_exemplars, right_pre_exemplars, exemplars):
        self.logger.add_text("AND-hub RUNNED: " +str(ID) + " , signature: " + str(siganture_name))
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
        self._draw_uncert_msg(msg,axs)
        self.logger.add_fig(fig)

    def EVENT_and_hub_received_exemplars_msg(self, ID, from_left_child, msg):
        source = "from left"
        if from_left_child is False:
            source = "from right"
        self.logger.add_text("AND-hub obtained exemplars msg: " + str(ID) + ", " + source)
        pic = globs.pic
        fig, axs = plt.subplots(ncols=1, figsize=(6, 6), dpi=80)
        axs.imshow(pic, cmap='gray_r')
        self._draw_many_prog_examples(msg.exemplars, axs)
        self.logger.add_fig(fig)

    def EVENT_and_hub_failed(self, ID):
        self.logger.add_text("AND-hub failed: " + str(ID))

######## EVENTS OF I HUB #########################################
    def EVENT_i_hub_run(self, ID, uncertainty_msg, exemplars_msg):
        self.logger.add_text("I-hub RUNNED: " +str(ID))
        pic = globs.pic
        fig, axs = plt.subplots(ncols=2,figsize=(18, 12), dpi=80)
        axs[0].imshow(pic, cmap='gray_r')
        axs[0].set_title('incoming uncertainty:')
        self._draw_uncert_msg(uncertainty_msg, axs[0])

        axs[1].imshow(pic, cmap='gray_r')
        axs[1].set_title('outcoming exemplars:')
        self._draw_many_prog_examples(exemplars_msg.exemplars, axs[1])

        self.logger.add_fig(fig)

    ######## EVENTS OF RW HUB #########################################
    def EVENT_rw_hub_failed(self, ID):
        self.logger.add_text("RW-hub " + str(ID) + " failed...")

    def EVENT_rw_hub_sent_uncertainty_to_child(self, ID, uncert_msg):
        self.logger.add_text("RW-hub "+str(ID)+" sent msg to child:")
        pic = globs.pic
        fig, axs = plt.subplots(ncols=1, figsize=(6, 6), dpi=80)
        axs.imshow(pic, cmap='gray_r')
        axs.set_title('uncert to child of rw:')
        self._draw_uncert_msg(uncert_msg, axs)
        self.logger.add_fig(fig)

    def EVENT_rw_hub_obtained_exemplars_from_child(self, ID, exemplars_msg):
        self.logger.add_text("RW-hub " + str(ID) + " obtained exemplars from child:")
        pic = globs.pic
        fig, axs = plt.subplots(ncols=1, figsize=(6, 6), dpi=80)
        axs.imshow(pic, cmap='gray_r')
        axs.set_title('exemplars from child to rw:')
        self._draw_many_prog_examples(exemplars_msg.exemplars, axs)
        self.logger.add_fig(fig)


    ######## EVENTS OF OR HUB #########################################
    def EVENT_or_hub_removes_alternative(self, ID, alternative_to_remove):
        self.logger.add_text("OR-hub " + str(ID) + " removes alterantive " + str(alternative_to_remove))

    def EVENT_or_hub_failed(self, ID):
        self.logger.add_text("OR-hub " + str(ID) + " failed...")

    def EVENT_or_hub_runned(self, ID, exemplars_before, exemplars_after):
        self.logger.add_text("OR-hub " + str(ID) + " runned:")
        pic = globs.pic
        fig, axs = plt.subplots(ncols=2, figsize=(18, 12), dpi=80)
        axs[0].imshow(pic, cmap='gray_r')
        axs[0].set_title('incoming exemplars from child:')
        self._draw_many_prog_examples(exemplars_before, axs[0])

        axs[1].imshow(pic, cmap='gray_r')
        axs[1].set_title('outcoming exemplars (after OR) to its parent:')
        self._draw_many_prog_examples(exemplars_after, axs[1])

        self.logger.add_fig(fig)

    ######## OTHER EVENTS  ############################################
    def EVENT_attached_new_hub(self, ID, parent_ID, hub_type_str):
        self.logger.add_text(str(parent_ID) + "--->" + str(ID) + " ["+ str(hub_type_str)+"]")

VIS = PropVisualiser()

