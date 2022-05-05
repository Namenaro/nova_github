import numpy as np
import torchvision.datasets as datasets
import matplotlib.pyplot as plt
import pandas as pd
import ast
import itertools


class LongTermMemory:
    def __init__(self):
        self.ids_tab = None
        self.u_prog_tab = None
        self.i_prog_tab = None
        self.or_prog_tab = None

        self.load_tables_from_file(path='./tables.xlsx')


    def load_tables_from_file(self, path='./tables.xlsx'):
        self.ids_tab = pd.read_excel(path, sheet_name='ids_table')
        self.u_prog_tab = pd.read_excel(path, sheet_name='u_progs_table')
        self.i_prog_tab = pd.read_excel(path, sheet_name='i_progs_table')
        self.or_prog_tab = pd.read_excel(path, sheet_name='or_progs_table')

    def get_program_signature_by_eid(self, eid):
        # получим имя программы-источника этого события
        program_name =

        # извлечем всю информацию об этой программы в объект сигнатуры
        # поиск будем производить по имени программы по трем таблицам
        u_progs_res = self.u_progs.loc[self.u_prog_tab['pr_name'] == program_name]



        return signature


def convert(cell):
    res = ast.literal_eval(cell)
    return res

