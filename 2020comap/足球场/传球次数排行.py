import matplotlib.pyplot as plt
import numpy as np
import json

def work(data,N):
    x = np.arange(N)  # 即array([0,1,2...N])

    # 随机生成N个0到100之间的整数

    # 随机生成几种颜色，reshape第二个参数-1指随着N变化，第一维度填满有剩就来填第二维
    # 生成的是随机的N组三通道(r,g,b)的颜色
    colors = np.random.rand(N * 3).reshape(N, -1)

    #labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    labels = []
    num = []
    #print(data)
    for i in data:
        labels.append(i['name'])
        num.append(i['num']/100)
    plt.title('All player xT')  # 设置窗格标题
    plt.barh(x, num, alpha=0.8, color=colors, tick_label=labels)
    plt.savefig('resualt/event/' + "All player xT.png", format="PNG", bbox_inches='tight')
    plt.show()
if __name__ == '__main__':
    with open('data/'+"nodes_Huskies_0.txt","r") as f:    #设置文件对象
        data= f.read()    #可以是随便对文件的操作
        data=json.loads(data)
    work(data,len(data))