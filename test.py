import pandas as pd
lists = [['data center','X',94,47]
 ,['data center','Y',6,3]]
df = pd.DataFrame(lists, columns=['dimension','indicator','pred','actual'])
df2 = pd.DataFrame(lists, columns=['dimension','indicator','pred','actual'])
result=[]
result.append(df)
result.append(df2)
result=pd.concat(result)
print(result)