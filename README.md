# aave_brownie

brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.g.alchemy.com/v2/ksum25lCNpT-xWJnpeKg8jMeoRDhXHDA accounts=10 mnemonic=brownie port=8545

brownie run scripts/aave_borrow.py --network mainnet-fork
