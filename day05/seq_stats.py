import sys
from collections import Counter


def print_out(A, C, G, T, Un, total):
    print(f'A:         {A}   {(A/total)*100:.1f} %')
    print(f'C:         {C}   {(C/total)*100:.1f} %')
    print(f'G:         {G}   {(G/total)*100:.1f} %')
    print(f'T:         {T}   {(T/total)*100:.1f} %')
    print(f'Unknown:   {Un}   {(Un/total)*100:.1f} %')
    print(f'Total:     {total}\n')

def calc_stat(text):
    tot_count = {'A':0, 'C':0, 'G':0, 'T':0, 'Un':0}
    for char in text:
        if char == 'A':
            tot_count['A']+=1
        if char == 'C':
            tot_count['C']+=1
        if char == 'G':
            tot_count['G']+=1
        if char == 'T':
            tot_count['T']+=1
        if char == 'X':
            tot_count['Un']+=1
    return tot_count

def main_func(filenames, print_out, calc_stat):
    result = []
    for i in range(len(filenames)):
            with open(filenames[i], 'r') as fh:
                text = fh.read()
                tot_count = calc_stat(text)
                result.append(tot_count)
            print(f'{filenames[i]}')
            print_out(tot_count['A'], tot_count['C'], tot_count['G'], tot_count['T'], tot_count['Un'], sum(tot_count.values()))
    return result

if __name__=="__main__":

    if len(sys.argv) <2:
        exit(f'Usage: {sys.argv[0]} FILENAME')

    filenames = sys.argv[1:]

    result = main_func(filenames, print_out, calc_stat)    
    sum_results = Counter(result[0])+Counter(result[1])
    print('All')
    print_out(sum_results['A'], sum_results['C'], sum_results['G'], sum_results['T'], sum_results['Un'], sum(sum_results.values()))