from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"the current entrance_fee is {entrance_fee}")
    print("funding")
    fund_me.fund({"from": account, "value": entrance_fee})
    balance = fund_me.getBalance()
    print(balance)
    print(entrance_fee)


def withdraw():
    # assign the last instance of contract to a variable
    fund_me = FundMe[-1]
    # assign account to get_account function
    account = get_account()
    fund_me.withdrawAll({"from": account})
    balance = fund_me.getBalance()
    print(balance)


def main():
    fund()
    withdraw()
