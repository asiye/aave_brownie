from brownie import network, config
from scripts.helpful_scripts import get_account
from scripts.get_weth import get_weth


def main():
    account = get_account()
    network_config = config["networks"][network.show_active()]
    erc20_address = network_config.get("weth_token")
    if network.show_active() in ["mainnet-fork"]:
        get_weth()
