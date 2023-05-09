import matplotlib.pylab as plt

x = []
for i in range(-1,21):
    x.append(i)

# 在这里修改数据，依次是2mm,4mm,8mm对应的电流值
y1 = [-0.004,0.27,2.35,4.11,5.36,6.48,7.33,8.22,9,9.7,10.4,11,11.44,12.01,12.7,12.95,13.43,13.9,14.3,14.6,15.03,15.24]
y2 = [-0.02,0.19,0.65,1.6,2,2.43,2.75,3.07,3.31,3.58,3.85,4.08,4.26,4.45,4.64,4.81,4.98,5.11,5.25,5.39,5.58,5.64]
y3 = [-0.06,0.6,2.8,4.9,6.3,7.35,8.37,9.4,10.3,10.8,11.6,12.4,13,13.6,14.2,14.7,15.3,15.9,16.3,16.55,16.9,17.4]


tags = ['2mm','4mm','8mm']

plt.plot(x, y1, label=tags[0])
plt.plot(x, y2, label=tags[1])
plt.plot(x, y3, label=tags[2])
plt.legend(loc='upper left')

#在这里修改坐标轴范围
plt.xticks(range(-1,21))
plt.yticks(range(0, 20, 1))


plt.grid(True)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (10^-11 A)')
plt.ylim(bottom=0)
plt.show()
