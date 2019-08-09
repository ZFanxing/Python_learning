
#使用Pool的方法更方便，即不需要人为分配几个核，默认使用机器硬件支持的所用核数目
import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    #map的方式，自动分配进程
    pool = mp.Pool(processes=2)#可以设置具体使用几个核，不设置的话默认硬件的所有核
    res = pool.map(job, range(10))
    print(res)

    #async的方式，默认每次只在一个进程里计算，除非设置
    res = pool.apply_async(job, (2,))   #这种方式，只给了一个值，就只使用一个核
    print(res.get())

    multi_res = [pool.apply_async(job, (i,))
                 for i in range(10)]
    print([res.get()
           for res in multi_res])


if __name__ =='__main__':
    multicore()


