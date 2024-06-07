class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter]=TrieNode()
            cur=cur.children[letter]
        cur.isEnd=True
    def search(self,word):
        cur=self.root
        re=""
        for letter in word:
            if letter not in cur.children:
                return word

            cur=cur.children[letter]
            re+=letter
            if cur.isEnd:
                return re
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie=Trie()
        for word in dictionary:
            trie.insert(word)
        sentence=sentence.split()

        for i in range(len(sentence)):
            sentence[i]=trie.search(sentence[i])
        return " ".join(sentence)

