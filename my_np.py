import matplotlib.pyplot as plt
import numpy as np

# 0.生成数据
x = np.linspace(-10, 10, 1000)
y = np.sin(x)

# 1.创建画布
plt.Figure(figsize=(20,8), dpi=100)

# 2.图像绘制
plt.plot(x,y)

plt.grid()

# 3.图像显示
plt.show()