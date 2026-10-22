Python
import json
import os
import pytest
from src.beast_ledger_engine import BEASTCivicLedger

def test_ledger_schema_exists():
    assert os.path.exists("schemas/ledger_record_schema.json"), "Ledger record schema missing!"

def test_ledger_genesis_and_chain():
    ledger = BEASTCivicLedger()
    assert len(ledger.chain) == 1, "Ledger should initialize with a genesis block."

    # Append test block
    ledger.append_block(
        payload_data={"test": "record_entry"},
        judicial_hash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        sentinel_sig="a1b2c3d4e5f67890abcdef1234567890abcdef1234567890abcdef1234567890"
    )

    assert len(ledger.chain) == 2
    assert ledger.verify_chain_integrity() is True

def test_ledger_tamper_detection():
    ledger = BEASTCivicLedger()
    ledger.append_block(
        payload_data={"test": "record_entry"},
        judicial_hash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        sentinel_sig="a1b2c3d4e5f67890abcdef1234567890abcdef1234567890abcdef1234567890"
    )

    # Tamper with the payload of block 1
    ledger.chain[1]["payload_data"]["test"] = "tampered_data"

    assert ledger.verify_chain_integrity() is False
300-Character Description for beast-ledger
Plaintext
The beast-ledger repository is the core append-only hash-chained Civic Ledger for B
