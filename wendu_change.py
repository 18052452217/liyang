#案例：显示温度变化
import random

import matplotlib.pyplot as plt

#0.生成数据
x = range(60)
y_beijing = [random.uniform(10,15) for i in x]
y_shanghai = [random.uniform(15,25) for i in x]

#1.创建画布
plt.Figure(figsize=(20,8), dpi=100)

#2.图像绘制
plt.plot(x,y_beijing, color="g", label="北京", linestyle="-.")
plt.plot(x,y_shanghai, label="山西")

#2.1添加x,y轴刻度
y_ticks = range(40)
x_ticks_label = ["11点{}分".format(i) for i in x]

plt.yticks(y_ticks[::5])
plt.xticks(x[::20], x_ticks_label[::20])

#2.2添加网格
plt.grid(True, linestyle="-", alpha=0.5)

#2.3添加描述
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("一小时温度变化图", fontsize=10)

#2.4显示图例
plt.legend(loc="best")


#3.图像显示
plt.show()