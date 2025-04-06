import numpy as np
import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

name = input("请输入你的姓名: ")
student_id = input("请输入你的学号: ")

x = np.linspace(0, 10, 100)
y = np.sin(x + int(student_id[0]) % 10) * np.cos(x + int(student_id[1]) % 10)

plt.plot(x, y)
plt.title(f"{name} 的折线图")
filename = f"{name}_折线图.png"

plt.savefig(filename)
plt.show()