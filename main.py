import random
import pandas as pd
def sort(file):
    data = pd.read_csv(str(file), header=None, na_values=" NaN")
    data = data[data[0].notna()]
    mylist = data[0].tolist()
    random.shuffle(mylist)
    print(mylist)
    for i in range(len(mylist)-1):
        print(mylist[i] + " + " + mylist[i+1])
    print(mylist[-1] + " + " + mylist[0])

x = str(input('enter file name:'))
if '.csv' in x:
    sort(x)
else:
    sort(x+'.csv')