import pandas as pd
import numpy as np
import scipy.stats

# JS散度
def JS_divergence(p, q):
    p = np.array(p)
    q = np.array(q)
    M = (p + q) / 2
    # 方法一：自定义函数
    js1 = 0.5 * np.sum(p * np.log(p / M)) + 0.5 * np.sum(q * np.log(q / M))
    # 方法二：调用scipy包
    js2 = 0.5 * scipy.stats.entropy(p, M) + 0.5 * scipy.stats.entropy(q, M)
    return round(float(js2), 4)

# 根因分析
def root_cause_analysis(df, num):
    # 第一步：计算某维度下某因素的真实值和预测值占总收入的差异性----Surprise
    group = df.groupby('C1').sum()
    group = group.reset_index()
    group = group.rename(columns={'pred': 'pred_sum', 'actual': 'actual_sum'})
    dta = pd.merge(df, group, on='dimension', how='left')

    dta['actual_sum'] = dta['actual_sum'].apply(lambda x: round(x))
    dta['pred_sum'] = dta['pred_sum'].apply(lambda x: round(x))

    dta['p'] = dta['pred'] / dta['pred_sum']
    dta['q'] = dta['actual'] / dta['actual_sum']

    # 第一步：计算JS散度——surprise 惊奇度
    JS_list = []
    for i in dta['C1'].tolist():
        ls1 = dta[dta['C1'] == i]['p']
        ls2 = dta[dta['C1'] == i]['q']
        JS = JS_divergence(ls1, ls2)
        JS_list.append(JS)
    dta['JS'] = JS_list

    # 第二步：计算某维度下某因素波动占总体波动的比率----Explanatory power
    dta['EP'] = (dta['actual'] - dta['pred']) / (dta['actual_sum'] - dta['pred_sum'])

    # 转换维度与指标，二次计算
    df3 = df.copy()
    df3['dimension'] = df['indicator']
    df3['indicator'] = df['dimension']

    # 第一步：计算某维度下某因素的真实值和预测值占总收入的差异性----Surprise
    group = df3.groupby('C1').sum()
    group = group.reset_index()
    group = group.rename(columns={'pred': 'pred_sum', 'actual': 'actual_sum'})
    dta2 = pd.merge(df3, group, on='dimension', how='left')

    dta2['actual_sum'] = dta2['actual_sum'].apply(lambda x: round(x))
    dta2['pred_sum'] = dta2['pred_sum'].apply(lambda x: round(x))

    dta2['p'] = dta2['pred'] / dta2['pred_sum']
    dta2['q'] = dta2['actual'] / dta2['actual_sum']

    # 第一步：计算JS散度——surprise 惊奇度
    JS_list = []
    for i in dta2['dimension'].tolist():
        ls1 = dta2[dta2['dimension'] == i]['p']
        ls2 = dta2[dta2['dimension'] == i]['q']
        JS = JS_divergence(ls1, ls2)
        JS_list.append(JS)
    dta2['JS'] = JS_list

    # 第二步：计算某维度下某因素波动占总体波动的比率----Explanatory power
    dta2['EP'] = (dta2['actual'] - dta2['pred']) / (dta2['actual_sum'] - dta2['pred_sum'])

    # 拼接结果
    frames = [dta, dta2]
    result = pd.concat(frames)

    # 第三步：排序出结果
    result = result.sort_values(by=['JS', 'EP'], ascending=False).reset_index()
    root_cause = result.groupby('dimension').mean().sort_values(by=['JS'], ascending=False).reset_index().head(1)

    return root_cause['dimension'].tolist()[0], result[['dimension', 'indicator']].head(num)

