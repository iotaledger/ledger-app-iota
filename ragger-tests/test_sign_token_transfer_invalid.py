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
# Owner: Account Address ( 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6 )
# ObjectType: GasCoin
# Balance: 58985094000
# Version: 340540910
# Digest: DzJ7RSo7cQGWYZcn4bF886ZAavaCyAXvHxcbsHgKj8mz
# BCS: AAHuPUwUAAAAACgTq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSnAbybsNAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ILipVGikwTTXPy7YgiDBqyMru4odWun3YE0PP6h8KjZAsPUOAAAAAAA=
#
# ObjectID: 0x7832ee1651ef144281b3d785bc8b7501f37aa46ba96a32be95d5d0071e501950
# Owner: Account Address ( 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6 )
# ObjectType: 0x2::coin::Coin<0x1461ef74f97e83eb024a448ab851f980f4e577a97877069c72b44b5fe9929ee3::cert::CERT>
# Balance: 14028523715
# Version: 340540909
# Digest: 2B2NSgS2JJUuXgfNckxheig2zrScjQQtKN1RyPMBd8fU
# BCS: AAMHFGHvdPl+g+sCSkSKuFH5gPTld6l4dwaccrRLX+mSnuMEY2VydARDRVJUAO09TBQAAAAAKHgy7hZR7xRCgbPXhbyLdQHzeqRrqWoyvpXV0AceUBlQw0gqRAMAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYgAZWKkwQ2s+uvbZ3YacRydwI3n61B9lVfr8UWyjZnE1vwDxQAAAAAAA==
#
# ObjectID: 0xbc6dd3caa189309096cf3183786c9bb8d97d89d0185ec236214ebd2cc14f1319
# Owner: Account Address ( 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6 )
# ObjectType: 0x2::coin::Coin<0x929065320c756b8a4a841deeed013bd748ee45a28629c4aaafc56d8948ebb081::vusd::VUSD>
# Balance: 15000000
# Version: 338244725
# Digest: 74sxR2hccsGSP9Shbeuhs3Fawx9k1fZcnfMfvsYGdg1A
# BCS: AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKLxt08qhiTCQls8xg3hsm7jZfYnQGF7CNiFOvSzBTxMZwOHkAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA==
#

# test_sign_tx_vusd_and_stiota
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
#       "Pure": {
#         "bytes": "GzZp4yGJPuScOHoI/CUdv/83zSqYHmxHOlsq/eGdNj4="
#       },
#       "$kind": "Pure"
#     },
#     {
#       "Object": {
#         "ImmOrOwnedObject": {
#           "objectId": "0xbc6dd3caa189309096cf3183786c9bb8d97d89d0185ec236214ebd2cc14f1319",
#           "version": "338244725",
#           "digest": "74sxR2hccsGSP9Shbeuhs3Fawx9k1fZcnfMfvsYGdg1A"
#         },
#         "$kind": "ImmOrOwnedObject"
#       },
#       "$kind": "Object"
#     },
#     {
#       "Object": {
#         "ImmOrOwnedObject": {
#           "objectId": "0x7832ee1651ef144281b3d785bc8b7501f37aa46ba96a32be95d5d0071e501950",
#           "version": "340540909",
#           "digest": "2B2NSgS2JJUuXgfNckxheig2zrScjQQtKN1RyPMBd8fU"
#         },
#         "$kind": "ImmOrOwnedObject"
#       },
#       "$kind": "Object"
#     }
#   ],
#   "commands": [
#     {
#       "TransferObjects": {
#         "objects": [
#           {
#             "Input": 1,
#             "$kind": "Input"
#           }
#         ],
#         "address": {
#           "Input": 0,
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
#         "objectId": "0x13ab84f34a622442d5c0ba7f73c79139b0fd65c88adcbe26552970b1441ae64a",
#         "version": "340540910",
#         "digest": "DzJ7RSo7cQGWYZcn4bF886ZAavaCyAXvHxcbsHgKj8mz"
#       }
#     ]
#   }
# }
def test_sign_tx_vusd_and_stiota(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAADACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEAvG3TyqGJMJCWzzGDeGybuNl9idAYXsI2IU69LMFPExl1NCkUAAAAACBaJHq9+GLhbEpxqvm18H2KPdWPGTQKT3T4K3wbXtsTdQEAeDLuFlHvFEKBs9eFvIt1AfN6pGupajK+ldXQBx5QGVDtPUwUAAAAACARbQsy3S3uSFZd04WH+C4WZ4ltDby4XYSwsgkYvfrG8wIBAQEBAAEAAAEBAQIAAQAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYBE6uE80piJELVwLp/c8eRObD9ZciK3L4mVSlwsUQa5kruPUwUAAAAACDA+bJF/W52RAtRpqZmqU251Y0dDGWKjCAI+ri22feUPQ9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W26AMAAAAAAABAQg8AAAAAAAA=')

    object_list = [
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKLxt08qhiTCQls8xg3hsm7jZfYnQGF7CNiFOvSzBTxMZwOHkAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
        base64.b64decode('AAMHFGHvdPl+g+sCSkSKuFH5gPTld6l4dwaccrRLX+mSnuMEY2VydARDRVJUAO09TBQAAAAAKHgy7hZR7xRCgbPXhbyLdQHzeqRrqWoyvpXV0AceUBlQw0gqRAMAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYgAZWKkwQ2s+uvbZ3YacRydwI3n61B9lVfr8UWyjZnE1vwDxQAAAAAAA=='),
        base64.b64decode('AAHuPUwUAAAAACgTq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSnAbybsNAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ILipVGikwTTXPy7YgiDBqyMru4odWun3YE0PP6h8KjZAsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

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

# test_sign_tx_vusd_and_iota
# --------------------------
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
#     },
#     {
#       "Object": {
#         "ImmOrOwnedObject": {
#           "objectId": "0xbc6dd3caa189309096cf3183786c9bb8d97d89d0185ec236214ebd2cc14f1319",
#           "version": "338244725",
#           "digest": "74sxR2hccsGSP9Shbeuhs3Fawx9k1fZcnfMfvsYGdg1A"
#         },
#         "$kind": "ImmOrOwnedObject"
#       },
#       "$kind": "Object"
#     }
#   ],
#   "commands": [
#     {
#       "TransferObjects": {
#         "objects": [
#           {
#             "Input": 1,
#             "$kind": "Input"
#           }
#         ],
#         "address": {
#           "Input": 0,
#           "$kind": "Input"
#         }
#       },
#       "$kind": "TransferObjects"
#     },
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
#         "objectId": "0x13ab84f34a622442d5c0ba7f73c79139b0fd65c88adcbe26552970b1441ae64a",
#         "version": "340540910",
#         "digest": "DzJ7RSo7cQGWYZcn4bF886ZAavaCyAXvHxcbsHgKj8mz"
#       }
#     ]
#   }
# }
def test_sign_tx_vusd_and_iota(backend, scenario_navigator, device, navigator):
    client = Client(backend, use_block_protocol=True)
    path = "m/44'/4218'/0'/0'/1'" # 0x0f58eb1351454d623a6a4366198d6cd5aa4a12a12a3caefb501476e06d8bd5b6

    _, public_key, _, _ = client.get_public_key(path=path)
    assert len(public_key) == 32

    transaction = base64.b64decode('AAAAAAACACAbNmnjIYk+5Jw4egj8JR2//zfNKpgebEc6Wyr94Z02PgEAvG3TyqGJMJCWzzGDeGybuNl9idAYXsI2IU69LMFPExl1NCkUAAAAACBaJHq9+GLhbEpxqvm18H2KPdWPGTQKT3T4K3wbXtsTdQIBAQEBAAEAAAEBAAEAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2AROrhPNKYiRC1cC6f3PHkTmw/WXIity+JlUpcLFEGuZK7j1MFAAAAAAgwPmyRf1udkQLUaamZqlNudWNHQxliowgCPq4ttn3lD0PWOsTUUVNYjpqQ2YZjWzVqkoSoSo8rvtQFHbgbYvVtugDAAAAAAAAQEIPAAAAAAAA')

    object_list = [
        base64.b64decode('AAMHkpBlMgx1a4pKhB3u7QE710juRaKGKcSqr8VtiUjrsIEEdnVzZARWVVNEAHU0KRQAAAAAKLxt08qhiTCQls8xg3hsm7jZfYnQGF7CNiFOvSzBTxMZwOHkAAAAAAAAD1jrE1FFTWI6akNmGY1s1apKEqEqPK77UBR24G2L1bYg+IoPFKZUYrotPBXnn3FJ9G/LaZ70lkkdB9cvK1Clb9/wDxQAAAAAAA=='),
        base64.b64decode('AAHuPUwUAAAAACgTq4TzSmIkQtXAun9zx5E5sP1lyIrcviZVKXCxRBrmSnAbybsNAAAAAA9Y6xNRRU1iOmpDZhmNbNWqShKhKjyu+1AUduBti9W2ILipVGikwTTXPy7YgiDBqyMru4odWun3YE0PP6h8KjZAsPUOAAAAAAA='),
    ]

    def apdu_task():
        return client.sign_tx(path=path, transaction=transaction, object_list=object_list)

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

