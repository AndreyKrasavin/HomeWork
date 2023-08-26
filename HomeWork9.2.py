
import pandas as pd

df = pd.read_csv('california.csv')

df[df['population'] <=500 ], df['median_house_value'] # наверное тупо указывать еще условие что от 0 и больше, ведь количество людей не может быть отрицательным значение
df[df['households'].max() ], df['population'].min()
