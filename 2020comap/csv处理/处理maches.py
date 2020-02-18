import openpyxl
import csv
import json

def work ():
    res=[]
    f = csv.reader(open('matches.csv', 'r'))
    for i in f:
        if i[0]!='MatchID':
            res.append({'MatchID':i[0],'Outcome':i[2],'scroe':i[3]+':'+i[4],'Side':i[5]})
    print(res)
    with open( "../足球场/data/哈士奇比赛结果.txt", "w", encoding="utf-8")as f:
        for each in json.dumps(res):
            f.write(each)
if __name__ == '__main__':
    work()