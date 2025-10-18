class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = [homepage]
        self.currentSite = 0
        self.n = 1
        

    def visit(self, url: str) -> None:
        if self.currentSite+1 < len(self.browser):
            self.browser[self.currentSite+1] = url
        else:
            self.browser.append(url)
        self.currentSite += 1
        self.n = self.currentSite + 1
    def back(self, steps: int) -> str:
        self.currentSite = max(0,self.currentSite  - steps)
        return self.browser[self.currentSite]
    def forward(self, steps: int) -> str:
        self.currentSite = min(self.n-1,self.currentSite + steps)
        return self.browser[self.currentSite]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)