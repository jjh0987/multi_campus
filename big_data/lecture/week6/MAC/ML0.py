import tensorflow as tf
print(tf.__version__)
import matplotlib.pyplot as plt
from  sklearn.neighbors import KNeighborsClassifier


data_len_bream = 35
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

plt.scatter(bream_length,bream_weight)
plt.xlabel('length')
plt.ylabel('weight')

data_len_smelt = 14
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

plt.scatter(smelt_length,smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')

lenght = bream_length + smelt_length
weight = bream_weight + smelt_weight
fish = [[i,j] for i,j in zip(lenght,weight)]
plt.scatter(lenght,weight)

fish_ans_label = [1]*data_len_bream + [0]*data_len_smelt

kn = KNeighborsClassifier()
kn.fit(fish,fish_ans_label)
kn.score(fish,fish_ans_label)
kn.predict([[26,350],[8,10]]) # (2,1)

kn_49 = KNeighborsClassifier(n_neighbors=49) # k-neighbor 참고데이터 49 default : 5
kn_49.fit(fish,fish_ans_label)
kn_49.score(fish,fish_ans_label) # 0.7142857142857143
35/49

import numpy as np
input_arr = np.array(fish)
input_arr.shape # list 형식은 shape 불가

ans_arr = np.array(fish_ans_label)
np.random.seed(42) # ?
index = np.arange(49)
np.random.shuffle(index)
print(index)

train_fish = input_arr[index[:35]]
train_ans_arr = ans_arr[index[:35]]
test_fish = input_arr[index[35:]]
test_ans_arr = ans_arr[index[35:]]
kn = KNeighborsClassifier()
kn.fit(train_fish,train_ans_arr)
kn.score(test_fish,test_ans_arr)

kn.predict(test_fish)

plt.scatter(train_fish[:,0],train_fish[:,1])
plt.scatter(test_fish[:,0],test_fish[:,1])
kn.score([[20,200]],[1]) # data form