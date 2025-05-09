use crate::parser::common::{CoinType, IOTA_COIN_DIVISOR, IOTA_COIN_TYPE};
use crate::utils::*;

extern crate alloc;
use alloc::format;

use arrayvec::ArrayString;
use arrayvec::ArrayVec;
use either::*;
use ledger_crypto_helpers::common::HexSlice;

#[inline(never)]
pub fn get_coin_and_amount_fields(
    total_amount: u64,
    coin_type: CoinType,
) -> (
    (ArrayString<32>, ArrayString<32>),
    Either<ArrayString<8>, (ArrayString<4>, ArrayString<256>)>,
) {
    if let Some((ticker, divisor)) = get_known_coin_ticker(&coin_type) {
        let (quotient, remainder_str) = get_amount_in_decimals(total_amount, divisor);
        let v1 = format!(
            "{} {}.{}",
            ticker.as_str(),
            quotient,
            remainder_str.as_str()
        );
        let amount = (
            ArrayString::from("Amount").unwrap(),
            ArrayString::from(&v1).unwrap(),
        );
        (amount, Left(ticker))
    } else {
        let v1 = format!("{}", total_amount);
        let amount = (
            ArrayString::from("Raw Amount").unwrap(),
            ArrayString::from(&v1).unwrap(),
        );
        let (coin_id, module, name) = coin_type;

        let v2 = format!(
            "{}::{}::{}",
            HexSlice(&coin_id),
            core::str::from_utf8(module.as_slice()).unwrap_or("invalid utf-8"),
            core::str::from_utf8(name.as_slice()).unwrap_or("invalid utf-8")
        );
        let coin = Right((
            ArrayString::from("Coin").unwrap(),
            ArrayString::from(&v2).unwrap(),
        ));
        (amount, coin)
    }
}

#[inline(never)]
fn get_known_coin_ticker(coin_type: &CoinType) -> Option<(ArrayString<8>, u8)> {
    if *coin_type == IOTA_COIN_TYPE {
        return Some((ArrayString::from("IOTA").unwrap(), IOTA_COIN_DIVISOR));
    }

    for k in KNOWN_COINS {
        let mut module = ArrayVec::new();
        let _ = module.try_extend_from_slice(k.module.as_bytes());

        let mut function = ArrayVec::new();
        let _ = function.try_extend_from_slice(k.function.as_bytes());

        if *coin_type == (k.coin_id, module, function) {
            return Some((ArrayString::from(k.ticker).unwrap(), k.divisor));
        }
    }
    None
}

struct KnownCoin<'a> {
    coin_id: [u8; 32],
    module: &'a str,
    function: &'a str,
    divisor: u8,
    ticker: &'a str,
}

use hex_literal::hex;

const KNOWN_COINS: [KnownCoin; 2] = [
    // Mainnet stIOTA
    KnownCoin {
        coin_id: hex!("346778989a9f57480ec3fee15f2cd68409c73a62112d40a3efd13987997be68c"),
        module: "cert",
        function: "CERT",
        divisor: 9,
        ticker: "stIOTA",
    },
    // Testnet stIOTA
    KnownCoin {
        coin_id: hex!("1461ef74f97e83eb024a448ab851f980f4e577a97877069c72b44b5fe9929ee3"),
        module: "cert",
        function: "CERT",
        divisor: 9,
        ticker: "stIOTA",
    },
];
