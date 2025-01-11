import argparse
from Bio import SeqIO
import re

# Taking variables from the terminal
def args_fromTerminal():
    parser = argparse.ArgumentParser()

    parser.add_argument('FILENAME', type=str, default='sequence.fasta', help="filename (default = sequence.fasta)")
    parser.add_argument('--dublicate', help='Search for duplicate sequences', action='store_true')
    parser.add_argument('--GC', help="search for GC", action='store_true')

    args = parser.parse_args()
    return args

# taking sequence from FASTA file
def sequence_fromFASTA(args):
    file_exists = args.FILENAME
    try:
        if file_exists:     
            sequence = SeqIO.read(file_exists, "fasta")
            sequence = str(sequence.seq)
    except:
        exit()
      
    print(sequence)
    return sequence

# search for the longest dublicates in sequences
def longest_dublicate(args, sequence):
    if args.dublicate:
        length = 1
        result = ''

        while True:
            regex = r'([GATC]{' + str(length) + r'}).*\1'
            m = re.search(regex, sequence)
            if m:
                result = m.group(1)
                length +=1
            else:
                break
        print('The longest dublicate:', result)
        print('The length of the longest dublicate:', length-1)

# search for longest sequence containing only G or/and C
def longest_GC(args, sequence):
    if args.GC:
        length = 1
        result = ''

        while True:
            regex = r'([GC]{' + str(length) + r',})'
            m = re.search(regex, sequence)
            if m:
                result = m.group(1)
                length +=1
            else:
                break
        print('The longest GC sequence:', result)
        print('The longest GC sequence length:', length-1)

args = args_fromTerminal()
sequence = sequence_fromFASTA(args)
longest_dublicate(args, sequence)
longest_GC(args, sequence)
