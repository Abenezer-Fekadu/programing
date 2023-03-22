class Solution:
    def convertToBase7(self, num: int) -> str:
        base7_num = ''
        sign, num = ('', num) if num >= 0 else ('-', -num)

        while True:
            num, remainder = divmod(num, 7)
            base7_num = str(remainder) + base7_num

            if num == 0:
                break            

        return sign + base7_num