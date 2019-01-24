import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
"""
单次聚类
"""


class julei():
    def __init__(self):
        self.data = np.random.randint(-20, 20, size=(100, 2))

    # 求距离
    def dist(self):
        index1 = random.choice(range(100))
        index2 = random.choice(range(100))
        if index1 == index2:
            index2 = random.choice(range(100))
        target1 = self.data[index1]
        target2 = self.data[index2]
        temp = np.sum((self.data - target1) ** 2, axis=1)-np.sum((self.data - target2) ** 2, axis=1)
        return temp < 0

    def cut_data(self, df):
        A = df[df['type'] == True]
        B = df[df['type'] == False]
        # if mean:
        #     # 返回Series类型的对象
        #     return A.mean(), B.mean()
        # else:
            # 画图用
        return A, B

    # 画图
    def draw(self, df):
        A,B = self.cut_data(df)
        plt.scatter(A['x'], A['y'], color='red')
        plt.scatter(B['x'], B['y'], color='blue')
        # savefig要写在show之前
        plt.savefig('./julei.png')
        plt.show()

    # 分类
    def des(self):
        # 第一次分类
        data2 = self.dist()
        df = pd.DataFrame(self.data, columns=['x', 'y'])
        df.insert(2, 'type', data2)
        self.draw(df)


if __name__ == '__main__':
    func = julei()
    func.des()
