class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def search(self, word: str) -> None:
        current = self.root  # make a root node funtion from where it originates
        for c in word:           # Search each chars of strings
            if c not in current.children:     # check if current chars is present in children node of not
                return False                  # return fasle if it is not their 
            current = current.children[c]     # if it is their then pass to next children node for same test to pass on
        return current.endofWord              # check and end this function as we reach end node


    def insert(self, word: str) -> bool:
        current = self.root # Current start from root node
        for c in word:              # Break string into chars
            if c not in current.children:        # Check if c is present or not to pass it to Trienode
                current.children[c] = TrieNode() # make a child node and pass missing charter into it 
            current = current.children[c]
        current.endofWord = True     # Telling that it is last node of word no new clid node from here 



             
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True    
