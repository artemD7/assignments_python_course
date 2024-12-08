import pytest
import seq_stats_4 


text = ('ATTGC')
tot_count = {'A':0, 'C':0, 'G':0, 'T':0, 'Un':0}

def seq_stats_test(text, tot_count):
   tot_count = seq_stats_4.calc_stat(text, tot_count)
   assert tot_count == {'A':1, 'C':1, 'G':1, 'T':2, 'Un':0}

