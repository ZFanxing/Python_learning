import threading
import time

def thread_job():
    #print('this is a added Thread,number is %s', threading.current_thread())
    print('T1 start \n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def T2_job():
    print('T2 start\n')
    print('T2 finish\n')

def main():

    add_thread = threading.Thread(target=thread_job,name='T1')
    thread2 = threading.Thread(target=T2_job,name='T2')
    add_thread.start()
    thread2.start()
    thread2.join()
    add_thread.join()
    print('all down')

    # print(threading.active_count())   #目前有多少个激活里的线程
    # print(threading.enumerate())      #输出激活的线程的名字
    # print(threading.current_thread())   #输出当前运行的线程名字

if __name__ =="__main__":
    main()