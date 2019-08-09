import multiprocessing as mp

value = mp.Value('d', 1)  #第一个参数是数据类型，第二个参数是具体数值
array = mp.Array('i', [1, 2, 3])  #mp的array只能是一维的向量，与numpy不同
