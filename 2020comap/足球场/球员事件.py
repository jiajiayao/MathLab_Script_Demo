import matplotlib.pyplot as plt
import numpy as np
import json


def work(pep_index,N,title,MatchID):


    x = np.arange(N)  # 即array([0,1,2...N])

    # 随机生成N个0到100之间的整数

    # 随机生成几种颜色，reshape第二个参数-1指随着N变化，第一维度填满有剩就来填第二维
    # 生成的是随机的N组三通道(r,g,b)的颜色
    colors = np.random.rand(N * 3).reshape(N, -1)

 #   labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    labels=[]
    num=[]
    for i in pep_index:
        #print(i)
        labels.append(i)
        num.append(pep_index[i])

    plt.title('No.'+MatchID+'_'+title)  # 设置窗格标题
    plt.barh(x, num, alpha=0.8, color=colors, tick_label=labels)
    plt.savefig('resualt/event/'+'No.'+MatchID+'_'+title+".png", format="PNG", bbox_inches='tight')
    plt.show()
if __name__ == '__main__':
    with open('data/' + '哈士奇比赛事件.txt', "r") as f:  # 设置文件对象
        events = f.read()  # 可以是随便对文件的操作
        events = json.loads(events)
    MatchID=''
    event='Shot' #Free Kick  Duel Pass
    OriginPlayerID='Huskies_M1'
    #work(1)
    data=[]
    events_index={}
    pep_index={}
    for i in events:
        if i['MatchID']!=MatchID:
            data.append(i)
            events_index[i['type']]=0
            pep_index[i['OriginPlayerID']]=0
    events_index=list(events_index.keys())
    print(events_index)
    #print(events_index[0])
    for i in data:
        if i['type']==event:
            pep_index[i['OriginPlayerID']]=pep_index[i['OriginPlayerID']]+1
    #print(pep_index)
    work(pep_index,len(pep_index),event,MatchID)


