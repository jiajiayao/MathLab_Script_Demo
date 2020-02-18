import openpyxl
import csv
import json

def word(time):
    ##参数
    machId=str(time)
    teamId='Huskies'

    f = csv.reader(open('passingevents.csv','r'))
    type={}
    #获取index
    for i in f:
        if i[0] == machId:#比赛场数
            if str(i[1])==teamId:
                type[i[2]]=0
                type[i[3]]=0
    f = csv.reader(open('passingevents.csv','r'))
    link=[]

    for t in f:
        if t[0] == machId:  # 比赛场数
            if str(t[1]) == teamId:
                type[t[2]]=type[t[2]]+1
                type[t[3]] = type[t[3]] + 1
                link.append({'source':t[2],'target':t[3]})

    print(json.dumps(type))
    data=[]
    for i in type.keys():
        data.append({"name":i,"num":type[i]})
    print(json.dumps(data))

    with open( '../足球场/data/'+"edge_"+teamId+"_"+machId+".txt", "w", encoding="utf-8")as f:
        for each in json.dumps(link):
            f.write(each)

    with open( '../足球场/data/'+"nodes_"+teamId+"_"+machId+".txt", "w", encoding="utf-8")as f:
         for each in json.dumps(data):
           f.write(each)

if __name__ == '__main__':
    for i in range(1,39):
        word(i)









