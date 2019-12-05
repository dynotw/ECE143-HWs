import pandas as pd

def split_count(x):
    '''

    :param x: input, series
    :return: dataframe
    '''
    assert isinstance(x,pd.Series)

    # split a string column into series(dataframe, split1)
    split1 = x.str.split(', ').apply(pd.Series)

    # append all series in dataframe, then value the frequency of each words
    se = split1[0]
    for i in range(1, split1.shape[1]):
        se = se.append(split1[i], ignore_index=True)
    da = se.value_counts(ascending=True)
    da = da.to_frame()
    da.rename(columns={0: 'count'}, inplace=True)

    return da

if __name__ == '__main__':
    df = pd.read_csv('survey_data.csv',index_col='ID')
    # index_col来限定index
    print(df)
    x = df['Is there anything in particular you want to use Python for?']
    print(x)
    print(split_count(x))


