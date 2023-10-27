
def file_open(name):
    
    with open(name,'r') as input:
        list = [x for x in input]
        return list
    

if __name__ == '__main__':

    file = 'eventi_gauss.txt'

    print(file_open(file))