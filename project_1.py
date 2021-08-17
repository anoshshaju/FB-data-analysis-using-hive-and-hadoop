import pandas as pd
data = pd.read_csv(r"C:\Users\Ajish Shaju\Downloads\input files\pseudo_facebook.csv")
n = len(data)
userid = list(data['userid'].unique())
old_userid = 0 
f = open("fb_details.txt",'a')
for i in data.index:
    if data['userid'][i] in userid:
        record = data['userid'][i],data['age'][i],data['gender'][i],data['friend_count'][i]
        f.write(str(record)+'\n')
        userid.remove(data['userid'][i])
f.close()        