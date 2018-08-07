class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        operator = ""
        y = [i for i in str(x)]
        try:
            int(y[0])
        except:
            operator = y[0]
            y.remove(y[0])
        y.reverse()
        if operator:
            print int("{0}{1}".format(operator, "".join(y)))
        else:
            print int("".join(y))

obj = Solution()
obj.reverse(-123)
obj.reverse(987654321)

