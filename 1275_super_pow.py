class Solution:
    """
    @param a: the given number a
    @param b: the given array
    @return: the result
    """
    def superPow(self, a, b):
        b = int("".join([str(num) for num in b]))
        base, ans = a, 1
        while b > 0:
            if b % 2 == 1:
                ans = ans % 1337 * base % 1337 
            base = (base % 1337)**2
            b = b // 2
        return ans % 1337
#a good one:
result = 1
for i in range(len(b)):
    result = ((result**10) * (a**int(b[i]))) % 1337
return result