# from Account import Account
# from Transaction import Transaction
from BlockChain import *

a = Account("Lol", "Bro")
b = Account("Yo", "Bitches")
print(a)

t1 = Transaction(a, b, 10)
t2 = Transaction(b, a, 1)
t3 = Transaction(b, a, 4)
print(t1)


b1 = Block([t1, t2], "init", "nonce")
b2 = Block([t3], "b1_hash", "nonce2")

bc = BlockChain()
