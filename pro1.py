class bank:
    bname = 'sbi'
    bloc = 'banglore'
    bceo = 'raj'
    count = 2
    if count > 0:
        def __init__(self, name, num, mail, addr, bal, acnum):
        
            self.name = name
            self.num = num
            self.mail = mail
            self.addr = addr
            self.bal = bal
            self.acnum = acnum
            self.limit()
    else:
        print('only two can be created for a class')

    @classmethod
    def limit(cls):
        cls.count-=1
    def disp(self):
        print(self.name, self.num, self.mail, self.addr, self.bal, self.acnum)
    
    def chname(self, new):
        self.name = new
    
    def withdraw(self, draw):
        if draw <= self.bal:
            self.bal -= draw 
        return f'hi {self.name} the debited amount is {draw} and available balance is {self.bal} '

    def credit(self, credit):
        self.bal+= credit
        return f'hi {self.name} the credit amount is {credit} and avilable balance is {self.bal}'  

    def transfer(self, other,amt):
        if self.bal >=amt:
            other.bal+=amt
            self.bal-=amt
            return f'{amt} is successfully transferred from {self.name} to {other.name}'
        else:
            return 'insufficient balance'

a = bank('amith', 986557447, 'amith@gmail.com', 'gadag', 6500, 12345)
b = bank('arun', 8874567488, 'arun@gamil.com', 'dvg', 9000, 23654)