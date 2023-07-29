class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  

        while b != 0:
            carry = a & b
            a = (a ^ b) & mask
            b = ((carry & mask) << 1) 


        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)

        return a


def main():
    Sol = Solution()
    print(Sol.getSum(5, 10))
    print(Sol.getSum(20, 30))
    print(Sol.getSum(-1000, 1000))
    print(Sol.getSum(-1, 0))
    return 

if __name__ == '__main__':
    main()
