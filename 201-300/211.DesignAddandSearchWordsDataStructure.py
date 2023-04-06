class WordDictionary(object):

    def __init__(self):
        self.prefix = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.prefix
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]

        cur['is_word'] = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        cur = [self.prefix]
        for letter in word:
            nex = []
            if len(cur) == 0:
                return False
            if letter == '.':
                for dic in cur:
                    nex += [val for val in dic.values() if val != True and val != False]
            else:
                for dic in cur:
                    if letter in dic:
                        nex += [dic[letter]]
            cur = nex
            
        for dic in cur:
            if 'is_word' in dic and dic['is_word']:
                return True
        
        return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
