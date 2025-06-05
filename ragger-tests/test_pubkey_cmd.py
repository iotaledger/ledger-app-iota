import pytest

from application_client.client import Client, Errors
from contextlib import contextmanager
from ragger.bip import calculate_public_key_and_chaincode, CurveChoice
from ragger.error import ExceptionRAPDU
from ragger.navigator import NavInsID, NavIns
from utils import ROOT_SCREENSHOT_PATH, run_apdu_and_nav_tasks_concurrently


# In this test we check that the GET_PUBLIC_KEY works in non-confirmation mode
def test_get_public_key_no_confirm(backend):
    for path in [ "m/44'/4218'/0'/0'/0'" ]:
        client = Client(backend, use_block_protocol=True)
        _, public_key, _, address = client.get_public_key(path=path)

        assert public_key.hex() == "f0a9c612b7e69f1a114aa9189c1f32997d395d09d183368ddfd6d5dc49e34647"
        assert address.hex() == "1b3669e321893ee49c387a08fc251dbfff37cd2a981e6c473a5b2afde19d363e"


# In this test we check that the GET_PUBLIC_KEY works in confirmation mode
def test_get_public_key_confirm_accepted(backend, scenario_navigator, firmware, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/0'"

    def nav_task():
        scenario_navigator.address_review_approve()

    def apdu_task():
        return client.get_public_key_with_confirmation(path=path)

    def check_result(result):
        _, public_key, _, address = result
        assert public_key.hex() == "f0a9c612b7e69f1a114aa9189c1f32997d395d09d183368ddfd6d5dc49e34647"
        assert address.hex() == "1b3669e321893ee49c387a08fc251dbfff37cd2a981e6c473a5b2afde19d363e"

    run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)
