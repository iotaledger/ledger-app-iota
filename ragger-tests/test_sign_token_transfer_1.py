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
# ObjectID: 0x2d9482356f5c02694cc98ac72b517e24eaf54ef3a7662f8cee81ce6ca822c739
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x1ec8ca48b9b39f721510dc717d7f077c9bc84eca28e784ba8dc0b913e23ed5ca::deposit_test_coin::DEPOSIT_TEST_COIN>
# Balance: 1000000000
# Version: 292323579
# Digest: 79ScvbUk9oVCR64kuvZSDQjGFqwi5Kq6QdH3oUfENT7c
# BCS: AAMHHsjKSLmzn3IVENxxfX8HfJvITsoo54S6jcC5E+I+1coRZGVwb3NpdF90ZXN0X2NvaW4RREVQT1NJVF9URVNUX0NPSU4A+4BsEQAAAAAoLZSCNW9cAmlMyYrHK1F+JOr1TvOnZi+M7oHObKgixzkAypo7AAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiABHefVakVH8AxQKTp2EY6phZ6YqPIOvu3YHdqPQaxWa9ATFwAAAAAA
#
# ObjectID: 0x57a524205644363fed2c495e6a4c9df0b23347987176ea54b08d9eedb5e2abdb
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x1461ef74f97e83eb024a448ab851f980f4e577a97877069c72b44b5fe9929ee3::cert::CERT>
# Balance: 4676174571
# Version: 340540901
# Digest: 8gWVVowMMtRakSYTLCyco233PMmLoXkvK7FvySg9D636
# BCS: AAMHFGHvdPl+g+sCSkSKuFH5gPTld6l4dwaccrRLX+mSnuMEY2VydARDRVJUAOU9TBQAAAAAKFelJCBWRDY/7SxJXmpMnfCyM0eYcXbqVLCNnu214qvb68K4FgEAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYgPtVht5QLbaiJTmN0p92D3yCv1lNJblfPGRO2elW1FznwDxQAAAAAAA==
#
# ObjectID: 0x78084fe4b7cb74d2054e426c2654085dd0cbdfa488717974259e2e1870ac5cab
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x1461ef74f97e83eb024a448ab851f980f4e577a97877069c72b44b5fe9929ee3::cert::CERT>
# Balance: 935234914
# Version: 340540910
# Digest: AMkvwZn1oYF6iNbzmBotZaTYa15H1yN1PRkWdaCFjbNd
# BCS: AAMHFGHvdPl+g+sCSkSKuFH5gPTld6l4dwaccrRLX+mSnuMEY2VydARDRVJUAO49TBQAAAAAKHgIT+S3y3TSBU5CbCZUCF3Qy9+kiHF5dCWeLhhwrFyrYo2+NwAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYguKlUaKTBNNc/LtiCIMGrIyu7ih1a6fdgTQ8/qHwqNkDwDxQAAAAAAA==
#
# ObjectID: 0x7832ee1651ef144281b3d785bc8b7501f37aa46ba96a32be95d5d0071e501950
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x1461ef74f97e83eb024a448ab851f980f4e577a97877069c72b44b5fe9929ee3::cert::CERT>
# Balance: 14028523715
# Version: 340540909
# Digest: 2B2NSgS2JJUuXgfNckxheig2zrScjQQtKN1RyPMBd8fU
# BCS: AAMHFGHvdPl+g+sCSkSKuFH5gPTld6l4dwaccrRLX+mSnuMEY2VydARDRVJUAO09TBQAAAAAKHgy7hZR7xRCgbPXhbyLdQHzeqRrqWoyvpXV0AceUBlQw0gqRAMAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYgAZWKkwQ2s+uvbZ3YacRydwI3n61B9lVfr8UWyjZnE1vwDxQAAAAAAA==
#
# ObjectID: 0xbc6dd3caa189309096cf3183786c9bb8d97d89d0185ec236214ebd2cc14f1319
# Owner: Address(0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6)
# ObjectType: 0x2::coin::Coin<0x929065320c756b8a4a841deeed013bd748ee45a28629c4aaafc56d8948ebb081::vusd::VUSD>
# Balance: 15000000
# Version: 338244725
# Digest: 74sxR2hccsGSP9Shbeuhs3Fawx9k1fZcnfMfvsYGdg1A
# BCS: AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKLxt08qhiTCQls8xg3hsm7jZfYnQGF7CNiFOvSzBTxMZwOHkAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA==
#

# test_sign_tx_stiota_whole_coin
# ------------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x57a524205644363fed2c495e6a4c9df0b23347987176ea54b08d9eedb5e2abdb",
#               "version": "340540901",
#               "digest": "8gWVVowMMtRakSYTLCyco233PMmLoXkvK7FvySg9D636"
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
def test_sign_tx_stiota_whole_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAACAQBXpSQgVkQ2P+0sSV5qTJ3wsjNHmHF26lSwjZ7tteKr2+U9TBQAAAAAIHIgzlTp2lDccQR2TBqspDxfa6/RSgYLaG5cQr3cf/EtACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAQEAAAEBAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AROrhPNKYiRC1cC6f3PHkTmw/WXIity+JlUpcLFEGuZK7j1MFAAAAAAgwPmyRf1udkQLUaamZqlNudWNHQxliowgCPq4ttn3lD0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAMHFGHvdPl+g+sCSkSKuFH5gPTld6l4dwaccrRLX+mSnuMEY2VydARDRVJUAOU9TBQAAAAAKFelJCBWRDY/7SxJXmpMnfCyM0eYcXbqVLCNnu214qvb68K4FgEAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYgPtVht5QLbaiJTmN0p92D3yCv1lNJblfPGRO2elW1FznwDxQAAAAAAA=='),
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

# test_sign_tx_vusd_whole_coin
# ----------------------------
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
def test_sign_tx_vusd_whole_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAACAQC8bdPKoYkwkJbPMYN4bJu42X2J0BhewjYhTr0swU8TGXU0KRQAAAAAIFoker34YuFsSnGq+bXwfYo91Y8ZNApPdPgrfBte2xN1ACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAQEAAAEBAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AROrhPNKYiRC1cC6f3PHkTmw/WXIity+JlUpcLFEGuZK7j1MFAAAAAAgwPmyRf1udkQLUaamZqlNudWNHQxliowgCPq4ttn3lD0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKLxt08qhiTCQls8xg3hsm7jZfYnQGF7CNiFOvSzBTxMZwOHkAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
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

# test_sign_tx_three_stiota_whole_coin
# ------------------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x57a524205644363fed2c495e6a4c9df0b23347987176ea54b08d9eedb5e2abdb",
#               "version": "340540901",
#               "digest": "8gWVVowMMtRakSYTLCyco233PMmLoXkvK7FvySg9D636"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x78084fe4b7cb74d2054e426c2654085dd0cbdfa488717974259e2e1870ac5cab",
#               "version": "340540910",
#               "digest": "AMkvwZn1oYF6iNbzmBotZaTYa15H1yN1PRkWdaCFjbNd"
#             }
#           },
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x7832ee1651ef144281b3d785bc8b7501f37aa46ba96a32be95d5d0071e501950",
#               "version": "340540909",
#               "digest": "2B2NSgS2JJUuXgfNckxheig2zrScjQQtKN1RyPMBd8fU"
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
def test_sign_tx_three_stiota_whole_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAEAQBXpSQgVkQ2P+0sSV5qTJ3wsjNHmHF26lSwjZ7tteKr2+U9TBQAAAAAIHIgzlTp2lDccQR2TBqspDxfa6/RSgYLaG5cQr3cf/EtAQB4CE/kt8t00gVOQmwmVAhd0MvfpIhxeXQlni4YcKxcq+49TBQAAAAAIIsKeGhpR5qy63EhY+R+eOwURcd0M3HNmFm812IOKCY+AQB4Mu4WUe8UQoGz14W8i3UB83qka6lqMr6V1dAHHlAZUO09TBQAAAAAIBFtCzLdLe5IVl3ThYf4LhZniW0NvLhdhLCyCRi9+sbzACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAwEAAAEBAAECAAEDAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AROrhPNKYiRC1cC6f3PHkTmw/WXIity+JlUpcLFEGuZK7j1MFAAAAAAgwPmyRf1udkQLUaamZqlNudWNHQxliowgCPq4ttn3lD0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAMHFGHvdPl+g+sCSkSKuFH5gPTld6l4dwaccrRLX+mSnuMEY2VydARDRVJUAOU9TBQAAAAAKFelJCBWRDY/7SxJXmpMnfCyM0eYcXbqVLCNnu214qvb68K4FgEAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYgPtVht5QLbaiJTmN0p92D3yCv1lNJblfPGRO2elW1FznwDxQAAAAAAA=='),
        base64.b64decode('AAMHFGHvdPl+g+sCSkSKuFH5gPTld6l4dwaccrRLX+mSnuMEY2VydARDRVJUAO49TBQAAAAAKHgIT+S3y3TSBU5CbCZUCF3Qy9+kiHF5dCWeLhhwrFyrYo2+NwAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYguKlUaKTBNNc/LtiCIMGrIyu7ih1a6fdgTQ8/qHwqNkDwDxQAAAAAAA=='),
        base64.b64decode('AAMHFGHvdPl+g+sCSkSKuFH5gPTld6l4dwaccrRLX+mSnuMEY2VydARDRVJUAO09TBQAAAAAKHgy7hZR7xRCgbPXhbyLdQHzeqRrqWoyvpXV0AceUBlQw0gqRAMAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYgAZWKkwQ2s+uvbZ3YacRydwI3n61B9lVfr8UWyjZnE1vwDxQAAAAAAA=='),
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

# test_sign_tx_three_vusd_whole_coin
# ----------------------------------
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
def test_sign_tx_three_vusd_whole_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAAEAQC8bdPKoYkwkJbPMYN4bJu42X2J0BhewjYhTr0swU8TGXU0KRQAAAAAIFoker34YuFsSnGq+bXwfYo91Y8ZNApPdPgrfBte2xN1AQAbweQ7MZqb8SNT+xTD9Lk0KEHRcunluc2wUQwilqzLd3U0KRQAAAAAIMa5L4nBRHry8L3SdIN6wkhVUfU8zesw552W/4Woer4KAQAWzUAMtx36rNUCfRjjdww5VYSBUCQRsXXBukTEALKUyHU0KRQAAAAAIF23K7cqumqYsACp3Vrs1f5sAvEHlvhxTEITbRV6J0GAACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEBAwEAAAEBAAECAAEDAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AROrhPNKYiRC1cC6f3PHkTmw/WXIity+JlUpcLFEGuZK7j1MFAAAAAAgwPmyRf1udkQLUaamZqlNudWNHQxliowgCPq4ttn3lD0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

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

# test_sign_tx_vusd_split_coin
# ----------------------------
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
def test_sign_tx_vusd_split_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAADAQC8bdPKoYkwkJbPMYN4bJu42X2J0BhewjYhTr0swU8TGXU0KRQAAAAAIFoker34YuFsSnGq+bXwfYo91Y8ZNApPdPgrfBte2xN1AAigJSYAAAAAAAAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4CAgEAAAEBAQABAQMAAAAAAQIAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYBE6uE80piJELVwLp/c8eRObD9ZciK3L4mVSlwsUQa5kruPUwUAAAAACDA+bJF/W52RAtRpqZmqU251Y0dDGWKjCAI+ri22feUPQ9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    object_list = [
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKLxt08qhiTCQls8xg3hsm7jZfYnQGF7CNiFOvSzBTxMZwOHkAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
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

# test_sign_tx_stiota_split_coin
# ------------------------------
# TransactionData:
# {
#   "V1": {
#     "kind": {
#       "Programmable": {
#         "inputs": [
#           {
#             "ImmutableOrOwned": {
#               "object_id": "0x7832ee1651ef144281b3d785bc8b7501f37aa46ba96a32be95d5d0071e501950",
#               "version": "340540909",
#               "digest": "2B2NSgS2JJUuXgfNckxheig2zrScjQQtKN1RyPMBd8fU"
#             }
#           },
#           {
#             "Pure": "AHhBywIAAAA="
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
def test_sign_tx_stiota_split_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAADAQB4Mu4WUe8UQoGz14W8i3UB83qka6lqMr6V1dAHHlAZUO09TBQAAAAAIBFtCzLdLe5IVl3ThYf4LhZniW0NvLhdhLCyCRi9+sbzAAgAeEHLAgAAAAAgGzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4CAgEAAAEBAQABAQMAAAAAAQIAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYBE6uE80piJELVwLp/c8eRObD9ZciK3L4mVSlwsUQa5kruPUwUAAAAACDA+bJF/W52RAtRpqZmqU251Y0dDGWKjCAI+ri22feUPQ9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    object_list = [
        base64.b64decode('AAMHFGHvdPl+g+sCSkSKuFH5gPTld6l4dwaccrRLX+mSnuMEY2VydARDRVJUAO09TBQAAAAAKHgy7hZR7xRCgbPXhbyLdQHzeqRrqWoyvpXV0AceUBlQw0gqRAMAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYgAZWKkwQ2s+uvbZ3YacRydwI3n61B9lVfr8UWyjZnE1vwDxQAAAAAAA=='),
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

# test_sign_tx_unrecognized_coin
# ------------------------------
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
#             "ImmutableOrOwned": {
#               "object_id": "0x2d9482356f5c02694cc98ac72b517e24eaf54ef3a7662f8cee81ce6ca822c739",
#               "version": "292323579",
#               "digest": "79ScvbUk9oVCR64kuvZSDQjGFqwi5Kq6QdH3oUfENT7c"
#             }
#           }
#         ],
#         "commands": [
#           {
#             "TransferObjects": {
#               "objects": [
#                 {
#                   "Input": 1
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
def test_sign_tx_unrecognized_coin(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAACACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEALZSCNW9cAmlMyYrHK1F+JOr1TvOnZi+M7oHObKgixzn7gGwRAAAAACBbT7xnnhHP0679qpTId7IICMKeSKS+kCiu/GQnMjihvwEBAQEBAAEAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AROrhPNKYiRC1cC6f3PHkTmw/WXIity+JlUpcLFEGuZK7j1MFAAAAAAgwPmyRf1udkQLUaamZqlNudWNHQxliowgCPq4ttn3lD0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAMHHsjKSLmzn3IVENxxfX8HfJvITsoo54S6jcC5E+I+1coRZGVwb3NpdF90ZXN0X2NvaW4RREVQT1NJVF9URVNUX0NPSU4A+4BsEQAAAAAoLZSCNW9cAmlMyYrHK1F+JOr1TvOnZi+M7oHObKgixzkAypo7AAAAAAAPWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtiABHefVakVH8AxQKTp2EY6phZ6YqPIOvu3YHdqPQaxWa9ATFwAAAAAA'),
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
                               , NavInsID.RIGHT_CLICK, NavInsID.RIGHT_CLICK # Coin ...
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

