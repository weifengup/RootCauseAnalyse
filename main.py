# import adtributor
import pandas as pd
# coding=utf-8
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
pd.set_option('display.width',1000)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)

CSV_FILE_PATH = 'Rec1909021733.csv'
data = pd.read_csv(CSV_FILE_PATH, encoding='utf-8')
df=pd.DataFrame(data['DateTime'], columns=['DateTime'])
df['Time']=data['Time']
df['出口流量']=data['出口流量log(%)']
df['立压']=data['立压log(MPa)']
df['C1']=data['C1(%)']
df['C2']=data['C2(%)']
df['总烃']=data['总烃(%)']
df['泵冲']=data['泵冲1(spm)']+data['泵冲2(spm)']+data['泵冲3(spm)']
df['大钩位置']=data['大钩位置(m)']
df['actural']=data['溢流']
df['pred']=data['pred']
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(df.head(100))


