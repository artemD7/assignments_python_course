import sys

if len(sys.argv) <2:
    exit(f'Usage: {sys.argv[0]} FILENAME')

filenames = sys.argv[1:]
tot_count = {'A':0, 'C':0, 'G':0, 'T':0, 'Un':0}
def print_out(A, C, G, T, Un, total):
    print(f'A:         {A}   {(A/total)*100:.1f} %')
    print(f'C:         {C}   {(C/total)*100:.1f} %')
    print(f'G:         {G}   {(G/total)*100:.1f} %')
    print(f'T:         {T}   {(T/total)*100:.1f} %')
    print(f'Unknown:   {Un}   {(Un/total)*100:.1f} %')
    print(f'Total:     {total}\n')

def calc_stat(text, tot_count):
    
    A = 0
    C = 0
    G = 0
    T = 0
    Un = 0
    total = len(text)-1
    for char in text:
        if char == 'A':
            A +=1
            tot_count['A']+=1
        if char == 'C':
            C +=1
            tot_count['C']+=1
        if char == 'G':
            G +=1
            tot_count['G']+=1
        if char == 'T':
            T +=1
            tot_count['T']+=1
        if char == 'X':
            Un +=1
            tot_count['Un']+=1
    return A,C,G,T,Un,total

for i in range(len(filenames)):
        with open(filenames[i], 'r') as fh:
            text = fh.read()
            A, C, G, T, Un, total = calc_stat(text, tot_count)
        print(f'{filenames[i]}')
        print_out(A, C, G, T, Un, total)    
print('All')
print_out(tot_count['A'], tot_count['C'], tot_count['G'], tot_count['T'], tot_count['Un'], sum(tot_count.values()))

