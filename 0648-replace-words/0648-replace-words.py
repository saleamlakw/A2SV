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
        result=""
        for letter in word:
            if letter not in cur.children:
                return word
            result+=letter
            cur=cur.children[letter]
            if cur.isEnd:
                return result
        return word
    def startsWith(self,prefix):
        cur=self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur=cur.children[letter]
        return True


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie=Trie()
        for ele in dictionary:
            trie.insert(ele)

        sen=sentence.split()
        for i in range(len(sen)):
            sen[i]=trie.search(sen[i])
        return " ".join(sen)
