import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--radius',help='radius in units', required =True, type=int)
arg = parser.parse_args()
r = arg.radius
pi = 3.14
print(f'The area of the circle is {pi*r**2:.1f}')
print(f'The circumference of the circle is {2*pi*r:.1f}')