import os
import time

import psutil

print("Welcome! Current system is " + os.name + ", start to get system info data three seconds later...")
time.sleep(1)
print("Welcome! Current system is " + os.name + ", start to get system info data three two later...")
time.sleep(1)
print("Welcome! Current system is " + os.name + ", start to get system info data three one later...")
# os.system("cls")
time.sleep(1)
print()


# function of Get CPU State;
def get_cpu_state(interval=1):
    """
    获取cpu信息
    :param interval:阻塞时间，单位为秒
    :return: cpu使用率，已转换为str类型
    """
    return str(psutil.cpu_percent(interval))


# function of Get Memory
def get_memory_state():
    """
    获取内存信息
    :return: 返回内存使用率，已用内存，总共内存的元组
    """
    phymem = psutil.virtual_memory()
    return phymem.percent, int(phymem.used), int(phymem.total)


# function of get data to loop
def get_data_loop(interval=1):
    """
    获取cpu和网络信息，需要阻塞，所以设置一段时间间隔，再获取cpu，内存，网络信息
    :param interval: 阻塞时间，单位为秒
    :return:
    """
    before = psutil.net_io_counters()
    cpu_state = get_cpu_state(interval)
    memory_state = get_memory_state()
    after = psutil.net_io_counters()

    return cpu_state, memory_state, after.bytes_sent, after.bytes_recv, after.bytes_sent - before.bytes_sent, after.bytes_recv - before.bytes_recv


def bytes2human(n):
    """
    将字节数进行单位转换，如
    bytes2human(10000)='9.8 K'
    bytes2human(100001221)='95.4 M'
    :param n:
    :return:
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return "{:.2f} {}".format(value, s)
    return "{:.2f} B".format(n)


def update_output(cpu_state, memory_state, now_sent, now_recv, sent_rate, recv_rate, init_sent, init_recv):
    """
    显示最新的数据
    :param cpu_state: CPU使用率
    :param memory_state: 元组（内存使用率，已用内存，总内存）
    :param now_sent: 已经发送的数据量，从开机开始算
    :param now_recv: 已经接收的数据量，从开机开始算
    :param sent_rate: 当前，或者说前一秒的发送速率
    :param recv_rate: 当前，或者说前一秒的接收速率
    :param init_sent: 程序启动时候已经发送的数据量，从开机开始算
    :param init_recv: 程序启动时候已经接收的数据量，从开机开始算
    :return:
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("Time: " + time.asctime())
    print("CPU 使用率: " + cpu_state + "%")
    print("内存使用率: " + str(memory_state[0]) + "%, " + bytes2human(memory_state[1]) + "/" + bytes2human(memory_state[2]))
    print("网络状况: " + "已发送数据" + bytes2human(now_sent - init_sent)
          + ", 已接收数据" + bytes2human(now_recv - init_recv)
          + ", 发送速率" + bytes2human(sent_rate) + "/s, 接收速率"
          + bytes2human(recv_rate) + "/s")
    print()


if __name__ == "__main__":
    try:
        interval = 0
        init_network_state = psutil.net_io_counters()
        init_sent = init_network_state.bytes_sent
        init_recv = init_network_state.bytes_recv
        while True:
            args = get_data_loop(interval)
            update_output(*args, init_sent, init_recv)
            interval = 1
    except KeyboardInterrupt or SystemExit:
        pass
