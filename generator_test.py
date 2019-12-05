def foo():
    bar_a = yield 1
    print('adfasdf')# bar_a是语句块(yield 1)的返回值，默认为None
    print(bar_a)
    bar_a=1
    print(bar_a)
    bar_b = yield bar_a
    yield "最后一个值，再迭代就要报StopIteration了"

def eoo():
    bar_a = yield 1
    print('adfasdf')  # bar_a是语句块(yield 1)的返回值，默认为None
    print(bar_a)
    bar_b = yield bar_a
    yield "最后一个值，再迭代就要报StopIteration了"


def gen():
    while True:
        s = yield
        print(s)