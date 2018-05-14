#coding=utf-8
#  Matplotlib Tutorial 1 following from :
# https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

# ------------------ 1. Introduction and Line：介绍和画线 ------------------

# import matplotlib.pyplot as plt
#
# plt.plot([1,2,3],[5,7,4])
#
# plt.show()


# ------------------ 2. Legends titles and labels：标题和标签 ------------------

# import matplotlib.pyplot as plt
#
# x = [1,2,3]
# y = [5,7,4]
#
# x2 = [1,2,3]
# y2 = [10,14,12]
#
# plt.plot(x,y,label='First Line')    #添加标签,用于分辨两条线
# plt.plot(x2,y2,label='Second Line')
#
# plt.xlabel('plot number')
# plt.ylabel('Importtant var')
# plt.title('Interesting Graph\ncheck it out')
# plt.legend()    # 当我们有多个 axes时，用legend把图例放在一起
# plt.show()


# ------------------ 3. bar charts and histograms：柱状图和直方图 ------------------

# import matplotlib.pyplot as plt
#
# # ----- bar -----
# x = [2,4,6,8,10]
# y = [5,7,4,4,1]
#
# x2 = [1,3,5,7,9]
# y2 = [1,4,7,3,9]
#
# plt.bar(x,y,label='Bars1',color='r')    # 添加颜色标签
# plt.bar(x2,y2,label='Bars2')      # 将所有数据以柱状图显示
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\ncheck it out')    # 加 '\n' 用于分割
# plt.legend()    # 当我们有多个 axes时，用legend把图例放在一起
# plt.show()

# # ----- histograms -----
# population_ages = [20,12,21,43,54,23,30,25,56,34,12,54,34,29,18,25,
#                    18,64,23,67,45,23,45,67,87,23,45,34,54,23,30,25,56,]
#
# # ids = [x for x in range(len(population_ages))]
# # plt.bar(ids, population_ages)
#
# bins = [0,10,20,30,40,50,60,70,80,90]
#
# plt.hist(population_ages,bins,histtype='bar')   # 使用直方图可以统计分布情况
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\ncheck it out')
# plt.legend()    # 当我们有多个 axes时，用legend把图例放在一起
# plt.show()


# ------------------ 4. Scatter Plots:散点图 ------------------

# import matplotlib.pyplot as plt
#
# x = [1,4,6,9,6,4,5,2,8]
# y = [9,7,5,3,3,5,8,4,2]
#
# # plt.plot(x,y,label='First Line',color='g', linewidth=1)    # 点线图
# plt.scatter(x,y, label='skitscat', color='r',marker='*',s=50)
#                                   #用marker表示散点图样式,s表示尺寸
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\ncheck it out')    # 加 '\n' 用于分割
# plt.legend()    # 当我们有多个 axes时，用legend把图例放在一起
# plt.show()


# ------------------ 5. stack plots:堆叠式图区 ------------------

import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,5,6,7,8]
eating = [2,3,4,2,1]
working = [7,8,6,7,2]
playing = [8,6,9,4,13]

plt.plot([],[],color='m', label='sleeping', linewidth=5) # 为堆叠的区域添加标签
plt.plot([],[],color='r', label='eating', linewidth=5) # 为堆叠的区域添加标签
plt.plot([],[],color='g', label='working', linewidth=5) # 为堆叠的区域添加标签
plt.plot([],[],color='c', label='playing', linewidth=5) # 为堆叠的区域添加标签

plt.stackplot(days, sleeping, eating, working, playing,colors=['m','c','r','g'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\ncheck it out')    # 加 '\n' 用于分割
plt.legend()    # 当我们有多个 axes时，用legend把图例放在一起
plt.show()