from brownie import FundMe, MockV3Aggregator, network, config
from web3 import Web3
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS



def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract

    # if we are on rinkeby -> use:
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print("👉👉👉  Deploying to live Network!!!!")
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    #fund_me = FundMe.deploy({"from": account}, publish_source=True) #👈🏻 True for verification
    else:
        print("👉👉👉 Deploying Mock!!!")
        deploy_mocks()
        #use the most recently deployed MockV3Aggregator:
        price_feed_address = MockV3Aggregator[-1].address # mock_aggregator.address
        

    # if on ganache -> use:
        #fund_me = FundMe.deploy("0x8A753747A1Fa494EC906cE90E9f37563A8AF630e", {"from": account}, publish_source=True)
    fund_me = FundMe.deploy(
    price_feed_address,
    {"from": account}, 
    publish_source=config["networks"][network.show_active()].get("verify"),
)
    print(f"🚀🕺💃 Contract deployed to {fund_me.address}")
    print(f"🙈 Check out at: https://rinkeby.etherscan.io/address/{fund_me.address}")
    return fund_me
        

def main():
    deploy_fund_me()