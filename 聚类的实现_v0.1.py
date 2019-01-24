import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
"""
加入回归
"""


class julei():
    def __init__(self):
        self.data = np.random.randint(-20, 20, size=(100, 2))

    # 求距离
    def dist(self, avg=None):
        if avg:
            target1 = np.array([avg[0]['x'], avg[0]['y']])
            target2 = np.array([avg[1]['x'], avg[1]['y']])
        else:
            index1 = random.choice(range(100))
            index2 = random.choice(range(100))
            if index1 == index2:
                index2 = random.choice(range(100))
            target1 = self.data[index1]
            target2 = self.data[index2]
        temp = np.sum((self.data - target1) ** 2, axis=1)-np.sum((self.data - target2) ** 2, axis=1)
        return temp < 0

    def cut_data(self, df, mean=False):
        A = df[df['type'] == True]
        B = df[df['type'] == False]
        if mean:
            # 返回Series类型的对象
            return A.mean(), B.mean()
        else:
            # 画图用
            return A, B

    # 画图
    def draw(self, df):
        fig = plt.figure()
        A,B = self.cut_data(df)
        plt.scatter(A['x'], A['y'], color='red')
        plt.scatter(B['x'], B['y'], color='blue')
        plt.show()
        plt.savefig('./julei.png')

    # 分类
    def des(self):
        # 第一次分类
        data2 = self.dist()
        df = pd.DataFrame(self.data, columns=['x', 'y'])
        df.insert(2, 'type', data2)
        A=np.array([0.0,0.0])
        B=np.array([0.0,0.0])
        while True:
            # 获取2个类各自的平均值
            # 返回series类型
            A1, B1 = self.cut_data(df, mean=True)
            # 取出2个平均点的x，y值np.array类型
            A1 = A1[:2].values
            B1 = B1[:2].values
            # 数组比较
            if np.equal(A.all(),A1.all()) & np.equal(B.all(),B1.all()):
                break
            else:
                A = A1
                B = B1
                # 获取新的类
                df['type'] = self.dist(avg=[A1, B1])
                self.draw(df)


if __name__ == '__main__':
    func = julei()
    func.des()
