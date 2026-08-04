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
# ObjectID: 0x16cd400cb71dfaacd5027d18e3770c39558481502411b175c1ba44c400b294c8
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x929065320c756b8a4a841deeed013bd748ee45a28629c4aaafc56d8948ebb081::vusd::VUSD>
# Balance: 28000000
# Version: 338244725
# Digest: 7JpuxUnmu64AB5aukFtQRwYF1E3kj1Rn2uN8UyjMXXom
# BCS: AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKBbNQAy3Hfqs1QJ9GON3DDlVhIFQJBGxdcG6RMQAspTIAD+rAQAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA==
#
# ObjectID: 0x1bc1e43b319a9bf12353fb14c3f4b9342841d172e9e5b9cdb0510c2296accb77
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x929065320c756b8a4a841deeed013bd748ee45a28629c4aaafc56d8948ebb081::vusd::VUSD>
# Balance: 7000000
# Version: 338244725
# Digest: ENjWCBi7D3vqp9hta1fabNSQ49pBQh2psB14xuwS9PJ9
# BCS: AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKBvB5DsxmpvxI1P7FMP0uTQoQdFy6eW5zbBRDCKWrMt3wM9qAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA==
#
# ObjectID: 0xbc6dd3caa189309096cf3183786c9bb8d97d89d0185ec236214ebd2cc14f1319
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x929065320c756b8a4a841deeed013bd748ee45a28629c4aaafc56d8948ebb081::vusd::VUSD>
# Balance: 15000000
# Version: 338244725
# Digest: 74sxR2hccsGSP9Shbeuhs3Fawx9k1fZcnfMfvsYGdg1A
# BCS: AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKLxt08qhiTCQls8xg3hsm7jZfYnQGF7CNiFOvSzBTxMZwOHkAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA==
#

# test_sign_tx_vusd_merge_three
# -----------------------------
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
#             "ImmutableOrOwned": {
#               "object_id": "0x1bc1e43b319a9bf12353fb14c3f4b9342841d172e9e5b9cdb0510c2296accb77",
#               "version": "338244725",
#               "digest": "ENjWCBi7D3vqp9hta1fabNSQ49pBQh2psB14xuwS9PJ9"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x16cd400cb71dfaacd5027d18e3770c39558481502411b175c1ba44c400b294c8",
#               "version": "338244725",
#               "digest": "7JpuxUnmu64AB5aukFtQRwYF1E3kj1Rn2uN8UyjMXXom"
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
def test_sign_tx_vusd_merge_three(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAEAQC8bdPKoYkwkJbPMYN4bJu42X2J0BhewjYhTr0swU8TGXU0KRQAAAAAIFoker34YuFsSnGq+bXwfYo91Y8ZNApPdPgrfBte2xN1AQAbweQ7MZqb8SNT+xTD9Lk0KEHRcunluc2wUQwilqzLd3U0KRQAAAAAIMa5L4nBRHry8L3SdIN6wkhVUfU8zesw552W/4Woer4KAQAWzUAMtx36rNUCfRjjdww5VYSBUCQRsXXBukTEALKUyHU0KRQAAAAAIF23K7cqumqYsACp3Vrs1f5sAvEHlvhxTEITbRV6J0GAACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgIDAQAAAgEBAAECAAEBAQAAAQMAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYBE6uE80piJELVwLp/c8eRObD9ZciK3L4mVSlwsUQa5kruPUwUAAAAACDA+bJF/W52RAtRpqZmqU251Y0dDGWKjCAI+ri22feUPQ9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    object_list = [
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKLxt08qhiTCQls8xg3hsm7jZfYnQGF7CNiFOvSzBTxMZwOHkAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKBvB5DsxmpvxI1P7FMP0uTQoQdFy6eW5zbBRDCKWrMt3wM9qAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKBbNQAy3Hfqs1QJ9GON3DDlVhIFQJBGxdcG6RMQAspTIAD+rAQAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
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

# test_sign_tx_vusd_merge_split
# -----------------------------
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
#             "ImmutableOrOwned": {
#               "object_id": "0x1bc1e43b319a9bf12353fb14c3f4b9342841d172e9e5b9cdb0510c2296accb77",
#               "version": "338244725",
#               "digest": "ENjWCBi7D3vqp9hta1fabNSQ49pBQh2psB14xuwS9PJ9"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x16cd400cb71dfaacd5027d18e3770c39558481502411b175c1ba44c400b294c8",
#               "version": "338244725",
#               "digest": "7JpuxUnmu64AB5aukFtQRwYF1E3kj1Rn2uN8UyjMXXom"
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
def test_sign_tx_vusd_merge_split(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAFAQC8bdPKoYkwkJbPMYN4bJu42X2J0BhewjYhTr0swU8TGXU0KRQAAAAAIFoker34YuFsSnGq+bXwfYo91Y8ZNApPdPgrfBte2xN1AQAbweQ7MZqb8SNT+xTD9Lk0KEHRcunluc2wUQwilqzLd3U0KRQAAAAAIMa5L4nBRHry8L3SdIN6wkhVUfU8zesw552W/4Woer4KAQAWzUAMtx36rNUCfRjjdww5VYSBUCQRsXXBukTEALKUyHU0KRQAAAAAIF23K7cqumqYsACp3Vrs1f5sAvEHlvhxTEITbRV6J0GAAAhApa4CAAAAAAAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4DAwEAAAIBAQABAgACAQAAAQEDAAEBAwEAAAABBAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtgETq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSu49TBQAAAAAIMD5skX9bnZEC1GmpmapTbnVjR0MZYqMIAj6uLbZ95Q9D1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bboAwAAAAAAAEBCDwAAAAAAAA==')

    object_list = [
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKLxt08qhiTCQls8xg3hsm7jZfYnQGF7CNiFOvSzBTxMZwOHkAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKBvB5DsxmpvxI1P7FMP0uTQoQdFy6eW5zbBRDCKWrMt3wM9qAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKBbNQAy3Hfqs1QJ9GON3DDlVhIFQJBGxdcG6RMQAspTIAD+rAQAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
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

# test_sign_tx_vusd_transfer_two
# ------------------------------
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
#             "ImmutableOrOwned": {
#               "object_id": "0x1bc1e43b319a9bf12353fb14c3f4b9342841d172e9e5b9cdb0510c2296accb77",
#               "version": "338244725",
#               "digest": "ENjWCBi7D3vqp9hta1fabNSQ49pBQh2psB14xuwS9PJ9"
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
def test_sign_tx_vusd_transfer_two(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAADAQC8bdPKoYkwkJbPMYN4bJu42X2J0BhewjYhTr0swU8TGXU0KRQAAAAAIFoker34YuFsSnGq+bXwfYo91Y8ZNApPdPgrfBte2xN1AQAbweQ7MZqb8SNT+xTD9Lk0KEHRcunluc2wUQwilqzLd3U0KRQAAAAAIMa5L4nBRHry8L3SdIN6wkhVUfU8zesw552W/4Woer4KACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAgEAAAEBAAECAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AROrhPNKYiRC1cC6f3PHkTmw/WXIity+JlUpcLFEGuZK7j1MFAAAAAAgwPmyRf1udkQLUaamZqlNudWNHQxliowgCPq4ttn3lD0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKLxt08qhiTCQls8xg3hsm7jZfYnQGF7CNiFOvSzBTxMZwOHkAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKBvB5DsxmpvxI1P7FMP0uTQoQdFy6eW5zbBRDCKWrMt3wM9qAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
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

