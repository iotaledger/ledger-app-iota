use crate::parser::common::*;
use core::convert::TryFrom;
use core::marker::ConstParamTy;
use ledger_device_sdk::io::{ApduHeader, StatusWords};
use ledger_parser_combinators::core_parsers::*;
use ledger_parser_combinators::endianness::*;
use num_enum::TryFromPrimitive;

#[derive(ConstParamTy, PartialEq, Eq)]
#[repr(u8)]
pub enum ParseChecks {
    None,
    PromptUser,
    CheckSwapTx,
}

// Payload for a public key request
pub type Bip32Key = DArray<Byte, U32<{ Endianness::Little }>, 10>;

pub struct IotaPubKeyAddress(IotaAddressRaw);

use ledger_device_sdk::hash::{blake2::Blake2b_256, HashError, HashInit};

/// Compressed Ed25519 public key
pub type Ed25519PubKey = [u8; 32];

impl IotaPubKeyAddress {
    pub fn from_pubkey(pubkey: &Ed25519PubKey) -> Result<Self, HashError> {
        let mut hasher = Blake2b_256::new();
        let mut hash = IotaAddressRaw::default();
        hasher.update(pubkey)?;
        hasher.finalize(&mut hash)?;
        Ok(IotaPubKeyAddress(hash))
    }
    pub fn get_binary_address(&self) -> &[u8] {
        &self.0
    }
}

impl core::fmt::Display for IotaPubKeyAddress {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        write!(f, "0x{}", HexSlice(&self.0))
    }
}

/// Displays a byte slice as lowercase hex
pub struct HexSlice<'a>(pub &'a [u8]);

impl core::fmt::Display for HexSlice<'_> {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        for byte in self.0 {
            write!(f, "{:02x}", byte)?;
        }
        Ok(())
    }
}

#[repr(u8)]
#[derive(Debug, TryFromPrimitive)]
pub enum Ins {
    GetVersion = 0,
    VerifyAddress = 1,
    GetPubkey = 2,
    Sign = 3,
    GetVersionStr = 0xfe,
    Exit = 0xff,
}

impl TryFrom<ApduHeader> for Ins {
    type Error = StatusWords;
    fn try_from(m: ApduHeader) -> Result<Ins, Self::Error> {
        match m {
            ApduHeader {
                cla: 0,
                ins,
                p1: 0,
                p2: 0,
            } => Self::try_from(ins).map_err(|_| StatusWords::BadIns),
            _ => Err(StatusWords::BadIns),
        }
    }
}

// Status word used when swap transaction parameters check failed
pub const SW_SWAP_TX_PARAM_MISMATCH: u16 = 0x6e05;
