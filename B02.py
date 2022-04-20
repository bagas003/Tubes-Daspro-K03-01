import time

def kerangajaib():

    def lcg():
        m = 2**32; a = 53; c = 69
        x = int(time.time())

        for i in range(10):
            x = (a*x + c) % m
        
        return x % 10
    
    respon = ['gatau','iya kyknya','gk','adadeh','wow','same...','iyh', 'mlz','boring bgt lu','terserah']

    input('\nKerangAjaib: apa?\nLu         : ')
    print('KerangAjaib: '+ respon[lcg()])
