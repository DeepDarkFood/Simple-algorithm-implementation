import numpy as np
import pandas as pd
import math


class Tree():
    def __init__(self):
        self.data = pd.DataFrame([[1,0,1],[0,0,0],[0,1,1],[1,1,1]],columns=['a','b','t'])

    def count(self,data):
        num0 = data[data['t'] == 0]['t'].count()
        num1 = data[data['t'] == 1]['t'].count()
        return num0,num1

    def Ent(self, x):
        if x == 't':
            # 计算目标值信息熵
            data = self.data
            num = data['t'].count()
            num0, num1 = self.count(data)
            ent = -(num0 / num) * math.log(num0 / num, 2) - (num1 / num) * math.log(num1 / num, 2)
            return ent
        else:
            data = self.data
            # 分为结果为1和0俩类，分别计算信息熵
            data0 = data[data[x] == 0]
            data1 = data[data[x] == 1]
            num00,num01=self.count(data0)
            num10,num11=self.count(data1)
            num0 = data0['t'].count()
            num1 = data1['t'].count()
            try:
                ent0 = -(num00 / num0) * math.log(num00 / num0, 2) - (num01 / num0) * math.log(num01 / num0, 2)
            except:
                ent0=0
            try:
                ent1 = -(num10 / num1) * math.log(num10 / num1, 2) - (num11 / num1) * math.log(num11 / num1, 2)
            except:
                ent1=0
            return ent0, ent1

    def tree(self, input):
        # 计算Gain
        data = self.data
        ent_t=self.Ent('t')
        ent_a0,ent_a1=self.Ent('a')
        ent_b0,ent_b1=self.Ent('b')
        gain_a=ent_t-(1/2*ent_a0+1/2*ent_a1)
        gain_b=ent_t-(1/2*ent_b0+1/2*ent_b1)
        if gain_a>gain_b:
            data1=data[data['a']==input[0]]
            print('类型：',data1[data1['b']==input[1]]['t'].values[0])
        else:
            data1 = data[data['b'] == input[1]]
            print('类型：',data1[data1['a'] == input[0]]['t'].values[0])


if __name__ == '__main__':
    tr = Tree()
    tr.tree([1,0])
