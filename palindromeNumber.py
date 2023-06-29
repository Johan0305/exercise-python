class Solution:
    def isPalindrome(self, x: int) -> bool:
        num= str(x)[::-1]

        return int(num) == x


Solution.isPalindrome("",121)