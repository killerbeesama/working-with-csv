import pandas as pd

data = pd.read_csv("working with csv/Central_Park_Data.csv")
grey=data[data['Primary Fur Color'] == 'Gray'].count()['Primary Fur Color']
red=data[data['Primary Fur Color'] == 'Cinnamon'].count()['Primary Fur Color']
black=data[data['Primary Fur Color'] == 'Black'].count()['Primary Fur Color']

new_data = {'Fur color':['grey','red','black'],
            'Count':[grey,red,black]}
df = pd.DataFrame(new_data)
print(df)

