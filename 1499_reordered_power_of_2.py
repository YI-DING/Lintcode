#Solution from @jiuzhang.com:
class Solution():
    def reorderedPowerOf2(self, N):
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << b))
                   for b in xrange(31))
#Mine:
    def reorderedPowerOf2(self, N):
        def dictize(number):
            dicc = {i:0 for i in range(10)}
            for num in str(number):
                dicc[int(num)] += 1
            return dicc
            
        n = len(str(N))
        #find exp s.t 10^n < 2^exp < 10^(n+1) 
        left, right = 10**(n-1), 10**n
        tmp, exp = right, 0
        while tmp > 0:
            tmp = tmp//2
            exp += 1
        exp -= 1
        small, big = exp-1, exp+1
        powers = [exp]
        while 2**small >= left:
            powers.append(small)
            small -= 1
        while 2**big < right:
            powers.append(big)
            big += 1
        print(powers)
        
        Ndict = dictize(N)
        for power in powers:
            if dictize(2**power) == Ndict:
                return True
        return False