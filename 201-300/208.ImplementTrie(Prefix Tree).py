class Trie(object):

    def __init__(self):
        self.prefix = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        
        cur = self.prefix
        for letter in word:
            if letter not in cur:
                cur[letter] = {'word_exists': False}
            cur = cur[letter]
        
        cur['word_exists'] = True


            


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.prefix
        for letter in word:
            if letter in cur:
                cur = cur[letter]
            else:
                return False
        return cur['word_exists']
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.prefix
        for letter in prefix:
            if letter in cur:
                cur = cur[letter]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
