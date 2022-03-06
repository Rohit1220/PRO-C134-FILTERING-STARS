import matplotlib,pandas as pd

df = pd.read_csv("D.csv")

dis = df['Distance'].to_list()
dis.pop(0)
new_dis = []

for i in range(0,len(dis)):
    dist = dis[i]
    if dist <=100:
        new_dis.append(dis)

new_dis.to_csv('FS.csv')