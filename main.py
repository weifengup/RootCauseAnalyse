import adtributor
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
df['出口流量']=pd.to_numeric(data['出口流量log(%)'])
df['立压']=pd.to_numeric(data['立压log(MPa)'])
df['C1']=pd.to_numeric(data['C1(%)'])
df['C2']=pd.to_numeric(data['C2(%)'])
df['总烃']=pd.to_numeric(data['总烃(%)'])
df['泵冲']=pd.to_numeric(data['泵冲1(spm)'])+pd.to_numeric(data['泵冲2(spm)'])+pd.to_numeric(data['泵冲3(spm)'])
df['大钩位置']=pd.to_numeric(data['大钩位置(m)'])
df['actual']=pd.to_numeric(data['溢流'])
df['pred']=pd.to_numeric(data['pred'])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result=adtributor.root_cause_analysis(df,df.shape[1])
    print(result.head(1000))


