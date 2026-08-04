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
# ObjectID: 0x8ab42f84008a74368745eccf8989a7b19740737cb300d9faa02bb984be2610f7
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: GasCoin
# Balance: 4100000000
# Version: 131
# Digest: BxAPGfGBtVtzWxiA2dDD3k3xwqQFNLwju5y8xZr8gubx
# BCS: AAGDAAAAAAAAACiKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ9wAJYfQAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA=
#
# ObjectID: 0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: GasCoin
# Balance: 1000000000
# Version: 131
# Digest: 88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU
# BCS: AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA=
#

# test_sign_stake_merge_split_coin
# --------------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#               "version": "131",
#               "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2",
#               "version": "134",
#               "digest": "ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty"
#             }
#           },
#           {
#             "Pure": "APIFKgEAAAA="
#           },
#           {
#             "Shared": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000000005",
#               "initial_shared_version": "1",
#               "mutable": true
#             }
#           },
#           {
#             "Pure": "hkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOc="
#           }
#         ],
#         "commands": [
#           {
#             "MergeCoins": {
#               "coin": {
#                 "Input": 0
#               },
#               "coins_to_merge": [
#                 {
#                   "Input": 1
#                 }
#               ]
#             }
#           },
#           {
#             "SplitCoins": {
#               "coin": {
#                 "Input": 0
#               },
#               "amounts": [
#                 {
#                   "Input": 2
#                 }
#               ]
#             }
#           },
#           {
#             "MoveCall": {
#               "package": "0x0000000000000000000000000000000000000000000000000000000000000003",
#               "module": "iota_system",
#               "function": "request_add_stake",
#               "type_arguments": [],
#               "arguments": [
#                 {
#                   "Input": 3
#                 },
#                 {
#                   "NestedResult": [
#                     1,
#                     0
#                   ]
#                 },
#                 {
#                   "Input": 4
#                 }
#               ]
#             }
#           }
#         ]
#       }
#     },
#     "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "gas_payment": {
#       "objects": [
#         {
#           "object_id": "0x8ab42f84008a74368745eccf8989a7b19740737cb300d9faa02bb984be2610f7",
#           "version": "131",
#           "digest": "BxAPGfGBtVtzWxiA2dDD3k3xwqQFNLwju5y8xZr8gubx"
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
def test_sign_stake_merge_split_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAFAQCZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnAQAe7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04oYAAAAAAAAAIMfrxsRDCzz35Y11q1PduRgCdN72Oxq1YZ+9twls29cSAAgA8gUqAQAAAAEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUBAAAAAAAAAAEAIIZMZRlYCUcyoSJxNM98q3WH8Fo5k5iARVJVP7wB26TnAwMBAAABAQEAAgEAAAEBAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMLaW90YV9zeXN0ZW0RcmVxdWVzdF9hZGRfc3Rha2UAAwEDAAMBAAAAAQQAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYCirQvhACKdDaHRezPiYmnsZdAc3yzANn6oCu5hL4mEPeDAAAAAAAAACCitmybZdloPrq9rSjiMBvdOYVLg8C1f6DTg978ICme40ifuMiIlnA6sfupU4s5KrZbF1Z0ExJB2oVmXdG2JPMPhgAAAAAAAAAgrfsbaZSu5LHsf4mMHVswUSkxaElmBc5tV7cPXMyJut0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ9wAJYfQAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
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

# test_sign_stake_split_merge_coin
# --------------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#               "version": "131",
#               "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#             }
#           },
#           {
#             "Pure": "APkClQAAAAA="
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2",
#               "version": "134",
#               "digest": "ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty"
#             }
#           },
#           {
#             "Shared": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000000005",
#               "initial_shared_version": "1",
#               "mutable": true
#             }
#           },
#           {
#             "Pure": "hkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOc="
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
#             "MergeCoins": {
#               "coin": {
#                 "NestedResult": [
#                   0,
#                   0
#                 ]
#               },
#               "coins_to_merge": [
#                 {
#                   "Input": 2
#                 }
#               ]
#             }
#           },
#           {
#             "MoveCall": {
#               "package": "0x0000000000000000000000000000000000000000000000000000000000000003",
#               "module": "iota_system",
#               "function": "request_add_stake",
#               "type_arguments": [],
#               "arguments": [
#                 {
#                   "Input": 3
#                 },
#                 {
#                   "NestedResult": [
#                     0,
#                     0
#                   ]
#                 },
#                 {
#                   "Input": 4
#                 }
#               ]
#             }
#           }
#         ]
#       }
#     },
#     "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "gas_payment": {
#       "objects": [
#         {
#           "object_id": "0x8ab42f84008a74368745eccf8989a7b19740737cb300d9faa02bb984be2610f7",
#           "version": "131",
#           "digest": "BxAPGfGBtVtzWxiA2dDD3k3xwqQFNLwju5y8xZr8gubx"
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
def test_sign_stake_split_merge_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAFAQCZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnAAgA+QKVAAAAAAEAHuxsMu82RnMx+3sIi0rLHORvc2NUMI4D/2zpE6QnNOKGAAAAAAAAACDH68bEQws89+WNdatT3bkYAnTe9jsatWGfvbcJbNvXEgEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUBAAAAAAAAAAEAIIZMZRlYCUcyoSJxNM98q3WH8Fo5k5iARVJVP7wB26TnAwIBAAABAQEAAwMAAAAAAQECAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwtpb3RhX3N5c3RlbRFyZXF1ZXN0X2FkZF9zdGFrZQADAQMAAwAAAAABBAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtgKKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ94MAAAAAAAAAIKK2bJtl2Wg+ur2tKOIwG905hUuDwLV/oNOD3vwgKZ7jSJ+4yIiWcDqx+6lTizkqtlsXVnQTEkHahWZd0bYk8w+GAAAAAAAAACCt+xtplK7ksex/iYwdWzBRKTFoSWYFzm1Xtw9czIm63Q9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    object_list = [
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ9wAJYfQAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
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

# test_sign_stake_mul_coin
# ------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#               "version": "131",
#               "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2",
#               "version": "134",
#               "digest": "ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty"
#             }
#           },
#           {
#             "Shared": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000000005",
#               "initial_shared_version": "1",
#               "mutable": true
#             }
#           },
#           {
#             "Pure": "AA=="
#           },
#           {
#             "Pure": "hkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOc="
#           }
#         ],
#         "commands": [
#           {
#             "MakeMoveVector": {
#               "type": null,
#               "elements": [
#                 {
#                   "Input": 0
#                 },
#                 {
#                   "Input": 1
#                 }
#               ]
#             }
#           },
#           {
#             "MoveCall": {
#               "package": "0x0000000000000000000000000000000000000000000000000000000000000003",
#               "module": "iota_system",
#               "function": "request_add_stake_mul_coin",
#               "type_arguments": [],
#               "arguments": [
#                 {
#                   "Input": 2
#                 },
#                 {
#                   "Result": 0
#                 },
#                 {
#                   "Input": 3
#                 },
#                 {
#                   "Input": 4
#                 }
#               ]
#             }
#           }
#         ]
#       }
#     },
#     "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "gas_payment": {
#       "objects": [
#         {
#           "object_id": "0x8ab42f84008a74368745eccf8989a7b19740737cb300d9faa02bb984be2610f7",
#           "version": "131",
#           "digest": "BxAPGfGBtVtzWxiA2dDD3k3xwqQFNLwju5y8xZr8gubx"
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
def test_sign_stake_mul_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAFAQCZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnAQAe7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04oYAAAAAAAAAIMfrxsRDCzz35Y11q1PduRgCdN72Oxq1YZ+9twls29cSAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQEAAAAAAAAAAQABAAAghkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOcCBQACAQAAAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADC2lvdGFfc3lzdGVtGnJlcXVlc3RfYWRkX3N0YWtlX211bF9jb2luAAQBAgACAAABAwABBAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtgKKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ94MAAAAAAAAAIKK2bJtl2Wg+ur2tKOIwG905hUuDwLV/oNOD3vwgKZ7jSJ+4yIiWcDqx+6lTizkqtlsXVnQTEkHahWZd0bYk8w+GAAAAAAAAACCt+xtplK7ksex/iYwdWzBRKTFoSWYFzm1Xtw9czIm63Q9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    object_list = [
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ9wAJYfQAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
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

# test_sign_stake_mul_coin_with_amount
# ------------------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#               "version": "131",
#               "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2",
#               "version": "134",
#               "digest": "ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty"
#             }
#           },
#           {
#             "Shared": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000000005",
#               "initial_shared_version": "1",
#               "mutable": true
#             }
#           },
#           {
#             "Pure": "AQCdlmsBAAAA"
#           },
#           {
#             "Pure": "hkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOc="
#           }
#         ],
#         "commands": [
#           {
#             "MakeMoveVector": {
#               "type": null,
#               "elements": [
#                 {
#                   "Input": 0
#                 },
#                 {
#                   "Input": 1
#                 }
#               ]
#             }
#           },
#           {
#             "MoveCall": {
#               "package": "0x0000000000000000000000000000000000000000000000000000000000000003",
#               "module": "iota_system",
#               "function": "request_add_stake_mul_coin",
#               "type_arguments": [],
#               "arguments": [
#                 {
#                   "Input": 2
#                 },
#                 {
#                   "Result": 0
#                 },
#                 {
#                   "Input": 3
#                 },
#                 {
#                   "Input": 4
#                 }
#               ]
#             }
#           }
#         ]
#       }
#     },
#     "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "gas_payment": {
#       "objects": [
#         {
#           "object_id": "0x8ab42f84008a74368745eccf8989a7b19740737cb300d9faa02bb984be2610f7",
#           "version": "131",
#           "digest": "BxAPGfGBtVtzWxiA2dDD3k3xwqQFNLwju5y8xZr8gubx"
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
def test_sign_stake_mul_coin_with_amount(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAFAQCZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnAQAe7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04oYAAAAAAAAAIMfrxsRDCzz35Y11q1PduRgCdN72Oxq1YZ+9twls29cSAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQEAAAAAAAAAAQAJAQCdlmsBAAAAACCGTGUZWAlHMqEicTTPfKt1h/BaOZOYgEVSVT+8Aduk5wIFAAIBAAABAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMLaW90YV9zeXN0ZW0acmVxdWVzdF9hZGRfc3Rha2VfbXVsX2NvaW4ABAECAAIAAAEDAAEEAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2Aoq0L4QAinQ2h0Xsz4mJp7GXQHN8swDZ+qAruYS+JhD3gwAAAAAAAAAgorZsm2XZaD66va0o4jAb3TmFS4PAtX+g04Pe/CApnuNIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzD4YAAAAAAAAAIK37G2mUruSx7H+JjB1bMFEpMWhJZgXObVe3D1zMibrdD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    object_list = [
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ9wAJYfQAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
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

# test_sign_stake_mul_coin_gas
# ----------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2",
#               "version": "134",
#               "digest": "ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty"
#             }
#           },
#           {
#             "Shared": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000000005",
#               "initial_shared_version": "1",
#               "mutable": true
#             }
#           },
#           {
#             "Pure": "AA=="
#           },
#           {
#             "Pure": "hkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOc="
#           }
#         ],
#         "commands": [
#           {
#             "MakeMoveVector": {
#               "type": null,
#               "elements": [
#                 "Gas",
#                 {
#                   "Input": 0
#                 }
#               ]
#             }
#           },
#           {
#             "MoveCall": {
#               "package": "0x0000000000000000000000000000000000000000000000000000000000000003",
#               "module": "iota_system",
#               "function": "request_add_stake_mul_coin",
#               "type_arguments": [],
#               "arguments": [
#                 {
#                   "Input": 1
#                 },
#                 {
#                   "Result": 0
#                 },
#                 {
#                   "Input": 2
#                 },
#                 {
#                   "Input": 3
#                 }
#               ]
#             }
#           }
#         ]
#       }
#     },
#     "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "gas_payment": {
#       "objects": [
#         {
#           "object_id": "0x8ab42f84008a74368745eccf8989a7b19740737cb300d9faa02bb984be2610f7",
#           "version": "131",
#           "digest": "BxAPGfGBtVtzWxiA2dDD3k3xwqQFNLwju5y8xZr8gubx"
#         },
#         {
#           "object_id": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#           "version": "134",
#           "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#         },
#         {
#           "object_id": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#           "version": "131",
#           "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#         }
#       ],
#       "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#       "price": "1000",
#       "budget": "1000000"
#     },
#     "expiration": "None"
#   }
# }
def test_sign_stake_mul_coin_gas(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAEAQAe7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04oYAAAAAAAAAIMfrxsRDCzz35Y11q1PduRgCdN72Oxq1YZ+9twls29cSAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQEAAAAAAAAAAQABAAAghkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOcCBQACAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwtpb3RhX3N5c3RlbRpyZXF1ZXN0X2FkZF9zdGFrZV9tdWxfY29pbgAEAQEAAgAAAQIAAQMAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYDirQvhACKdDaHRezPiYmnsZdAc3yzANn6oCu5hL4mEPeDAAAAAAAAACCitmybZdloPrq9rSjiMBvdOYVLg8C1f6DTg978ICme40ifuMiIlnA6sfupU4s5KrZbF1Z0ExJB2oVmXdG2JPMPhgAAAAAAAAAgrfsbaZSu5LHsf4mMHVswUSkxaElmBc5tV7cPXMyJut2Z6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    object_list = [
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ9wAJYfQAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
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

# test_sign_stake_mul_coin_gas_with_amount
# ----------------------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x1eec6c32ef36467331fb7b088b4acb1ce46f736354308e03ff6ce913a42734e2",
#               "version": "134",
#               "digest": "ETQev8rzu1uat1pq2aARETiFTH68S5X1mC3rsoaW3kty"
#             }
#           },
#           {
#             "Pure": "AC9oWQAAAAA="
#           },
#           {
#             "Shared": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000000005",
#               "initial_shared_version": "1",
#               "mutable": true
#             }
#           },
#           {
#             "Pure": "AQCUNXcAAAAA"
#           },
#           {
#             "Pure": "hkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOc="
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
#             "MakeMoveVector": {
#               "type": null,
#               "elements": [
#                 {
#                   "NestedResult": [
#                     0,
#                     0
#                   ]
#                 },
#                 {
#                   "Input": 0
#                 }
#               ]
#             }
#           },
#           {
#             "MoveCall": {
#               "package": "0x0000000000000000000000000000000000000000000000000000000000000003",
#               "module": "iota_system",
#               "function": "request_add_stake_mul_coin",
#               "type_arguments": [],
#               "arguments": [
#                 {
#                   "Input": 2
#                 },
#                 {
#                   "Result": 1
#                 },
#                 {
#                   "Input": 3
#                 },
#                 {
#                   "Input": 4
#                 }
#               ]
#             }
#           }
#         ]
#       }
#     },
#     "sender": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "gas_payment": {
#       "objects": [
#         {
#           "object_id": "0x8ab42f84008a74368745eccf8989a7b19740737cb300d9faa02bb984be2610f7",
#           "version": "131",
#           "digest": "BxAPGfGBtVtzWxiA2dDD3k3xwqQFNLwju5y8xZr8gubx"
#         },
#         {
#           "object_id": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#           "version": "134",
#           "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#         },
#         {
#           "object_id": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#           "version": "131",
#           "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#         }
#       ],
#       "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#       "price": "1000",
#       "budget": "1000000"
#     },
#     "expiration": "None"
#   }
# }
def test_sign_stake_mul_coin_gas_with_amount(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAFAQAe7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04oYAAAAAAAAAIMfrxsRDCzz35Y11q1PduRgCdN72Oxq1YZ+9twls29cSAAgAL2hZAAAAAAEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUBAAAAAAAAAAEACQEAlDV3AAAAAAAghkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOcDAgEAAAEBAQAFAAIDAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwtpb3RhX3N5c3RlbRpyZXF1ZXN0X2FkZF9zdGFrZV9tdWxfY29pbgAEAQIAAgEAAQMAAQQAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYDirQvhACKdDaHRezPiYmnsZdAc3yzANn6oCu5hL4mEPeDAAAAAAAAACCitmybZdloPrq9rSjiMBvdOYVLg8C1f6DTg978ICme40ifuMiIlnA6sfupU4s5KrZbF1Z0ExJB2oVmXdG2JPMPhgAAAAAAAAAgrfsbaZSu5LHsf4mMHVswUSkxaElmBc5tV7cPXMyJut2Z6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    object_list = [
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ9wAJYfQAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
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

