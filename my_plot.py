import matplotlib.pyplot as plt

#1.创建画布
plt.figure(figsize=(20, 8), dpi=200)

#2.图像绘制
x = [1, 2, 3, 4]
y = [5, 5, 5, 4]
plt.plot(x, y)

#2.1图像保存
plt.savefig("./data/test.png")

#3.图像展示
plt.show()


