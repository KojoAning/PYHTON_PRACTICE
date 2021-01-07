# import requests
# import pickle
# data = requests.get("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# # print(data)
#
# lis = data.split("\n")
# # print(lis)
# lis_2 = [item.split(",") for item in lis if len(item)!= 0]
# print(lis_2)
#
# with open("myiris.pkl","wb") as f:
#     pickle.dump(lis_2,f)

#-----------------------------cheaking the file -------------------------------------------------------------------

import pickle
with open("myiris.pkl","rb") as f :
    print(pickle.load(f))