
import multiprocessing as mp   #创建多进程
import threading as td         #创建线程
import time                    #计算各种方法的时间，方便对比
#创建多核、多线程的任务
def job(q):
    res = 0
    for i in range(10000000):
        res += i + i**2 + i**3
    q.put(res)

#指普通不使用多核情况，因为对比是双核，这里需要计算量加倍，加入了两次for循环
def normal():
    res = 0
    for _ in range(2):
        for i in range(10000000):
            res += i + i ** 2 + i ** 3
    print('normal', res)
    #q.put(res)

#多进程运算即多核运算，这里两个进程
def multcore():
    q = mp.Queue()  #创建队列，#使用队列Queue的概念，将每个进程或者线程的结果记录下来，方便之后的计算，
                    # 原因是多线程中每个线程的任务是没有返回值的
    p1 = mp.Process(target=job, args=(q,))  # 创建多进程，所有多参数加载在args里,要把q当作一个传入值
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:', res1 + res2)

def multithread():
    q = mp.Queue()
    t1 = mp.Process(target=job, args=(q,))  # 创建多线程，所有多参数加载在args里,要把q当作一个传入值
    t2 = mp.Process(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)



if __name__ == '__main__':
   st = time.time()
   normal()
   st1=time.time()
   print('normal time:', st1 - st)
   multithread()
   st2 = time.time()
   print('multithread time:', st2 - st1)
   multcore()
   st3 = time.time()
   print('multicore time:', st3 - st2)

