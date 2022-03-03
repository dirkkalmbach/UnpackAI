from brownie import SimpleStorage, accounts, config

def test_deploy():
    # 📥 Arrange
    account = accounts[0]
    account = accounts.add(config["wallets"]["from_key"])
    print("### ACCOUNT ##############:", account)

    # 🎬 Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    
    # 🕵️‍♂️ Assert
    assert starting_value == expected

def test_updating_storage():
    # 📥 Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # 🎬 Act
    expected = 15
    simple_storage.store(expected, {"from": account})

    # 🕵️‍♂️ Assert
    assert expected == simple_storage.retrieve()