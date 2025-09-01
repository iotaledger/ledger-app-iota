use crate::parser::common::{CoinType, IOTA_COIN_DECIMALS, IOTA_COIN_TYPE};
use crate::utils::*;

extern crate alloc;
use alloc::format;

use arrayvec::ArrayString;
use arrayvec::ArrayVec;
use either::*;
use ledger_crypto_helpers::common::HexSlice;
use ledger_log::info;

#[cfg(target_os = "nanox")]
pub const MESSAGE_MAX_LENGTH: usize = 1024 * 2;

#[cfg(not(target_os = "nanox"))]
pub const MESSAGE_MAX_LENGTH: usize = 1024 * 4;

pub fn is_printable_ascii(data: &ArrayVec<u8, MESSAGE_MAX_LENGTH>) -> Option<&str> {
    if data.iter().all(|&b| b > 0 && b.is_ascii()) {
        core::str::from_utf8(data.as_slice()).ok()
    } else {
        info!("is_printable_ascii: input contains NUL char or non-ASCII byte");
        None
    }
}

#[inline(never)]
pub fn get_coin_and_amount_fields(
    total_amount: u64,
    coin_type: CoinType,
) -> (
    (ArrayString<32>, ArrayString<32>),
    Either<ArrayString<8>, (ArrayString<4>, ArrayString<256>)>,
) {
    if let Some((ticker, decimals)) = get_known_coin_ticker(&coin_type) {
        let (quotient, remainder_str) = get_amount_in_decimals(total_amount, decimals);
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
        return Some((ArrayString::from("IOTA").unwrap(), IOTA_COIN_DECIMALS));
    }

    for k in KNOWN_COINS {
        let mut module = ArrayVec::new();
        let _ = module.try_extend_from_slice(k.module.as_bytes());

        let mut witness = ArrayVec::new();
        let _ = witness.try_extend_from_slice(k.witness.as_bytes());

        if *coin_type == (k.coin_id, module, witness) {
            return Some((ArrayString::from(k.ticker).unwrap(), k.decimals));
        }
    }
    None
}

struct KnownCoin<'a> {
    coin_id: [u8; 32],
    module: &'a str,
    witness: &'a str,
    decimals: u8,
    ticker: &'a str,
}

use hex_literal::hex;

const KNOWN_COINS: [KnownCoin; 4] = [
    // Mainnet Swirl stIOTA
    KnownCoin {
        coin_id: hex!("346778989a9f57480ec3fee15f2cd68409c73a62112d40a3efd13987997be68c"),
        module: "cert",
        witness: "CERT",
        decimals: 9,
        ticker: "stIOTA",
    },
    // Testnet Swirl stIOTA
    KnownCoin {
        coin_id: hex!("1461ef74f97e83eb024a448ab851f980f4e577a97877069c72b44b5fe9929ee3"),
        module: "cert",
        witness: "CERT",
        decimals: 9,
        ticker: "stIOTA",
    },
    // Mainnet Virtue USD
    KnownCoin {
        coin_id: hex!("d3b63e603a78786facf65ff22e79701f3e824881a12fa3268d62a75530fe904f"),
        module: "vusd",
        witness: "VUSD",
        decimals: 6,
        ticker: "VUSD",
    },
    // Testnet Virtue USD
    KnownCoin {
        coin_id: hex!("929065320c756b8a4a841deeed013bd748ee45a28629c4aaafc56d8948ebb081"),
        module: "vusd",
        witness: "VUSD",
        decimals: 6,
        ticker: "VUSD",
    },
];
