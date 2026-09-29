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
# ObjectID: 0x0000000000000000000000000000000000000000000000000000000000d70007
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x25afeacdd3b0e757ae40aa4b9852261003e1dffeeb37d2c4f2904bb809807ac9::usdt0::USDT0>
# Balance: 7000000
# Version: 1
# Digest: 9S3ycBfezAmaU7WNFYCpaSZDobznyNjwGZ5TE19BrU5g
# BCS: AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXAAfAz2oAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#
# ObjectID: 0x0000000000000000000000000000000000000000000000000000000000d70015
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x25afeacdd3b0e757ae40aa4b9852261003e1dffeeb37d2c4f2904bb809807ac9::usdt0::USDT0>
# Balance: 15000000
# Version: 1
# Digest: 3295K7aYx7dSSkVdsNXbPhcJsz2B8e6uTghrkRSvCua9
# BCS: AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXABXA4eQAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#
# ObjectID: 0x0000000000000000000000000000000000000000000000000000000000d70028
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x25afeacdd3b0e757ae40aa4b9852261003e1dffeeb37d2c4f2904bb809807ac9::usdt0::USDT0>
# Balance: 28000000
# Version: 1
# Digest: CURDahXucTxjgrQGCTCRC3LvLhhfL51xtihtYXPjovu6
# BCS: AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXACgAP6sBAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#
# ObjectID: 0x13ab84f34a622442d5c0ba7f73c79139b0fd65c88adcbe26552970b1441ae64a
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: GasCoin
# Balance: 58985094000
# Version: 340540910
# Digest: DzJ7RSo7cQGWYZcn4bF886ZAavaCyAXvHxcbsHgKj8mz
# BCS: AAHuPUwUAAAAACgTq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSnAbybsNAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ILipVGikwTTXPy7YgiDBqyMru4odWun3YE0PP6h8KjZAsPUOAAAAAAA=
#

# test_sign_tx_usdt0_whole_coin
# -----------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70015",
#               "version": "1",
#               "digest": "3295K7aYx7dSSkVdsNXbPhcJsz2B8e6uTghrkRSvCua9"
#             }
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           }
#         ],
#         "commands": [
#           {
#             "TransferObjects": {
#               "objects": [
#                 {
#                   "Input": 0
#                 }
#               ],
#               "address": {
#                 "Input": 1
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
def test_sign_tx_usdt0_whole_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAACAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcAFQEAAAAAAAAAIB4CFZiDvJ7aYnV1yUYST93mb2/JUyJ1wkoAqHIwq8n6ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAQEAAAEBAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AROrhPNKYiRC1cC6f3PHkTmw/WXIity+JlUpcLFEGuZK7j1MFAAAAAAgwPmyRf1udkQLUaamZqlNudWNHQxliowgCPq4ttn3lD0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXABXA4eQAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAHuPUwUAAAAACgTq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSnAbybsNAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ILipVGikwTTXPy7YgiDBqyMru4odWun3YE0PP6h8KjZAsPUOAAAAAAA='),
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

# test_sign_tx_three_usdt0_whole_coin
# -----------------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70015",
#               "version": "1",
#               "digest": "3295K7aYx7dSSkVdsNXbPhcJsz2B8e6uTghrkRSvCua9"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70007",
#               "version": "1",
#               "digest": "9S3ycBfezAmaU7WNFYCpaSZDobznyNjwGZ5TE19BrU5g"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70028",
#               "version": "1",
#               "digest": "CURDahXucTxjgrQGCTCRC3LvLhhfL51xtihtYXPjovu6"
#             }
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           }
#         ],
#         "commands": [
#           {
#             "TransferObjects": {
#               "objects": [
#                 {
#                   "Input": 0
#                 },
#                 {
#                   "Input": 1
#                 },
#                 {
#                   "Input": 2
#                 }
#               ],
#               "address": {
#                 "Input": 3
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
def test_sign_tx_three_usdt0_whole_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAEAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcAFQEAAAAAAAAAIB4CFZiDvJ7aYnV1yUYST93mb2/JUyJ1wkoAqHIwq8n6AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcABwEAAAAAAAAAIH1IYW3/vNduID4Bpc36tGEIwWXr+AEf05RaGuZAWlejAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcAKAEAAAAAAAAAIKp2nsSRs2t1sPlnUHuNxEaIrO3JxLVy4AB9SeTLRifRACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAwEAAAEBAAECAAEDAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AROrhPNKYiRC1cC6f3PHkTmw/WXIity+JlUpcLFEGuZK7j1MFAAAAAAgwPmyRf1udkQLUaamZqlNudWNHQxliowgCPq4ttn3lD0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXABXA4eQAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXAAfAz2oAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXACgAP6sBAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAHuPUwUAAAAACgTq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSnAbybsNAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ILipVGikwTTXPy7YgiDBqyMru4odWun3YE0PP6h8KjZAsPUOAAAAAAA='),
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

# test_sign_tx_usdt0_split_coin
# -----------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70015",
#               "version": "1",
#               "digest": "3295K7aYx7dSSkVdsNXbPhcJsz2B8e6uTghrkRSvCua9"
#             }
#           },
#           {
#             "Pure": "oCUmAAAAAAA="
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
def test_sign_tx_usdt0_split_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAADAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcAFQEAAAAAAAAAIB4CFZiDvJ7aYnV1yUYST93mb2/JUyJ1wkoAqHIwq8n6AAigJSYAAAAAAAAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4CAgEAAAEBAQABAQMAAAAAAQIAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYBE6uE80piJELVwLp/c8eRObD9ZciK3L4mVSlwsUQa5kruPUwUAAAAACDA+bJF/W52RAtRpqZmqU251Y0dDGWKjCAI+ri22feUPQ9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    object_list = [
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXABXA4eQAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAHuPUwUAAAAACgTq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSnAbybsNAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ILipVGikwTTXPy7YgiDBqyMru4odWun3YE0PP6h8KjZAsPUOAAAAAAA='),
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

# test_sign_tx_usdt0_merge_three
# ------------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70015",
#               "version": "1",
#               "digest": "3295K7aYx7dSSkVdsNXbPhcJsz2B8e6uTghrkRSvCua9"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70007",
#               "version": "1",
#               "digest": "9S3ycBfezAmaU7WNFYCpaSZDobznyNjwGZ5TE19BrU5g"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70028",
#               "version": "1",
#               "digest": "CURDahXucTxjgrQGCTCRC3LvLhhfL51xtihtYXPjovu6"
#             }
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
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
#                 },
#                 {
#                   "Input": 2
#                 }
#               ]
#             }
#           },
#           {
#             "TransferObjects": {
#               "objects": [
#                 {
#                   "Input": 0
#                 }
#               ],
#               "address": {
#                 "Input": 3
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
def test_sign_tx_usdt0_merge_three(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAEAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcAFQEAAAAAAAAAIB4CFZiDvJ7aYnV1yUYST93mb2/JUyJ1wkoAqHIwq8n6AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcABwEAAAAAAAAAIH1IYW3/vNduID4Bpc36tGEIwWXr+AEf05RaGuZAWlejAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcAKAEAAAAAAAAAIKp2nsSRs2t1sPlnUHuNxEaIrO3JxLVy4AB9SeTLRifRACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgIDAQAAAgEBAAECAAEBAQAAAQMAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYBE6uE80piJELVwLp/c8eRObD9ZciK3L4mVSlwsUQa5kruPUwUAAAAACDA+bJF/W52RAtRpqZmqU251Y0dDGWKjCAI+ri22feUPQ9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    object_list = [
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXABXA4eQAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXAAfAz2oAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXACgAP6sBAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAHuPUwUAAAAACgTq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSnAbybsNAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ILipVGikwTTXPy7YgiDBqyMru4odWun3YE0PP6h8KjZAsPUOAAAAAAA='),
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

# test_sign_tx_usdt0_merge_split
# ------------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70015",
#               "version": "1",
#               "digest": "3295K7aYx7dSSkVdsNXbPhcJsz2B8e6uTghrkRSvCua9"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70007",
#               "version": "1",
#               "digest": "9S3ycBfezAmaU7WNFYCpaSZDobznyNjwGZ5TE19BrU5g"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70028",
#               "version": "1",
#               "digest": "CURDahXucTxjgrQGCTCRC3LvLhhfL51xtihtYXPjovu6"
#             }
#           },
#           {
#             "Pure": "QKWuAgAAAAA="
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
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
#                 },
#                 {
#                   "Input": 2
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
#                   "Input": 3
#                 }
#               ]
#             }
#           },
#           {
#             "TransferObjects": {
#               "objects": [
#                 {
#                   "NestedResult": [
#                     1,
#                     0
#                   ]
#                 }
#               ],
#               "address": {
#                 "Input": 4
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
def test_sign_tx_usdt0_merge_split(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAFAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcAFQEAAAAAAAAAIB4CFZiDvJ7aYnV1yUYST93mb2/JUyJ1wkoAqHIwq8n6AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcABwEAAAAAAAAAIH1IYW3/vNduID4Bpc36tGEIwWXr+AEf05RaGuZAWlejAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcAKAEAAAAAAAAAIKp2nsSRs2t1sPlnUHuNxEaIrO3JxLVy4AB9SeTLRifRAAhApa4CAAAAAAAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4DAwEAAAIBAQABAgACAQAAAQEDAAEBAwEAAAABBAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtgETq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSu49TBQAAAAAIMD5skX9bnZEC1GmpmapTbnVjR0MZYqMIAj6uLbZ95Q9D1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    object_list = [
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXABXA4eQAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXAAfAz2oAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXACgAP6sBAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAHuPUwUAAAAACgTq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSnAbybsNAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ILipVGikwTTXPy7YgiDBqyMru4odWun3YE0PP6h8KjZAsPUOAAAAAAA='),
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

# test_sign_tx_usdt0_transfer_two
# -------------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70015",
#               "version": "1",
#               "digest": "3295K7aYx7dSSkVdsNXbPhcJsz2B8e6uTghrkRSvCua9"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x0000000000000000000000000000000000000000000000000000000000d70007",
#               "version": "1",
#               "digest": "9S3ycBfezAmaU7WNFYCpaSZDobznyNjwGZ5TE19BrU5g"
#             }
#           },
#           {
#             "Pure": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#           }
#         ],
#         "commands": [
#           {
#             "TransferObjects": {
#               "objects": [
#                 {
#                   "Input": 0
#                 },
#                 {
#                   "Input": 1
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
def test_sign_tx_usdt0_transfer_two(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAADAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcAFQEAAAAAAAAAIB4CFZiDvJ7aYnV1yUYST93mb2/JUyJ1wkoAqHIwq8n6AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcABwEAAAAAAAAAIH1IYW3/vNduID4Bpc36tGEIwWXr+AEf05RaGuZAWlejACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAgEAAAEBAAECAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AROrhPNKYiRC1cC6f3PHkTmw/WXIity+JlUpcLFEGuZK7j1MFAAAAAAgwPmyRf1udkQLUaamZqlNudWNHQxliowgCPq4ttn3lD0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXABXA4eQAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAMHJa/qzdOw51euQKpLmFImEAPh3/7rN9LE8pBLuAmAeskFdXNkdDAFVVNEVDAAAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXAAfAz2oAAAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        base64.b64decode('AAHuPUwUAAAAACgTq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSnAbybsNAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ILipVGikwTTXPy7YgiDBqyMru4odWun3YE0PP6h8KjZAsPUOAAAAAAA='),
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

