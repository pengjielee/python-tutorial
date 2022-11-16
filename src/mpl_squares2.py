import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
# 设置线条粗细
ax.plot(squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签
ax.set_title("Square number", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("square of value", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()