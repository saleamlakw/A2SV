class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.hashmap=Counter()
        self.timeToLive=timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hashmap[tokenId]=currentTime
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.hashmap and (self.hashmap[tokenId]+self.timeToLive)>currentTime:
            self.hashmap[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        re=0
        # print(self.hashmap)
        for r in self.hashmap:
            if (self.hashmap[r]+self.timeToLive)>currentTime:
                re+=1
        return re


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)