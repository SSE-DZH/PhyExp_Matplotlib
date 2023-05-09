import matplotlib.pylab as plt

waveLength = [365,405,436,546,577]
Frequency = []
# 在这里修改截止电压数据值
cutOffVoltage = [1.141,0.941,0.737,0.211,0.177]
for i in waveLength:
    Frequency.append(3*10**3/i)
    print(Frequency)

plt.xlabel("Frequency (10^5Hz)")
plt.ylabel("Cut-off Voltage (V)")
plt.plot(Frequency,cutOffVoltage)
plt.grid(True)
plt.show()



