def multiSort(self, array):
    maxx = 0
    maxxx = 0
    for sc in array:
        maxx = max(maxx,sc[1])
        maxxx = max(maxxx,sc[0])
    def keyy(ele):
        return ele[1]*maxx-ele[0]/maxxx
    array.sort(key=keyy,reverse=True)
    return array

     
def multiSort(self, array):
        # Write your code here
        array.sort(key = lambda x: (-x[1], x[0]))
        return array
