#!/usr/bin/env python3
"""Tests for electrum_order. Run: python3 utils/test_electrum_order.py"""
from electrum_order import PREFERRED_ELECTRUM_HOSTS, sort_electrums_preferred_first


def test_digibyte_operated_server_comes_first():
    servers = [
        {"url": "dgb.electrum1.cipig.net:20059"},
        {"url": "dgb.electrum2.cipig.net:20059"},
        {"url": "electrum.digiscope.me:50002"},
    ]
    assert [s["url"] for s in sort_electrums_preferred_first(servers, "url")] == [
        "electrum.digiscope.me:50002",
        "dgb.electrum1.cipig.net:20059",
        "dgb.electrum2.cipig.net:20059",
    ]


def test_the_rest_stay_alphabetical():
    servers = [{"url": "b.example:1"}, {"url": "a.example:1"}]
    assert [s["url"] for s in sort_electrums_preferred_first(servers, "url")] == [
        "a.example:1",
        "b.example:1",
    ]


def test_preferred_hosts_keep_their_listed_order():
    preferred = [{"url": f"{host}:50002"} for host in reversed(PREFERRED_ELECTRUM_HOSTS)]
    assert [s["url"] for s in sort_electrums_preferred_first(preferred, "url")] == [
        f"{host}:50002" for host in PREFERRED_ELECTRUM_HOSTS
    ]


def test_an_entry_without_the_key_does_not_raise():
    servers = [{"ws_url": "x.example:2"}, {"url": "electrum.digiscope.me:50002"}]
    assert sort_electrums_preferred_first(servers, "url")[0]["url"] == (
        "electrum.digiscope.me:50002"
    )


if __name__ == "__main__":
    for name, case in sorted(globals().items()):
        if name.startswith("test_"):
            case()
            print(f"ok {name}")
    print("all passed")
