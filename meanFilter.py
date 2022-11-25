import random
from matplotlib import pyplot as plt
import numpy as np

# 50~51의 랜덤으로 생성되는 1000개의 
# 샘플의 실시간으로 평균필터 된 값을 구하고 (샘플이 추가될때마다)
# 최종 평균을 구하세요

sampleCount = 1000
samples = []

meanPlots = []
samplePlots = []

result = 0

for i in range(sampleCount):
    sample = random.uniform(50,51)
    samples.append(sample)
    # print('val : ',val)
    # 평균 필터

    # 평균값을 계산
    # 평균 = 총합 / 갯수
    # mean = sum(samples) / len(samples)
    result = result + sample
    mean = result / (i+1)
    # mean = val
    # t = 0
    # for v in samples:
    #     t+= v
    # mean = t / (i+1)

    print(f'[{i+1}] sample : ', mean)

    samplePlots.append([sample])
    meanPlots.append([mean])

print('result mean : ', mean)

plt.plot(samplePlots, color='b', label='sample')
plt.plot(meanPlots, color='r', label='mean', alpha =0.5)
plt.legend(loc='best')
plt.show()