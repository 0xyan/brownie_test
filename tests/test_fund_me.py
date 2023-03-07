from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest


def test_can_fund_withdraw():
    account = get_account()
    # add return the contract in the deploy.py file amd assign to a variable
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    # building a tx
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    # we wanna check that in the mapping the address balance is equal to entrance fee
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdrawAll({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


# to skip test if we're not on the local network
def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    account = get_account()
    fund_me = deploy_fund_me()
    # will give us a random account
    bad_actor = accounts.add()
    # IF WE WANT to test to pass when transaction reverts
    # import exceptions package
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdrawAll({"from": bad_actor})
