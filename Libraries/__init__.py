import sys
print('\nStatistical Library by Edi Initialised\n')

path = __file__
lenght = len(path)-12
sys.path.insert(0,path[:lenght])
