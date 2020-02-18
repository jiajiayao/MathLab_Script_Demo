import json

with open('res_Huskies.txt',"r") as f:    #设置文件对象
    str = f.read()    #可以是随便对文件的操作
    print(str)
    str=json.loads(str)