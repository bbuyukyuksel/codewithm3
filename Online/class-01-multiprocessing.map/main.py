from multiprocessing import Pool
from itertools import repeat
import numpy as np

def is_factor(args):
    num, factor = args
    return 1 if num % factor == 0 else 0

if __name__ == '__main__':
    num = 20
    
    # Seri 
    #for i in range(1, num+1):
    #    factors[i-1] = is_factor(num, i)
    #print(factors)

    _nums_ = [num for x in range(1,num+1)]
    _iter_ = range(1, num+1)
    #_20s_ = np.ones(num) * num
    print(_nums_)
    print(*_iter_)
    params = tuple(zip(_nums_, _iter_))
    print(params)
    
    # Paralel
    # Alternatif-1
    mypool = Pool(processes=8)
    returns = mypool.map(is_factor, params)
    mypool.close()
    mypool.join()

    # Alternatif-2
    with Pool(processes=8) as p:
        returns = p.map(is_factor, params)
        p.close()
        p.join()
    
    print("Returns:", returns)
    print(returns)
    
    print("Toplam Bölen Sayısı:", sum(returns))
    
    for index, value in enumerate(returns):
        if value == 1:
            print(f"{index+1} sayısı tam bölünmektedir.")
    


