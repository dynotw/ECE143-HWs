class Interval(object):
    def __init__(self, a, b):
        """
        :a: integer
        :b: integer
        """
        assert a < b
        assert isinstance(a, int)
        assert isinstance(b, int)
        self._a = a
        # why not self.a = a ?

        self._b = b

    def __repr__(self):
        # if isinstance(self,Interval):

        # repression of the output
        # some output is not visible, we have to change the format of output
        # all the output from print function, is string

        return 'Interval('+ str(self._a) +','+ str(self._b) +')'



    def __eq__(self, other):
        # a=b
        assert isinstance(self, Interval)
        assert isinstance(other, Interval)

        return self._a == other._a and self._b==other._b

    # def __lt__(self, other):
    #     # a<b
    #     pass
    #
    # def __gt__(self, other):
    #     # a>b
    #     pass
    #
    # def __ge__(self, other):
    #     # a>=b
    #     pass
    #
    # def __le__(self, other):
    #     # a<=b
    #     pass

    def __add__(self, other):
        '''
        a+b
        :param other:
        :return:
        '''
        assert isinstance(self, Interval)
        assert isinstance(other, Interval)

        interval1_a = self._a
        interval1_b = self._b
        interval2_a = other._a
        interval2_b = other._b

        # interval1 is same as interval2
        if self==other:
            return self

        # interval 1 and 2 don't intersect
        elif ((interval1_b <= interval2_a) or (
                interval2_b <= interval1_a)):
            listout = []
            listout.append(self)
            listout.append(other)

            return listout

        # 1a < 2a and 2b < 1b
        if (interval1_a <= interval2_a and interval2_b <= interval1_b):
            return Interval(interval1_a, interval1_b)

        # 1a < 2a and 1b < 2b
        elif (interval1_a <= interval2_a and interval1_b <= interval2_b):
            return Interval(interval1_a, interval2_b)

        # 2a < 1a < and 2b < 1b
        elif (interval2_a <= interval1_a and interval2_b <= interval1_b):
            return Interval(interval2_a, interval1_b)

        # 2a < 1a and 1b < 2b
        elif (interval2_a <= interval1_a and interval1_b <= inrerval2_b):
            return Interval(interval2_a, interval2_b)

        else:
            # this is very useful, ensuring always have output

            raise NotImplementedError