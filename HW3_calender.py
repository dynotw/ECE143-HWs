import calendar

def number_of_days(year,month):
    '''

    :param year:
    :param month:
    :return:
    '''

    assert isinstance(year, int)
    assert year >0
    assert isinstance(month, int)
    assert 1<=month<=12

    x,y = calendar.monthrange(year, month)
    return y

def number_of_leap_years(year1,year2):
    '''

    :param year1:
    :param year2:
    :return:
    '''

    assert isinstance(year1,int)
    assert year1 >0
    assert isinstance(year2,int)
    assert year2 >0
    assert year2>=year1

    # calendar.leapdays includes year1 not year2

    x = calendar.leapdays(year1, year2)
    if calendar.isleap(year2):
        x= x+1

    return x

def get_day_of_week(year,month,day):
    '''

    :param year:
    :param month:
    :param day:
    :return:
    '''

    assert isinstance(year,int)
    assert year >0
    assert isinstance(month,int)
    assert 1<=month<=12
    assert isinstance(day,int)
    assert 1<=day<=31

    x = calendar.weekday(year, month, day)

    list1=['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday', 'Sunday']

    return list1[x]

