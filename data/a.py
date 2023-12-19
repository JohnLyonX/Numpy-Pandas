import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('600132.csv')  # parse_dates=True表示将日期转换为日期格式
df['Date'] = pd.to_datetime(df['Date'])

# 选择9月份的数据
september_data = df[(df['Date'] >= '2020-09-01') & (df['Date'] <= '2020-09-30')]
# 绘制柱形图
plt.bar(september_data['Date'], september_data['Volume'], color='blue')
plt.xticks(september_data['Date'], rotion=45)
plt.show()