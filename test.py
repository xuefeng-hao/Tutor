import pandas as pd
import os
path= '.'
filenames=os.listdir(path)
print(filenames)
mp3_list=[]
for file in filenames:
    root, extension = os.path.splitext(file)
    if extension == '.mp3':
        file=file.rstrip(".mp3")
        mp3_list.append(file)
print(mp3_list)
df=pd.DataFrame(mp3_list)
file_name='Liedname.csv'
df.to_csv(file_name,index=False)