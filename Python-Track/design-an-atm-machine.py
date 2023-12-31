class ATM:

    def __init__(self):
        self.money=[0]*5
        self.before=[]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.money[i]+=banknotesCount[i]
    def withdraw(self, amount: int) -> List[int]:
        self.before=self.money[:]
        re=[0]*5
        ch=amount
        
        if amount>=500:
            k=amount//500
            if self.money[4]>=k:
                    self.money[4]-=k
                    amount-=(k*500)
                    re[4]+=k
            else:
                amount-=(self.money[4]*500)
                re[4]+=self.money[4]
                self.money[4]=0
            
        if amount>=200:
            k=amount//200
            if self.money[3]>=k:
                    self.money[3]-=k
                    amount-=(k*200)
                    re[3]+=k
            else:
                amount-=(self.money[3]*200)
                re[3]+=self.money[3]
                self.money[3]=0

        if amount>=100:
            k=amount//100
            if self.money[2]>=k:
                    self.money[2]-=k
                    amount-=(k*100)
                    re[2]+=k
            else:
                amount-=(self.money[2]*100)
                re[2]+=self.money[2]
                self.money[2]=0

        if amount>=50 :
            k=amount//50
            if self.money[1]>=k:
                    self.money[1]-=k
                    amount-=(k*50)
                    re[1]+=k
            else:
                amount-=(self.money[1]*50)
                re[1]+=self.money[1]
                self.money[1]=0

        if amount>=20 :
            k=amount//20
            if self.money[0]>=k:
                    self.money[0]-=k
                    amount-=(k*20)
                    re[0]+=k
            else:
                amount-=(self.money[0]*20)
                re[0]+=self.money[0]
                self.money[0]=0
        
        if (re[4]*500+re[3]*200+re[2]*100+re[1]*50+re[0]*20)==ch:
            self.before=self.money
            return re
        else:
            self.money=self.before
            return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)