from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    #account = accounts[0] #10 accounts in total in Ganache
    #account = accounts.load("stupid-account")
    #account = accounts.add(os.getenv("PRIVATE_KEY"))
    #account = accounts.add(config["wallets"]["from_key"])
    account = get_account()
    print("👉👉👉 Account:", account)
    print("👉👉👉 Balance:", account.balance())
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    transaction = simple_storage.store(3, {"from": account})
    print("👉👉👉 ", transaction)
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print("👉👉👉 ", updated_stored_value)

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()