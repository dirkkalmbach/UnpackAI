from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1]
    print("👉👉👉 Last contract: ", simple_storage)
    print("👉👉👉 Last contracts value: ", simple_storage.retrieve())
    

def main():
    read_contract()