import matplotlib as mpl
import matplotlib.pyplot as plt
import random
# 创建图像
fig = plt.figure(figsize=(10,1))
# 模型参数设置
numofcell = 20     # 道路长度
numofcar = 12      # 空间中的车辆数
max_time = 100     # 设置最大时间步
max_speed = 5      # 允许的车辆最大速度
p_slowdown = 0.3   # 随机慢化概率
pause_time = 0.1   # 刷新时间（每一帧持续的时间）
cell_size = 15     # 元胞的大小

# 函数：构建一维空间
def Plot_Space():
    for i in range(1, numofcell): plt.plot([i-0.5, i-0.5], [-0.5, 0.5], '-k', linewidth = 0.5)
    plt.axis([-0.5, numofcell-0.5, -0.5, 0.5])
    plt.xticks([]);plt.yticks([])

# 函数：获取和前车的距离
def get_empty_front(link, numofcell, indexofcell):
    link2 = link * 2   # 周期性边界
    num = 0; i = 1
    while (link2[indexofcell + i]) == None:
        num += 1; i += 1
    return num

if __name__ == '__main__':
    # 随机生成初始元胞
    Plot_Space()
    link = [None] * numofcell
    num = 0
    while num != numofcar:
        sj = random.randint(0, numofcell - 1)
        if link[sj] == None:
            link[sj] = random.randint(0, 5)
            num += 1

    # NaSch模型
    for t in range(0, max_time):
        for cell in range(0, numofcell):
            if link[cell] != None:
                # 加速
                link[cell] = min(link[cell] + 1, max_speed)
                # 减速
                link[cell] = min(link[cell], get_empty_front(link, numofcell, cell))
                # 随机慢化
                if random.random() <= p_slowdown:
                    link[cell] = max(link[cell] - 1, 0)
        # 位置更新
        nlink = [None] * numofcell
        for cell in range(0, numofcell):
            if link[cell] != None:
                new_index = cell + link[cell]
                if new_index >= numofcell:
                    new_index -= numofcell
                nlink[new_index] = link[cell]
        link = nlink
        x1 = []
        for i in range(0, len(link)):
            if link[i] != None:
                x1.append(i)
        Plot_Space()
        plt.plot(x1, [0] * numofcar, 'sk', markersize=cell_size)
        plt.xlabel('timestep:' + str(t))

        plt.pause(pause_time)
        plt.cla()

