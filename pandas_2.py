import pandas as pd
def add_month_yr(x):
    '''
    :param x: dataframe
    :type x: pd.DataFrame
    :return: dataframe
    '''

    assert isinstance(x, pd.DataFrame)
    # ID column is index for x

    month_dict = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
                  '5': 'May', '6': 'Jun', '7': 'Jul', '8': 'Aug',
                  '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    s = x['Timestamp']
    # print(s)


    s1 = s.str.split('/| ', expand=True).rename(
        columns={0: 'month', 1: 'day', 2: 'year', 3: 'time'})
    # split() 分隔函数，如果有多个分隔符，那么各个分隔符之间用'|'隔开
    # print(s1)
    month_list = [month_dict[x] for x in s1['month']]
    # print(month_list)

    s1['month'] = month_list
    # expand_s.iloc[:, 0]与['month']效果一样
    # expand_s.iloc[:, 0] = month_list
    # iloc： works on the positions in the index （it only takes integers）， 是根据索引的行数来工作
    # loc: works on the labels in the index （it takes string）,当我们自行定义了index，使得index不再是默认的0, 1, 2, 3......., 同时同样也可以用iloc通过行数来索引
    s1['month-yr'] = s1.apply(
        lambda i: i.month + '-' + i.year, axis=1)
    # axis=2说明按行，axis=0说明按列
    x['month-yr'] = s1['month-yr']
    # print(x)

    return x

if __name__ == '__main__':
    df = pd.read_csv('survey_data.csv',index_col='ID')
    # 限定读取csv文件后的index
    print(type(add_month_yr(df)))
    print(add_month_yr(df))