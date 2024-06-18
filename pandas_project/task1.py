'''
В ячейке ниже представлен код генерирующий DataFrame, 
которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''

import random
import pandas as p

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = p.DataFrame({'whoAmI':lst})
# print(data.head())

view_one_hot = p.DataFrame()
view_one_hot['robot'] = (data['whoAmI'] == 'robot').astype(int)
view_one_hot['human'] = (data['whoAmI'] == 'human').astype(int)

print(view_one_hot.head())
