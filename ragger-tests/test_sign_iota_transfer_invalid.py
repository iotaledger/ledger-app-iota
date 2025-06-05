import base64
import pytest

from application_client.client import Client
from contextlib import contextmanager
from ragger.error import ExceptionRAPDU
from ragger.navigator import NavInsID
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
# ObjectID: 0x2b47a0dca64a7c783224e27125e5a9d337d0a6595bace34d65e4c7bbc0a71ee3
# Owner: Account Address ( 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6 )
# ObjectType: 0x0000000000000000000000000000000000000000000000000000000000000003::staking_pool::StakedIota
# Version: 2301
# Digest: 61tD4mkae65faomciPtSo1xvxZ7SjrdpWvFfauTLJBPH
# BCS: AAL9CAAAAAAAAFArR6Dcpkp8eDIk4nEl5anTN9CmWVus401l5Me7wKce43c1muAQnbWuHwT18qo25ZHVvQhRRYmrDZMmRzf8bQl0/AgAAAAAAAAAERAkAQAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiBG3FEWr6ouKxc3xTULBPfGkpGRFsFoOzuwIg0NBJhPnTCZEwAAAAAA
#
# ObjectID: 0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f
# Owner: Account Address ( 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6 )
# ObjectType: GasCoin
# Balance: 2000000000
# Version: 134
# Digest: Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE
# BCS: AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA=
#
# ObjectID: 0x8ab42f84008a74368745eccf8989a7b19740737cb300d9faa02bb984be2610f7
# Owner: Account Address ( 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6 )
# ObjectType: GasCoin
# Balance: 4100000000
# Version: 131
# Digest: BxAPGfGBtVtzWxiA2dDD3k3xwqQFNLwju5y8xZr8gubx
# BCS: AAGDAAAAAAAAACiKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ9wAJYfQAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA=
#
# ObjectID: 0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952
# Owner: Account Address ( 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6 )
# ObjectType: GasCoin
# Balance: 1000000000
# Version: 131
# Digest: 88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU
# BCS: AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA=
#

# test_sign_tx_iota_multi_recipient
# ---------------------------------
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
#       "Pure": {
#         "bytes": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
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
#         "bytes": "hkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOc="
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
#     },
#     {
#       "TransferObjects": {
#         "objects": [
#           {
#             "Input": 2,
#             "$kind": "Input"
#           }
#         ],
#         "address": {
#           "Input": 3,
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

def test_sign_tx_iota_multi_recipient(backend, scenario_navigator, firmware, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAEAQAe7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04oYAAAAAAAAAIMfrxsRDCzz35Y11q1PduRgCdN72Oxq1YZ+9twls29cSACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEAmesNGoYEyYrLsmCEgc9kfRtp1meW1SYTwtE0tO7wSVKDAAAAAAAAACBqCUCjjttDoknB+GD5sgWjUNoI031Etv0CRdGxKEzLZwAghkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOcCAQEBAAABAQABAQECAAEDAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AUifuMiIlnA6sfupU4s5KrZbF1Z0ExJB2oVmXdG2JPMPhgAAAAAAAAAgrfsbaZSu5LHsf4mMHVswUSkxaElmBc5tV7cPXMyJut0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

    def nav_task():
        if firmware.device.startswith("nano"):
            navigator.navigate_and_compare(
                instructions=[NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK]
                , timeout=10
                , test_case_name=scenario_navigator.test_name
                , path=scenario_navigator.screenshot_path
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=False
            )
        else:
            # Dismiss the "Enable Blind signing" screen
            navigator.navigate([NavInsID.USE_CASE_CHOICE_REJECT],
                            screen_change_before_first_instruction=False,
                            screen_change_after_last_instruction=False)

    def check_result(result):
        pytest.fail('should not happen')

    with pytest.raises(ExceptionRAPDU) as e:
        run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)

    assert len(e.value.data) == 0
    
# test_sign_tx_iota_whole_gas_coin_missing_object
# -----------------------------------------------
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
#         "objectId": "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
#         "version": "1234",
#         "digest": "4vJ9JU1bJJE96FWSJKvHsmmFADCg4gpZQff4P3bkLKi"
#       }
#     ]
#   }
# }

def test_sign_tx_iota_whole_gas_coin_missing_object(backend, scenario_navigator, firmware, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAABACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAQABAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtgESNFZ4kKvN7xI0VniQq83vEjRWeJCrze8SNFZ4kKvN79IEAAAAAAAAIAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    object_list = [
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

    def nav_task():
        if firmware.device.startswith("nano"):
            navigator.navigate_and_compare(
                instructions=[NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK]
                , timeout=10
                , test_case_name=scenario_navigator.test_name
                , path=scenario_navigator.screenshot_path
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=False
            )
        else:
            # Dismiss the "Enable Blind signing" screen
            navigator.navigate([NavInsID.USE_CASE_CHOICE_REJECT],
                            screen_change_before_first_instruction=False,
                            screen_change_after_last_instruction=False)

    def check_result(result):
        pytest.fail('should not happen')

    with pytest.raises(ExceptionRAPDU) as e:
        run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)

    assert len(e.value.data) == 0
    
# test_sign_tx_iota_whole_input_coin_missing_object
# -------------------------------------------------
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
#           "objectId": "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
#           "version": "1234",
#           "digest": "4vJ9JU1bJJE96FWSJKvHsmmFADCg4gpZQff4P3bkLKi"
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
#       },
#       {
#         "objectId": "0x99eb0d1a8604c98acbb2608481cf647d1b69d66796d52613c2d134b4eef04952",
#         "version": "131",
#         "digest": "88vQ8xTH3uNtRUaj8t3Y39UKgvZicxsK2ZoDYFGJ3uwU"
#       }
#     ]
#   }
# }

def test_sign_tx_iota_whole_input_coin_missing_object(backend, scenario_navigator, firmware, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAACAQASNFZ4kKvN7xI0VniQq83vEjRWeJCrze8SNFZ4kKvN79IEAAAAAAAAIAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAQEAAAEBAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AkifuMiIlnA6sfupU4s5KrZbF1Z0ExJB2oVmXdG2JPMPhgAAAAAAAAAgrfsbaZSu5LHsf4mMHVswUSkxaElmBc5tV7cPXMyJut2Z6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    object_list = [
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

    def nav_task():
        if firmware.device.startswith("nano"):
            navigator.navigate_and_compare(
                instructions=[NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK]
                , timeout=10
                , test_case_name=scenario_navigator.test_name
                , path=scenario_navigator.screenshot_path
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=False
            )
        else:
            # Dismiss the "Enable Blind signing" screen
            navigator.navigate([NavInsID.USE_CASE_CHOICE_REJECT],
                            screen_change_before_first_instruction=False,
                            screen_change_after_last_instruction=False)

    def check_result(result):
        pytest.fail('should not happen')

    with pytest.raises(ExceptionRAPDU) as e:
        run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)

    assert len(e.value.data) == 0
    
# test_sign_tx_iota_and_move_call
# -------------------------------
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
#     },
#     {
#       "Object": {
#         "SharedObject": {
#           "objectId": "0x0000000000000000000000000000000000000000000000000000000000000005",
#           "initialSharedVersion": "1",
#           "mutable": true
#         },
#         "$kind": "SharedObject"
#       },
#       "$kind": "Object"
#     },
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
#       "Pure": {
#         "bytes": "hkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOc="
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
#     },
#     {
#       "MoveCall": {
#         "package": "0x0000000000000000000000000000000000000000000000000000000000000003",
#         "module": "iota_system",
#         "function": "request_add_stake",
#         "typeArguments": [],
#         "arguments": [
#           {
#             "Input": 2,
#             "$kind": "Input"
#           },
#           {
#             "Input": 3,
#             "$kind": "Input"
#           },
#           {
#             "Input": 4,
#             "$kind": "Input"
#           }
#         ]
#       },
#       "$kind": "MoveCall"
#     }
#   ],
#   "gasData": {
#     "budget": "1000000",
#     "price": "1000",
#     "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "payment": [
#       {
#         "objectId": "0x8ab42f84008a74368745eccf8989a7b19740737cb300d9faa02bb984be2610f7",
#         "version": "131",
#         "digest": "BxAPGfGBtVtzWxiA2dDD3k3xwqQFNLwju5y8xZr8gubx"
#       },
#       {
#         "objectId": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#         "version": "134",
#         "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#       }
#     ]
#   }
# }

def test_sign_tx_iota_and_move_call(backend, scenario_navigator, firmware, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAFAQCZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUoMAAAAAAAAAIGoJQKOO20OiScH4YPmyBaNQ2gjTfUS2/QJF0bEoTMtnACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUBAAAAAAAAAAEBAB7sbDLvNkZzMft7CItKyxzkb3NjVDCOA/9s6ROkJzTihgAAAAAAAAAgx+vGxEMLPPfljXWrU925GAJ03vY7GrVhn723CWzb1xIAIIZMZRlYCUcyoSJxNM98q3WH8Fo5k5iARVJVP7wB26TnAgEBAQAAAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADC2lvdGFfc3lzdGVtEXJlcXVlc3RfYWRkX3N0YWtlAAMBAgABAwABBAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtgKKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ94MAAAAAAAAAIKK2bJtl2Wg+ur2tKOIwG905hUuDwLV/oNOD3vwgKZ7jSJ+4yIiWcDqx+6lTizkqtlsXVnQTEkHahWZd0bYk8w+GAAAAAAAAACCt+xtplK7ksex/iYwdWzBRKTFoSWYFzm1Xtw9czIm63Q9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    object_list = [
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ9wAJYfQAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

    def nav_task():
        if firmware.device.startswith("nano"):
            navigator.navigate_and_compare(
                instructions=[NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK]
                , timeout=10
                , test_case_name=scenario_navigator.test_name
                , path=scenario_navigator.screenshot_path
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=False
            )
        else:
            # Dismiss the "Enable Blind signing" screen
            navigator.navigate([NavInsID.USE_CASE_CHOICE_REJECT],
                            screen_change_before_first_instruction=False,
                            screen_change_after_last_instruction=False)

    def check_result(result):
        pytest.fail('should not happen')

    with pytest.raises(ExceptionRAPDU) as e:
        run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)

    assert len(e.value.data) == 0
    
# test_sign_multiple_move_call
# ----------------------------
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
#         "SharedObject": {
#           "objectId": "0x0000000000000000000000000000000000000000000000000000000000000005",
#           "initialSharedVersion": "1",
#           "mutable": true
#         },
#         "$kind": "SharedObject"
#       },
#       "$kind": "Object"
#     },
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
#       "Pure": {
#         "bytes": "hkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOc="
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
#         "bytes": "hkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOc="
#       },
#       "$kind": "Pure"
#     }
#   ],
#   "commands": [
#     {
#       "MoveCall": {
#         "package": "0x0000000000000000000000000000000000000000000000000000000000000003",
#         "module": "iota_system",
#         "function": "request_add_stake",
#         "typeArguments": [],
#         "arguments": [
#           {
#             "Input": 0,
#             "$kind": "Input"
#           },
#           {
#             "Input": 1,
#             "$kind": "Input"
#           },
#           {
#             "Input": 2,
#             "$kind": "Input"
#           }
#         ]
#       },
#       "$kind": "MoveCall"
#     },
#     {
#       "MoveCall": {
#         "package": "0x0000000000000000000000000000000000000000000000000000000000000003",
#         "module": "iota_system",
#         "function": "request_add_stake",
#         "typeArguments": [],
#         "arguments": [
#           {
#             "Input": 0,
#             "$kind": "Input"
#           },
#           {
#             "Input": 3,
#             "$kind": "Input"
#           },
#           {
#             "Input": 4,
#             "$kind": "Input"
#           }
#         ]
#       },
#       "$kind": "MoveCall"
#     }
#   ],
#   "gasData": {
#     "budget": "1000000",
#     "price": "1000",
#     "owner": "0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6",
#     "payment": [
#       {
#         "objectId": "0x8ab42f84008a74368745eccf8989a7b19740737cb300d9faa02bb984be2610f7",
#         "version": "131",
#         "digest": "BxAPGfGBtVtzWxiA2dDD3k3xwqQFNLwju5y8xZr8gubx"
#       },
#       {
#         "objectId": "0x489fb8c88896703ab1fba9538b392ab65b175674131241da85665dd1b624f30f",
#         "version": "134",
#         "digest": "Ci9cW4XFvH1PgyyAyx1b3cDRQLuZAPax2F5A5ticzvTE"
#       }
#     ]
#   }
# }

def test_sign_multiple_move_call(backend, scenario_navigator, firmware, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAFAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQEAAAAAAAAAAQEAHuxsMu82RnMx+3sIi0rLHORvc2NUMI4D/2zpE6QnNOKGAAAAAAAAACDH68bEQws89+WNdatT3bkYAnTe9jsatWGfvbcJbNvXEgAghkxlGVgJRzKhInE0z3yrdYfwWjmTmIBFUlU/vAHbpOcBAJnrDRqGBMmKy7JghIHPZH0badZnltUmE8LRNLTu8ElSgwAAAAAAAAAgaglAo47bQ6JJwfhg+bIFo1DaCNN9RLb9AkXRsShMy2cAIIZMZRlYCUcyoSJxNM98q3WH8Fo5k5iARVJVP7wB26TnAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwtpb3RhX3N5c3RlbRFyZXF1ZXN0X2FkZF9zdGFrZQADAQAAAQEAAQIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADC2lvdGFfc3lzdGVtEXJlcXVlc3RfYWRkX3N0YWtlAAMBAAABAwABBAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtgKKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ94MAAAAAAAAAIKK2bJtl2Wg+ur2tKOIwG905hUuDwLV/oNOD3vwgKZ7jSJ+4yIiWcDqx+6lTizkqtlsXVnQTEkHahWZd0bYk8w+GAAAAAAAAACCt+xtplK7ksex/iYwdWzBRKTFoSWYFzm1Xtw9czIm63Q9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    object_list = [
        base64.b64decode('AAGGAAAAAAAAACge7Gwy7zZGczH7ewiLSssc5G9zY1QwjgP/bOkTpCc04gBe0LIAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiZ6w0ahgTJisuyYISBz2R9G2nWZ5bVJhPC0TS07vBJUgDKmjsAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGDAAAAAAAAACiKtC+EAIp0NodF7M+Jiaexl0BzfLMA2fqgK7mEviYQ9wAJYfQAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ICTpVSt3otatS3dUSvIsQDY5vlLHxTgzrgD1+f7Tu1OusPUOAAAAAAA='),
        base64.b64decode('AAGGAAAAAAAAAChIn7jIiJZwOrH7qVOLOSq2WxdWdBMSQdqFZl3RtiTzDwCUNXcAAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2IKfnmT3SmOEPs3P7cIufkAW+GWPG8HSyArvnp8+dddcXsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

    def nav_task():
        if firmware.device.startswith("nano"):
            navigator.navigate_and_compare(
                instructions=[NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK]
                , timeout=10
                , test_case_name=scenario_navigator.test_name
                , path=scenario_navigator.screenshot_path
                , screen_change_before_first_instruction=True
                , screen_change_after_last_instruction=False
            )
        else:
            # Dismiss the "Enable Blind signing" screen
            navigator.navigate([NavInsID.USE_CASE_CHOICE_REJECT],
                            screen_change_before_first_instruction=False,
                            screen_change_after_last_instruction=False)

    def check_result(result):
        pytest.fail('should not happen')

    with pytest.raises(ExceptionRAPDU) as e:
        run_apdu_and_nav_tasks_concurrently(apdu_task, nav_task, check_result)

    assert len(e.value.data) == 0
    
