class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # a^n % b = (a%b)^n %b
        base, ans = a, 1
        while n > 0:
            if n % 2 == 1:
                ans = ans % b * base % b 
            base = (base % b)**2
            n = n // 2
        return ans % b