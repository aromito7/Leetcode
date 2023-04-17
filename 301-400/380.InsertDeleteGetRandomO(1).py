class RandomizedSet(object):

    def __init__(self):
        self.dic = defaultdict(lambda: -1)

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        output = False if self.dic[val] == 1 else True
        
        self.dic[val] = 1
        return output
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        output = True if self.dic[val] == 1 else False
        self.dic.pop(val)

        return output
        

    def getRandom(self):
        """
        :rtype: int
        """

        keys = self.dic.keys()
        length = len(keys)

        return keys[randint(0, length - 1)]




        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
