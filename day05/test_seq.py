from seq_stats import calc_stat

def test_seq_1():
    tot_count = calc_stat('ACAGCCTTTT')
    assert tot_count == {'A':2, 'C':3, 'G':1, 'T':4, 'Un':0}


def test_seq_2():
    tot_count = calc_stat('XXXAXXXT')
    assert tot_count == {'A':1, 'C':0, 'G':0, 'T':1, 'Un':6}