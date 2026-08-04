# THIS IS A GENERATED FILE
# DO NOT EDIT MANUALLY
# ----------------------------------------
# This file contains tests for the IOTA Ledger App.

import base64
import pytest

from application_client.client import Client
from contextlib import contextmanager
from ragger.error import ExceptionRAPDU
from ragger.navigator import NavIns, NavInsID
from utils import ROOT_SCREENSHOT_PATH, check_signature_validity, run_apdu_and_nav_tasks_concurrently

#
# Used Objects in these tests:
# ----------------------------
# ObjectID: 0x13ab84f34a622442d5c0ba7f73c79139b0fd65c88adcbe26552970b1441ae64a
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: GasCoin
# Balance: 58985094000
# Version: 340540910
# Digest: DzJ7RSo7cQGWYZcn4bF886ZAavaCyAXvHxcbsHgKj8mz
# BCS: AAHuPUwUAAAAACgTq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSnAbybsNAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ILipVGikwTTXPy7YgiDBqyMru4odWun3YE0PP6h8KjZAsPUOAAAAAAA=
#
# ObjectID: 0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: GasCoin
# Balance: 3000000000
# Version: 134
# Digest: ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty
# BCS: AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA=
#
# ObjectID: 0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: GasCoin
# Balance: 2000000000
# Version: 134
# Digest: Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE
# BCS: AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA=
#
# ObjectID: 0xbc6dd3caa189309096cf3183786c9bb8d97d89d0185ec236214ebd2cc14f1319
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x929065320c756b8a4a841deeed013bd748ee45a28629c4aaafc56d8948ebb081::vusd::VUSD>
# Balance: 15000000
# Version: 338244725
# Digest: 74sxR2hccsGSP9Shbeuhs3Fawx9k1fZcnfMfvsYGdg1A
# BCS: AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKLxt08qhiTCQls8xg3hsm7jZfYnQGF7CNiFOvSzBTxMZwOHkAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA==
#

# test_sign_tx_iota_transfer
# --------------------------
# Can sign a simple IOTA transfer transaction
#
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "AMqaOwAAAAA="
#           }
#         ],
#         "commands": [
#           {
#             "SplitCoins": {
#               "coin": "Gas",
#               "amounts": [
#                 {
#                   "Input": 1
#                 }
#               ]
#             }
#           },
#           {
#             "TransferObjects": {
#               "objects": [
#                 {
#                   "Result": 0
#                 }
#               ],
#               "address": {
#                 "Input": 0
#               }
#             }
#           }
#         ]
#       }
#     },
#     "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "gas_payment": {
#       "objects": [
#         {
#           "object_id": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#           "version": "134",
#           "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#         }
#       ],
#       "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#       "price": "1000",
#       "budget": "1000000"
#     },
#     "expiration": "None"
#   }
# }
def test_sign_tx_iota_transfer(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAACACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAIAMqaOwAAAAACAgABAQEAAQECAAABAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtgFIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzD4YAAAAAAAAAIK37G2mUruSx7H+JjB1bMFEpMWhJZgXObVe3D1zMibrdD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction)

    def nav_task():
        if device.is_nano:
            navigator.navigate_and_compare(
                instructions=[ NavInsID.RIGHT_CLICK # Review transfer
                               , NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK # From ...
                               , NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK # To ...
                               , NavInsID.RIGHT_CLICK # Amount
                               , NavInsID.RIGHT_CLICK # Max Gas
                               , NavInsID.BOTH_CLICK
                              ]
                , timeout=10
                , test_case_name=scenario_navigator.test_name
                , path=scenario_navigator.screenshot_path
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=False
            )
        else:
            scenario_navigator.review_approve()

    def check_result(result):
        assert len(result) == 64
        assert check_signature_validity(public_key, result, transaction)

    run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)

# test_sign_tx_blind_sign
# -----------------------
# Can blind sign an unknown transaction
#
def test_sign_tx_blind_sign(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAUCBVRufxJtL0AzGlQ7lghDm1gv0NEDAAAAAAAAACCA/avMkEmOfrhBOxQMQzSHHur6WoYgP9nP2wMvYE9J4ShK9DHPAytdhTJBNb+aMHPpINf1AgAAAAAAAAAgoG9BDBdegowkzuhMs72Vz/JcM/u9y2LGWW6OQjeE/+cC0IB0B1xwl/Nh6LRD4gdahSoikuiggHQHXHCX82HotEPiB1qFKiKS6AGAlpgAAAAAABZD+yV4/3GRxkMHmmLBzKjsJ1K8BVRufxJtL0AzGlQ7lghDm1gv0NEDAAAAAAAAACCA/avMkEmOfrhBOxQMQzSHHur6WoYgP9nP2wMvYE9J4QEAAAAAAAAALAEAAAAAAAA=')

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction)

    def nav_task():
        if device.is_nano:
            navigator.navigate_and_compare(
                instructions=[ NavInsID.BOTH_CLICK # Warning...
                               , NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK # Transaction Hash
                               , NavInsID.BOTH_CLICK]
                , timeout=10
                , path=scenario_navigator.screenshot_path
                , test_case_name=scenario_navigator.test_name
                , screen_change_before_first_instruction=False
                , screen_change_after_last_instruction=False
            )
        else:
            # Dismiss the "Blind signing ahead" screen
            navigator.navigate(
                instructions=[NavInsID.USE_CASE_CHOICE_REJECT]
                , timeout=20
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=True
            )
            # Below is similar to scenario_navigator.review_approve()
            # But screen_change_before_first_instruction=True causes hang
            navigator.navigate_until_text_and_compare(
                navigate_instruction=NavInsID.SWIPE_CENTER_TO_LEFT
                , validation_instructions=[NavInsID.USE_CASE_REVIEW_CONFIRM, NavInsID.USE_CASE_STATUS_DISMISS]
                , text="^Hold to sign$"
                , timeout=20
                , path=scenario_navigator.screenshot_path
                , test_case_name=scenario_navigator.test_name
                , screen_change_before_first_instruction=False
                , screen_change_after_last_instruction=True
            )

    def check_result(result):
        assert len(result) == 64
        assert check_signature_validity(public_key, result, transaction)

    with blind_sign_enabled(device, navigator):
        run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)

# test_sign_tx_refused
# --------------------
# The test will ask for a transaction signature that will be refused on screen
# Same Tx as test_sign_tx_iota_transfer, but with a different navigation flow
#
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "AMqaOwAAAAA="
#           }
#         ],
#         "commands": [
#           {
#             "SplitCoins": {
#               "coin": "Gas",
#               "amounts": [
#                 {
#                   "Input": 1
#                 }
#               ]
#             }
#           },
#           {
#             "TransferObjects": {
#               "objects": [
#                 {
#                   "Result": 0
#                 }
#               ],
#               "address": {
#                 "Input": 0
#               }
#             }
#           }
#         ]
#       }
#     },
#     "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "gas_payment": {
#       "objects": [
#         {
#           "object_id": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#           "version": "134",
#           "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#         }
#       ],
#       "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#       "price": "1000",
#       "budget": "1000000"
#     },
#     "expiration": "None"
#   }
# }
def test_sign_tx_refused(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAACACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAIAMqaOwAAAAACAgABAQEAAQECAAABAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtgFIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzD4YAAAAAAAAAIK37G2mUruSx7H+JjB1bMFEpMWhJZgXObVe3D1zMibrdD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction)

    def nav_task():
        if device.is_nano:
            navigator.navigate_and_compare(
                instructions=[ NavInsID.RIGHT_CLICK # Transfer IOTA
                               , NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK # From ...
                               , NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK # To ...
                               , NavInsID.RIGHT_CLICK # Amount
                               , NavInsID.RIGHT_CLICK # Max Gas
                               , NavInsID.RIGHT_CLICK # Confirm
                               , NavInsID.BOTH_CLICK
                              ]
                , timeout=10
                , test_case_name=scenario_navigator.test_name
                , path=scenario_navigator.screenshot_path
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=False
            )
        else:
            scenario_navigator.review_reject()

    def check_result(result):
        pytest.fail('should not happen')

    with pytest.raises(ExceptionRAPDU) as e:
        run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)

    assert len(e.value.data) == 0

# test_sign_tx_non_iota_transfer_rejected
# ---------------------------------------
# Should reject signing a non-IOTA coin transaction, if blind signing is not enabled
#
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0xbc6dd3caa189309096cf3183786c9bb8d97d89d0185ec236214ebd2cc14f1319",
#               "version": "338244725",
#               "digest": "74sxR2hccsGSP9Shbeuhs3Fawx9k1fZcnfMfvsYGdg1A"
#             }
#           },
#           {
#             "Pure": "QEIPAAAAAAA="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           }
#         ],
#         "commands": [
#           {
#             "SplitCoins": {
#               "coin": {
#                 "Input": 0
#               },
#               "amounts": [
#                 {
#                   "Input": 1
#                 }
#               ]
#             }
#           },
#           {
#             "TransferObjects": {
#               "objects": [
#                 {
#                   "NestedResult": [
#                     0,
#                     0
#                   ]
#                 }
#               ],
#               "address": {
#                 "Input": 2
#               }
#             }
#           }
#         ]
#       }
#     },
#     "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "gas_payment": {
#       "objects": [
#         {
#           "object_id": "0x13ab84f34a622442d5c0ba7f73c79139b0fd65c88adcbe26552970b1441ae64a",
#           "version": "340540910",
#           "digest": "DzJ7RSo7cQGWYZcn4bF886ZAavaCyAXvHxcbsHgKj8mz"
#         }
#       ],
#       "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#       "price": "1000",
#       "budget": "1000000"
#     },
#     "expiration": "None"
#   }
# }
def test_sign_tx_non_iota_transfer_rejected(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAADAQC8bdPKoYkwkJbPMYN4bJu42X2J0BhewjYhTr0swU8TGXU0KRQAAAAAIFoker34YuFsSnGq+bXwfYo91Y8ZNApPdPgrfBte2xN1AAhAQg8AAAAAAAAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4CAgEAAAEBAQABAQMAAAAAAQIAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYBE6uE80piJELVwLp/c8eRObD9ZciK3L4mVSlwsUQa5kruPUwUAAAAACDA+bJF/W52RAtRpqZmqU251Y0dDGWKjCAI+ri22feUPQ9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction)

    def nav_task():
        if device.is_nano:
            navigator.navigate_and_compare(
                instructions=[NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK, NavInsID.BOTH_CLICK]
                , timeout=10
                , test_case_name=scenario_navigator.test_name
                , path=scenario_navigator.screenshot_path
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=True
            )
        else:
            # Dismiss the "Enable Blind signing" screen
            navigator.navigate_and_compare(
                instructions=[NavInsID.USE_CASE_CHOICE_REJECT]
                , test_case_name=scenario_navigator.test_name
                , path=scenario_navigator.screenshot_path
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=False
            )

    def check_result(result):
        pytest.fail('should not happen')

    with pytest.raises(ExceptionRAPDU) as e:
        run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)

    assert len(e.value.data) == 0

# test_sign_tx_unknown_tx_rejected
# --------------------------------
# Should reject signing an unknown transaction, if blind signing is not enabled
#
def test_sign_tx_unknown_tx_rejected(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAUCBVRufxJtL0AzGlQ7lghDm1gv0NEDAAAAAAAAACCA/avMkEmOfrhBOxQMQzSHHur6WoYgP9nP2wMvYE9J4ShK9DHPAytdhTJBNb+aMHPpINf1AgAAAAAAAAAgoG9BDBdegowkzuhMs72Vz/JcM/u9y2LGWW6OQjeE/+cC0IB0B1xwl/Nh6LRD4gdahSoikuiggHQHXHCX82HotEPiB1qFKiKS6AGAlpgAAAAAABZD+yV4/3GRxkMHmmLBzKjsJ1K8BVRufxJtL0AzGlQ7lghDm1gv0NEDAAAAAAAAACCA/avMkEmOfrhBOxQMQzSHHur6WoYgP9nP2wMvYE9J4QEAAAAAAAAALAEAAAAAAAA=')

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction)

    def nav_task():
        if device.is_nano:
            navigator.navigate_and_compare(
                instructions=[NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK, NavInsID.BOTH_CLICK]
                , timeout=10
                , test_case_name=scenario_navigator.test_name
                , path=scenario_navigator.screenshot_path
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=True
            )
        else:
            # Dismiss the "Enable Blind signing" screen
            navigator.navigate_and_compare(
                instructions=[NavInsID.USE_CASE_CHOICE_REJECT]
                , test_case_name=scenario_navigator.test_name
                , path=scenario_navigator.screenshot_path
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=False
            )

    def check_result(result):
        pytest.fail('should not happen')

    with pytest.raises(ExceptionRAPDU) as e:
        run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)

    assert len(e.value.data) == 0

# test_sign_tx_blind_sign_big_transfer_tx
# ---------------------------------------
# can blind sign a transfer transaction with too many inputs
#
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           }
#         ],
#         "commands": [
#           {
#             "TransferObjects": {
#               "objects": [
#                 "Gas"
#               ],
#               "address": {
#                 "Input": 0
#               }
#             }
#           }
#         ]
#       }
#     },
#     "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "gas_payment": {
#       "objects": [
#         {
#           "object_id": "0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2",
#           "version": "134",
#           "digest": "ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty"
#         },
#         {
#           "object_id": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#           "version": "134",
#           "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#         }
#       ],
#       "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#       "price": "1000",
#       "budget": "1000000"
#     },
#     "expiration": "None"
#   }
# }
def test_sign_tx_blind_sign_big_transfer_tx(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAA2ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4AIBs2aeMhiT7knDh6CPwlHb//N80qmB5sRzpbKv3hnTY+AQEBAAEAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2Ah7sbDLvNkZzMft7CItKyxzkb3NjVDCOA/9s6ROkJzTihgAAAAAAAAAgx+vGxEMLPPfljXWrU925GAJ03vY7GrVhn723CWzb1xJIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzD4YAAAAAAAAAIK37G2mUruSx7H+JjB1bMFEpMWhJZgXObVe3D1zMibrdD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    object_list = [
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

    def nav_task():
        if device.is_nano:
            navigator.navigate_and_compare(
                instructions=[ NavInsID.BOTH_CLICK # Warning...
                               , NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK # Transaction Hash
                               , NavInsID.BOTH_CLICK]
                , timeout=10
                , path=scenario_navigator.screenshot_path
                , test_case_name=scenario_navigator.test_name
                , screen_change_before_first_instruction=False
                , screen_change_after_last_instruction=False
            )
        else:
            # Dismiss the "Blind signing ahead" screen
            navigator.navigate(
                instructions=[NavInsID.USE_CASE_CHOICE_REJECT]
                , timeout=20
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=True
            )
            # Below is similar to scenario_navigator.review_approve()
            # But screen_change_before_first_instruction=True causes hang
            navigator.navigate_until_text_and_compare(
                navigate_instruction=NavInsID.SWIPE_CENTER_TO_LEFT
                , validation_instructions=[NavInsID.USE_CASE_REVIEW_CONFIRM, NavInsID.USE_CASE_STATUS_DISMISS]
                , text="^Hold to sign$"
                , timeout=20
                , path=scenario_navigator.screenshot_path
                , test_case_name=scenario_navigator.test_name
                , screen_change_before_first_instruction=False
                , screen_change_after_last_instruction=True
            )

    def check_result(result):
        assert len(result) == 64
        assert check_signature_validity(public_key, result, transaction)

    with blind_sign_enabled(device, navigator):
        run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)

@contextmanager
def blind_sign_enabled(device, navigator):
    toggle_blind_sign(device, navigator)
    try:
        yield
    except:
        # Don't re-enable if we hit an exception
        raise
    else:
        toggle_blind_sign(device, navigator)

def toggle_blind_sign(device, navigator):
    if device.is_nano:
        navigator.navigate(
            instructions=[NavInsID.RIGHT_CLICK, NavInsID.BOTH_CLICK, NavInsID.BOTH_CLICK, NavInsID.RIGHT_CLICK, NavInsID.BOTH_CLICK, NavInsID.LEFT_CLICK]
            , timeout=10
            , screen_change_before_first_instruction=False
        )
    else:
        navigator.navigate([NavInsID.USE_CASE_HOME_SETTINGS,
                            NavIns(NavInsID.TOUCH, (200, 113)),
                            NavInsID.USE_CASE_SUB_SETTINGS_EXIT],
                            timeout=10,
                            screen_change_before_first_instruction=False,
                            screen_change_after_last_instruction=False)
    