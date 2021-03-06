import uuid

from bankapp.bankaccount.AccountStatus import AccountStatus
from bankapp.bankaccount.AccountType import AccountType
from bankapp.bankaccount.CurrentAccount import CurrentAccount


class SavingsAccount(CurrentAccount):

    def __init__(self):
        super(SavingsAccount, self).__init__(AccountType.SAVINGS_ACCOUNT.value, uuid.uuid4().hex.upper(),
                                             AccountStatus.ACTIVE.name)
        self.balance = 12000
