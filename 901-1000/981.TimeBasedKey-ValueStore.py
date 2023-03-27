class TimeMap(object):

    def __init__(self):
        self.dic = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """

        if key not in self.dic:
            self.dic[key] = []
        self.dic[key] += [[value, timestamp]]

        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """        
        if not key in self.dic:
            return ""
        arr = self.dic[key]

        i = len(arr) - 1
        curr = ""
        while i >= 0 and arr[i][1] > timestamp:
            i -= 1
        
        if i >= 0:
            curr = arr[i][0]

        return curr 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
