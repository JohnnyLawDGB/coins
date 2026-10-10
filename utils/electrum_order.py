#!/usr/bin/env python3
"""Server priority for the DigiByte fork of the coins repo.

KDF connects to electrum servers in the order the coin config lists them, so
the DigiByte-operated servers have to come first (DigiByte wallet spec §7.2).
Upstream sorts every list alphabetically, which put `dgb.electrum*.cipig.net`
ahead of `electrum.digiscope.me`.
"""

# DigiByte-operated hosts, in the order the app should try them. Everything
# else keeps upstream's alphabetical order after these, to fail over to.
PREFERRED_ELECTRUM_HOSTS = [
    "electrum.digiscope.me",
]


def sort_electrums_preferred_first(data, sort_key):
    """Upstream's alphabetical sort, with [PREFERRED_ELECTRUM_HOSTS] first."""

    def rank(entry):
        host = str(entry.get(sort_key, "")).split(":")[0]
        if host in PREFERRED_ELECTRUM_HOSTS:
            return PREFERRED_ELECTRUM_HOSTS.index(host)
        return len(PREFERRED_ELECTRUM_HOSTS)

    return sorted(data, key=lambda entry: (rank(entry), str(entry.get(sort_key, ""))))
