import pandas as pd
# use CategoricalDtype

def add_month_yr(x):
    '''
    :param x: dataframe
    :type x: pd.DataFrame
    :return: dataframe
    '''

    assert isinstance(x, pd.DataFrame)
    # ID column is index for x

    dict_month = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
                  '5': 'May', '6': 'Jun', '7': 'Jul', '8': 'Aug',
                  '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    s = x['Timestamp']

    s1 = s.str.split('/| ', expand=True).rename(columns={0: 'month', 1: 'day', 2: 'year', 3: 'time'})
    # print(s1)
    list_month = [dict_month[x] for x in s1['month']]
    # print(month_list)

    s1['month'] = list_month
    s1['month-yr'] = s1.apply(lambda i: i.month + '-' + i.year, axis=1)
    x['month-yr'] = s1['month-yr']

    return x

def fix_categorical(x):
    '''
    :param x:
    :return:
    '''

    assert isinstance(x,pd.DataFrame)

    cat = pd.api.types.CategoricalDtype(categories=['Sep-2017', 'Jan-2018', 'Feb-2018', 'Mar-2018','Apr-2018','Sep-2018','Oct-2018','Jan-2019'],ordered=True)
    x['month-yr'] = x['month-yr'].astype(cat)

    return x

# if __name__ == '__main__':
#     df = pd.read_csv('survey_data.csv',index_col='ID')
#     x=add_month_yr(df)
#     y=fix_categorical(x)
#     print(y['month-yr'].dtype)
#     print(y)
#     print(x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index())