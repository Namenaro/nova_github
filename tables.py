from signature_or import *
from signature_i import *
from signature_and import *

import torchvision.datasets as datasets
import matplotlib.pyplot as plt
import pandas as pd
import ast
import itertools

class LongTermMemory:
    def __init__(self):
        self.eid_tab = None
        self.and_prog_tab = None
        self.i_prog_tab = None
        self.or_prog_tab = None

        self.load_tables_from_file(path='./tables.xlsx')


    def load_tables_from_file(self, path='./tables.xlsx'):
        print ("loading tables from " + path)
        self.eid_tab = pd.read_excel(path, sheet_name='ids_table',  engine='openpyxl')
        self.and_prog_tab = pd.read_excel(path, sheet_name='u_progs_table',  engine='openpyxl')
        self.i_prog_tab = pd.read_excel(path, sheet_name='i_progs_table', engine='openpyxl')
        self.or_prog_tab = pd.read_excel(path, sheet_name='or_progs_table', engine='openpyxl')

    def get_program_signature_by_eid(self, eid):
        # получим имя программы-источника этого события
        eid_rows = self.eid_tab.loc[self.eid_tab['id_name'] == eid]
        if len(eid_rows) != 1:
            return None
        source_program_name = eid_rows["source"][0]

        # загрузим сигнатуру этой программы
        if source_program_name[0]=='a':
            rows = self.and_prog_tab.loc[self.eid_tab['pr_name'] == source_program_name]
            pre_eid_left = ["id_starter"][0]
            pre_eid_right =["target_id"][0]
            u =rows["u"][0]
            dy = u[1]
            dx = u[0]
            dactions = rows["area"][0]
            mapper1 =rows["map1"][0]
            map1 = {}
            for old_new in mapper1:
                old = old_new[0]
                new = old_new[1]
                map1[new]=old
            mapper2 =rows["map2"][0]
            map2 = {}
            for old_new in mapper2:
                old = old_new[0]
                new = old_new[1]
                map2[new] = old
            signature = AndSignature(source_program_name, pre_eid_left, pre_eid_right, dx, dy, dactions, map1, map2)
            return signature
        if source_program_name[0]=='i':
            rows = self.i_prog_tab.loc[self.eid_tab['pr_name'] == source_program_name]
            old_eid = None
            new_eid = 1
            steps = []
            signature = ISignature(source_program_name, old_eid,new_eid, steps)
            return signature

        if source_program_name[0] == 'o':
            rows = self.and_prog_tab.loc[self.or_prog_tab['pr_name'] == source_program_name]
            ors_list = rows["OR"][0]
            alternatives_list = []

            num_alternatives = len(ors_list[0]-1)
            for i in range(num_alternatives):
                alternative = {}
                for or_node in ors_list:
                    alternative[or_node[0]] = or_node[0][i+1]
                alternatives_list.append(alternative)

            signature = ORSignature(source_program_name, alternatives_list)
            return signature
        assert False, "Err: bad name for the program encountered!"


def convert(cell):
    res = ast.literal_eval(cell)
    return res

if __name__ == "__main__":
    ltm = LongTermMemory()
    ltm.get_program_signature_by_eid(2)