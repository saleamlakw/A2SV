class ListNode:
    def __init__(self,val = 0,next = None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = ListNode(homepage)
        self.current = self.browser
    def visit(self, url: str) -> None:
        newUrl = ListNode(url)
        self.browser.next  = newUrl
        newUrl.prev = self.browser
        self.browser= self.browser.next
    def back(self, steps: int) -> str:
        while self.browser.prev and steps:
            self.browser = self.browser.prev
            steps -= 1
        return self.browser.val
    def forward(self, steps: int) -> str:
        while self.browser.next and steps:
            self.browser = self.browser.next
            steps -= 1
        return self.browser.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)