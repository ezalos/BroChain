class Account():
    def __init__(self, PubKey = None, PrivKey = None):
        self.pubKey = PubKey
        self.privKey = PrivKey

    def __str__(self):
        return ("Public Key: " + self.pubKey + ". Private Key: " + self.privKey)
