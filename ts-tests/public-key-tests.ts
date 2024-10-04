import { sendCommandAndAccept, BASE_URL, IOTA_BIP_PATH, TESTNET_BIP_PATH } from "./common";
import { expect } from 'chai';
import { describe, it } from 'mocha';
import Axios from 'axios';
import type Iota from "./Iota";

// Public key and address for default speculos mnemonic: "glory promote mansion idle axis finger extra february uncover one trip resource lawn turtle enact monster seven myth punch hobby comfort wild raise skin"
// with BIP32 Path: 44'/4218'/0'/0'/0' (Testnet: 44'/1'/0'/0'/0')
const IOTA_PUBLIC_KEY = "f0a9c612b7e69f1a114aa9189c1f32997d395d09d183368ddfd6d5dc49e34647";
const TESTNET_PUBLIC_KEY = "f9e5d9f4437cf656ef76da8fa17d38f66569ec61cca09b28d7210d0ed18b59f0";
export const IOTA_ADDRESS = "1b3669e321893ee49c387a08fc251dbfff37cd2a981e6c473a5b2afde19d363e";
export const TESTNET_ADDRESS = "3a0de157f4b6c4bed40caf93def86c3e6946ed35d27c7121ef264336973e9955";

describe('public key tests', () => {

    afterEach(async function () {
        await Axios.post(BASE_URL + "/automation", { version: 1, rules: [] });
        await Axios.delete(BASE_URL + "/events");
    });

    it('provides a public key', async () => {

        await sendCommandAndAccept(async (client: Iota) => {
            const rv = await client.getPublicKey(IOTA_BIP_PATH);
            expect(new Buffer(rv.publicKey).toString('hex')).to.equal(IOTA_PUBLIC_KEY);
            expect(new Buffer(rv.address).toString('hex')).to.equal(IOTA_ADDRESS);
            return;
        }, []);
    });

    it('provides a public key testnet coin type', async () => {

        await sendCommandAndAccept(async (client: Iota) => {
            const rv = await client.getPublicKey(TESTNET_BIP_PATH);
            expect(new Buffer(rv.publicKey).toString('hex')).to.equal(TESTNET_PUBLIC_KEY);
            expect(new Buffer(rv.address).toString('hex')).to.equal(TESTNET_ADDRESS);
            return;
        }, []);
    });

    it('does address verification', async () => {

        await sendCommandAndAccept(async (client: Iota) => {
            const rv = await client.verifyAddress(IOTA_BIP_PATH);
            expect(new Buffer(rv.publicKey).toString('hex')).to.equal(IOTA_PUBLIC_KEY);
            expect(new Buffer(rv.address).toString('hex')).to.equal(IOTA_ADDRESS);
            return;
        }, [
            {
                "header": "Provide Public Key",
                "prompt": "",
            },
            {
                "header": "Address",
                "prompt": "0x" + IOTA_ADDRESS,
                "paginate": true,
            },
            {
                "text": "Confirm",
                "x": 43,
                "y": 11,
                "clear": false
            },
        ]);
    });
});
