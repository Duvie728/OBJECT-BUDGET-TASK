"""
# This is a Budget class
"""
class Budget:

    """
    # Creating a variable called avaialable_ balance
    """
    available_balance = 10000

    """
# This is the attribute of the class
    """
    def __init__(self,amount):
        self.amount = amount

        """
These are the method/function in the class
        """

    def withdraw_funds(self):
        print(f'{self.amount} naira is being withdrawnfrom this category')

    def deposit_funds(self):
        print(f'{self.amount} naira has been deposited in this category')

    def transfer_funds(self):
        print(f'{self.amount} naira has been transfered to category')

    def check_balance(self):
        self.amount = int(self.amount + Budget.available_balance)
        print(f'{self.amount} naira is your balance in this category')

"""
# These are the categories of objects created in the class
"""
food = Budget(100000)
clothes = Budget(50000)
entertainment = Budget(20000) 

"""
# these are  the call fuction
"""
food.withdraw_funds()
food.deposit_funds()
food.transfer_funds()
food.check_balance()

clothes.withdraw_funds()
clothes.deposit_funds()
clothes.transfer_funds()
clothes.check_balance()

entertainment.withdraw_funds()
entertainment.deposit_funds()
entertainment.transfer_funds()
entertainment.check_balance()


