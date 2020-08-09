class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {} #key是查找字符，value是下一节点字符
        self.end_of_word = '#'


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            #通过把Value定义为字典，不断嵌套key定义为下一个字符，setdefaut如果没有此字符，直接把Value赋值为字典，并拿出来给node，如果有此字符直接获取
            node = node.setdefault(char, {}) #setdefaut如果为空直接把这个拿出来，不为空直接获取
            print('char', char)
            print('self.root', self.root)
            print('fornode', node)

        print('node', node)
        node[self.end_of_word] = self.end_of_word
        print('self.root', self.root)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        # print(self.root)
        
        for char in word:
            if char not in node:
                return False
            node = node[char] #找到之后放到新的node里面
            # print(node)
        return self.end_of_word in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True





# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "apple"
obj.insert(word)
word = "app"
print(word)
obj.insert(word)
print('root',obj.root)
param_2 = obj.search(word)
print(param_2)
prefix = 'app'
param_3 = obj.startsWith(prefix)
print(param_3)