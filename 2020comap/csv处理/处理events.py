import openpyxl
import csv
import json

def work ():
    res=[]
    f = csv.reader(open('fullevents.csv', 'r'))
    for i in f:
        if i[1]=='Huskies':
                res.append({'MatchID':i[0],'OriginPlayerID':i[2],'type':i[6]})
    print(res)
    with open( "../足球场/data/哈士奇比赛事件.txt", "w", encoding="utf-8")as f:
        for each in json.dumps(res):
            f.write(each)
if __name__ == '__main__':
    work()