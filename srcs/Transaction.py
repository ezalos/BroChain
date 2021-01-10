import Account

class Transaction():
    def __init__(self, Sender, Recipient, Amount, Signature = None):
        self.sender: Account = Sender
        self.recipient = Recipient
        self.amount = Amount
        self.signature = Signature

    def __str__(self):
        return("Sender: " + str(self.sender) + " Recipient: " + str(self.recipient) + " Amount: " + str(self.amount))