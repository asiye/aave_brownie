from brownie import interface, config, network
from scripts.helpful_scripts import get_account
from web3 import Web3


def main():
    get_weth()


def get_weth():
    account = get_account()
    network_config = config["networks"][network.show_active()]
    # weth_address = "0xd0a1e359811322d97991e03f863a0c30c2cf029c"
    # weth = interface.IWeth(weth_address)
    weth = interface.IWeth(network_config.get("weth_token"))
    transaction = weth.deposit({"from": account, "value": Web3.toWei(0.1, "ether")})
    transaction.wait(1)
    print("Get 0.1 WETH")
    return transaction
