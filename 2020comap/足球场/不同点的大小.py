import sys, networkx as nx, matplotlib.pyplot as plt
import json
def work(time,name):
    ##参数
    machId=str(time)
    teamId='Huskies'

    with open('data/'+"nodes_"+teamId+"_"+machId+".txt","r") as f:    #设置文件对象
        nodes = f.read()    #可以是随便对文件的操作
        nodes=json.loads(nodes)

    # Create a list of 10 nodes numbered [0, 9]

    node_sizes = []
    labels = {}
    node_color=[]
    for n in nodes:
            node_sizes.append(n['num']*4)
            labels[n['name']] = n['name'][-2:] #节点名称
            node_color.append(n['num'])


    with open('data/'+"edge_"+teamId+"_"+machId+".txt","r") as f:    #设置文件对象
        edge = f.read()    #可以是随便对文件的操作
        edge=json.loads(edge)
    # Connect each node to its successor
    #edges = [ (i, i+1) for i in range(len(nodes)-1) ]
    edges=[]
    for n in edge:
            edges.append([n['source'], n['target']])

    # Create the graph and draw it with the node labels
    g = nx.DiGraph()
    #g.add_nodes_from(nodes)
    g.add_edges_from(edges)

    plt.figure(figsize=[10, 10])
    pos = nx.kamada_kawai_layout(g, weight=None)  # positions for all nodes
    #pos=nx.spring_layout(g)
    nx.draw(g,pos,node_size = node_sizes, node_color=node_color, labels=labels, with_labels=True,font_size=15,edge_color='lightblue',font_color='white')

    _str=name['MatchID']+'_'+name['Outcome']+'_'+name['scroe']+'_'+name['Side']
    plt.title(teamId+'_'+_str)
    plt.savefig('resualt/'+teamId+'/'+name['Outcome']+machId+".png", format="PNG", bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    with open('data/'+'哈士奇比赛结果.txt',"r") as f:    #设置文件对象
        names = f.read()    #可以是随便对文件的操作
        names=json.loads(names)
    for i in range(0,1):
        work(i,names[i])