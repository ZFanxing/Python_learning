import  multiprocessing as mp
import time


def job(v, num, l):
    l.acquire()  #锁住
    for _ in range(10):
        time.sleep(0.1)
        v.value += num   #用来获取共享内存，共享内存的形式必须是变量.value的形式，只有变量名不可以
        print(v.value)
    l.release() #释放

def multicore():
    l = mp.Lock()   #定义一个进程锁
    v = mp.Value('i', 1)   #定义共享内存
    p1 = mp.Process(target=job, args=(v, 1, l))  #需要将lock传入
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ =="__main__":
    multicore()

