
import datetime

class Budget:
    '''
        This class is tracking personal budget
        by tracking the income and expenses
    '''
    # init method 
    def __init__ (self, process = '', process_type = '', amount = 0):
        self.process = process
        self.process_type = process_type
        self.amount = amount
        #self.Balance = self.set_balance() + amount
        #self.today = datetime.datetime.now()
        #self.sign = ''
        self.statement = [[process,process_type,amount]]
        
    #def set_balance(self):
        #self.Balance += self.amount
    
    #def set_trans(self):
        #if self.process == 'Income':
            #self.sign = '+'
            #self.statement.append([self.today, self.process, self.process_type, self.sign, self.amount])
        #else:
            #self.sign = '-'
            #self.statement.append([self.today, self.process, self.process_type, self.sign, self.amount])  
            #if self.balance < 0:
                #raise ValueError('Transaction Declined!')    
    def get_statment(self):
        print('Process name | Process Type | Amount')
        for i in self.statement:
            list(map(lambda x:print(x),self.statement))
    
    def acc_summary(self):        
        #print('Your New Balace = {} - Updated at {}'.format(self.Balance, self.today))
        print('Process name | Process Type | Amount')
        for i in self.statement:
            list(map(lambda x:print(x),self.statement))
        return


# User Input
def switcher(argu):
    process = ''
    process_name = ''
    amount = 0
    trans_list = []
    if argu == '1':
        process = 'Income'
        process_type = input('What is your Income Type? ')
        amount = int(input('How much is your income ? '))
        if amount <= 0:
            raise ValueError('You Entered an amout less than or equal zero')
    else:
        process = 'Expense'
        process_type = input('What is your Expense Type? ')
        amount = int(input('How much is your expense ? '))
        if amount <= 0:
            raise ValueError('You Entered an amout less than or equal zero') 
        #amount = - amount
    trans_list.append(process)
    trans_list.append(process_type)
    trans_list.append(amount)
    return trans_list

trans = Budget()

user_input = input("""Please Choose From The Menu.. 
1 - Add Income
2 - Add Expense
3 - Show Summary
4 - Exit
* Enter a Number """)
llst = [] # to store the return from the switcher function
while user_input != '4':
    if user_input in ['1','2']:
        llst = switcher(user_input)
        p, p_t, a = llst[0],llst[1],llst[2] # process, process type, amount 
        trans = Budget(p,p_t,a)
    elif user_input == '3':
        trans.get_statment()
        break
    else:
        user_input = input('Invalid Entry!!!')
    user_input = input("""Please Choose From The Menu.. 
    1 - Add Income
    2 - Add Expense
    3 - Show Summary
    4 - Exit
    * Enter a Number """)
else:
    print('Thank you for using the Budget App!!')