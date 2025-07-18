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
# ObjectID: 0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2
# Owner: Account Address ( 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6 )
# ObjectType: GasCoin
# Balance: 3000000000
# Version: 134
# Digest: ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty
# BCS: AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA=
#
# ObjectID: 0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f
# Owner: Account Address ( 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6 )
# ObjectType: GasCoin
# Balance: 2000000000
# Version: 134
# Digest: Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE
# BCS: AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA=
#
# ObjectID: 0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952
# Owner: Account Address ( 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6 )
# ObjectType: GasCoin
# Balance: 1000000000
# Version: 131
# Digest: 88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU
# BCS: AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA=
#

# test_sign_tx_iota_whole_gas_coin
# --------------------------------
# TransactionData:
# {
#   "version": 2,
#   "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#   "expiration": {
#     "None": true,
#     "$kind": "None"
#   },
#   "inputs": [
#     {
#       "Pure": {
#         "bytes": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#       },
#       "$kind": "Pure"
#     }
#   ],
#   "commands": [
#     {
#       "TransferObjects": {
#         "objects": [
#           {
#             "GasCoin": true,
#             "$kind": "GasCoin"
#           }
#         ],
#         "address": {
#           "Input": 0,
#           "$kind": "Input"
#         }
#       },
#       "$kind": "TransferObjects"
#     }
#   ],
#   "gasData": {
#     "budget": "1000000",
#     "price": "1000",
#     "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "payment": [
#       {
#         "objectId": "0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2",
#         "version": "134",
#         "digest": "ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty"
#       }
#     ]
#   }
# }
def test_sign_tx_iota_whole_gas_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAABACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAQABAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtgEe7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04oYAAAAAAAAAIMfrxsRDCzz35Y11q1PduRgCdN72Oxq1YZ+9twls29cSD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    object_list = [
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

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

# test_sign_tx_iota_whole_gas_plus_input_coin
# -------------------------------------------
# TransactionData:
# {
#   "version": 2,
#   "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#   "expiration": {
#     "None": true,
#     "$kind": "None"
#   },
#   "inputs": [
#     {
#       "Object": {
#         "ImmOrOwnedObject": {
#           "objectId": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#           "version": "131",
#           "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#         },
#         "$kind": "ImmOrOwnedObject"
#       },
#       "$kind": "Object"
#     },
#     {
#       "Pure": {
#         "bytes": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#       },
#       "$kind": "Pure"
#     }
#   ],
#   "commands": [
#     {
#       "TransferObjects": {
#         "objects": [
#           {
#             "GasCoin": true,
#             "$kind": "GasCoin"
#           },
#           {
#             "Input": 0,
#             "$kind": "Input"
#           }
#         ],
#         "address": {
#           "Input": 1,
#           "$kind": "Input"
#         }
#       },
#       "$kind": "TransferObjects"
#     }
#   ],
#   "gasData": {
#     "budget": "1000000",
#     "price": "1000",
#     "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "payment": [
#       {
#         "objectId": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#         "version": "134",
#         "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#       }
#     ]
#   }
# }
def test_sign_tx_iota_whole_gas_plus_input_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAACAQCZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAgABAAABAQAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtgFIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzD4YAAAAAAAAAIK37G2mUruSx7H+JjB1bMFEpMWhJZgXObVe3D1zMibrdD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    object_list = [
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

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

# test_sign_tx_iota_split_gas_plus_input_coin
# -------------------------------------------
# TransactionData:
# {
#   "version": 2,
#   "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#   "expiration": {
#     "None": true,
#     "$kind": "None"
#   },
#   "inputs": [
#     {
#       "Pure": {
#         "bytes": "AOQLVAIAAAA="
#       },
#       "$kind": "Pure"
#     },
#     {
#       "Object": {
#         "ImmOrOwnedObject": {
#           "objectId": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#           "version": "131",
#           "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#         },
#         "$kind": "ImmOrOwnedObject"
#       },
#       "$kind": "Object"
#     },
#     {
#       "Pure": {
#         "bytes": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#       },
#       "$kind": "Pure"
#     }
#   ],
#   "commands": [
#     {
#       "SplitCoins": {
#         "coin": {
#           "GasCoin": true,
#           "$kind": "GasCoin"
#         },
#         "amounts": [
#           {
#             "Input": 0,
#             "$kind": "Input"
#           }
#         ]
#       },
#       "$kind": "SplitCoins"
#     },
#     {
#       "TransferObjects": {
#         "objects": [
#           {
#             "NestedResult": [
#               0,
#               0
#             ],
#             "$kind": "NestedResult"
#           },
#           {
#             "Input": 1,
#             "$kind": "Input"
#           }
#         ],
#         "address": {
#           "Input": 2,
#           "$kind": "Input"
#         }
#       },
#       "$kind": "TransferObjects"
#     }
#   ],
#   "gasData": {
#     "budget": "1000000",
#     "price": "1000",
#     "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "payment": [
#       {
#         "objectId": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#         "version": "134",
#         "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#       }
#     ]
#   }
# }
def test_sign_tx_iota_split_gas_plus_input_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAADAAgA5AtUAgAAAAEAmesNGoYEyYrLsmCEgc9kfRtp1meW1SYTwtE0tO7wSVKDAAAAAAAAACBqCUCjjttDoknB+GD5sgWjUNoI031Etv0CRdGxKEzLZwAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4CAgABAQAAAQIDAAAAAAEBAAECAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AUifuMiIlnA6sfupU4s5KrZbF1Z0ExJB2oVmXdG2JPMPhgAAAAAAAAAgrfsbaZSu5LHsf4mMHVswUSkxaElmBc5tV7cPXMyJut0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

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

# test_sign_tx_iota_whole_input_coin
# ----------------------------------
# TransactionData:
# {
#   "version": 2,
#   "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#   "expiration": {
#     "None": true,
#     "$kind": "None"
#   },
#   "inputs": [
#     {
#       "Object": {
#         "ImmOrOwnedObject": {
#           "objectId": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#           "version": "131",
#           "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#         },
#         "$kind": "ImmOrOwnedObject"
#       },
#       "$kind": "Object"
#     },
#     {
#       "Pure": {
#         "bytes": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#       },
#       "$kind": "Pure"
#     }
#   ],
#   "commands": [
#     {
#       "TransferObjects": {
#         "objects": [
#           {
#             "Input": 0,
#             "$kind": "Input"
#           }
#         ],
#         "address": {
#           "Input": 1,
#           "$kind": "Input"
#         }
#       },
#       "$kind": "TransferObjects"
#     }
#   ],
#   "gasData": {
#     "budget": "1000000",
#     "price": "1000",
#     "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "payment": [
#       {
#         "objectId": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#         "version": "134",
#         "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#       }
#     ]
#   }
# }
def test_sign_tx_iota_whole_input_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAACAQCZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAQEAAAEBAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AUifuMiIlnA6sfupU4s5KrZbF1Z0ExJB2oVmXdG2JPMPhgAAAAAAAAAgrfsbaZSu5LHsf4mMHVswUSkxaElmBc5tV7cPXMyJut0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

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

# test_sign_tx_iota_whole_two_input_coin
# --------------------------------------
# TransactionData:
# {
#   "version": 2,
#   "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#   "expiration": {
#     "None": true,
#     "$kind": "None"
#   },
#   "inputs": [
#     {
#       "Object": {
#         "ImmOrOwnedObject": {
#           "objectId": "0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2",
#           "version": "134",
#           "digest": "ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty"
#         },
#         "$kind": "ImmOrOwnedObject"
#       },
#       "$kind": "Object"
#     },
#     {
#       "Object": {
#         "ImmOrOwnedObject": {
#           "objectId": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#           "version": "131",
#           "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#         },
#         "$kind": "ImmOrOwnedObject"
#       },
#       "$kind": "Object"
#     },
#     {
#       "Pure": {
#         "bytes": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#       },
#       "$kind": "Pure"
#     }
#   ],
#   "commands": [
#     {
#       "TransferObjects": {
#         "objects": [
#           {
#             "Input": 0,
#             "$kind": "Input"
#           },
#           {
#             "Input": 1,
#             "$kind": "Input"
#           }
#         ],
#         "address": {
#           "Input": 2,
#           "$kind": "Input"
#         }
#       },
#       "$kind": "TransferObjects"
#     }
#   ],
#   "gasData": {
#     "budget": "1000000",
#     "price": "1000",
#     "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "payment": [
#       {
#         "objectId": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#         "version": "134",
#         "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#       }
#     ]
#   }
# }
def test_sign_tx_iota_whole_two_input_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAADAQAe7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04oYAAAAAAAAAIMfrxsRDCzz35Y11q1PduRgCdN72Oxq1YZ+9twls29cSAQCZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAgEAAAEBAAECAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AUifuMiIlnA6sfupU4s5KrZbF1Z0ExJB2oVmXdG2JPMPhgAAAAAAAAAgrfsbaZSu5LHsf4mMHVswUSkxaElmBc5tV7cPXMyJut0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

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

# test_sign_tx_iota_merge_two_input_coin
# --------------------------------------
# TransactionData:
# {
#   "version": 2,
#   "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#   "expiration": {
#     "None": true,
#     "$kind": "None"
#   },
#   "inputs": [
#     {
#       "Object": {
#         "ImmOrOwnedObject": {
#           "objectId": "0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2",
#           "version": "134",
#           "digest": "ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty"
#         },
#         "$kind": "ImmOrOwnedObject"
#       },
#       "$kind": "Object"
#     },
#     {
#       "Object": {
#         "ImmOrOwnedObject": {
#           "objectId": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#           "version": "131",
#           "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#         },
#         "$kind": "ImmOrOwnedObject"
#       },
#       "$kind": "Object"
#     },
#     {
#       "Pure": {
#         "bytes": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#       },
#       "$kind": "Pure"
#     }
#   ],
#   "commands": [
#     {
#       "MergeCoins": {
#         "destination": {
#           "Input": 0,
#           "$kind": "Input"
#         },
#         "sources": [
#           {
#             "Input": 1,
#             "$kind": "Input"
#           }
#         ]
#       },
#       "$kind": "MergeCoins"
#     },
#     {
#       "TransferObjects": {
#         "objects": [
#           {
#             "Input": 0,
#             "$kind": "Input"
#           }
#         ],
#         "address": {
#           "Input": 2,
#           "$kind": "Input"
#         }
#       },
#       "$kind": "TransferObjects"
#     }
#   ],
#   "gasData": {
#     "budget": "1000000",
#     "price": "1000",
#     "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "payment": [
#       {
#         "objectId": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#         "version": "134",
#         "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#       }
#     ]
#   }
# }
def test_sign_tx_iota_merge_two_input_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAADAQAe7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04oYAAAAAAAAAIMfrxsRDCzz35Y11q1PduRgCdN72Oxq1YZ+9twls29cSAQCZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgIDAQAAAQEBAAEBAQAAAQIAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYBSJ+4yIiWcDqx+6lTizkqtlsXVnQTEkHahWZd0bYk8w+GAAAAAAAAACCt+xtplK7ksex/iYwdWzBRKTFoSWYFzm1Xtw9czIm63Q9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    object_list = [
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

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

