#!/usr/bin/env python3

# This small utility program prints batches of public BITCOIN addresses.
# One can print BIP44, BIP49 and BIP84 addresses for multiple accounts.
# One can print external and internal (change) addresses.
# This program really just has a single line of interesting code,
# where it calls btc.get_address(...) from the Python trezorlib
# repeatedly with some appropriate arguments to ask the Trezor device
# for the public Bitcoin addresses.
#
# Copyright (C) 2020
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# See <https://www.gnu.org/licenses/lgpl-3.0.html>.

from trezorlib.client import get_default_client
from trezorlib.tools import parse_path
from trezorlib import btc
from trezorlib import messages
import sys
import logging

def main():
    coins = ["Bitcoin"] # See trezorlib to see what Bitcoin-compatible coins are supported, e.g. "Litecoin". Putting Ethereum, Monero, Ripple here will NOT work unless you make other changes to this program!
    showOnScreen = False # Show address also on screen of Model T, True or False; turned off
    amountOfAddresses = 100 # number of addresses to be printed. Number of addresses up to 1000000 is ok, for addresses 1000001 or larger Model T gives Warning on screen
    bips = ["44","49","84"] # for BTC use "44","49", and/or "84". Other coins might use other values.
    cointType = "0" # Bitcoin uses "0" real network, i.e. mainnet; "1" test network. Other coins might use other values.
    accounts = ["0", "1", "2"] # accounts up to 20 is ok, for accounts 21 or larger Model T gives Warning on screen
    changeTypes = ["0", "1"] # Bitcoin uses 0 for external and 1 for internal=change. Other coins might use other values.

    logging.basicConfig(stream=sys.stderr, level=logging.WARNING) # INFO, DEBUG

    # Use first connected device
    client = get_default_client()

    # Print out Trezor's features and settings
    logging.debug(client.features)

    for coin in coins:
        logging.debug("======== Addresses for coin %s ========", coin)

        for bip in bips:
          logging.debug("======== Addresses for BIP %s ========", bip)

          for account in accounts:
              logging.debug("======== Addresses for account %s========", account)

              for changeType in changeTypes:
                  logging.debug("======== Addresses for change type %s (0=external, 1=internal/change) ========", changeType)

                  # Printing addresses from 0 up to amountOfAddresses
                  for addressIndex in range(amountOfAddresses+1):

                      pathString = bip + "'/" + cointType + "'/" + account + "'/" + changeType + "/" + str(addressIndex)
                      bip32_path = parse_path(pathString)
                      # script_type: 0...bip44..."address", 4...bip49..."p2shsegwit", 3...bip84..."segwit"
                      # script_type: messages.InputScriptType.SPENDADDRESS, messages.InputScriptType.SPENDWITNESS, messages.InputScriptType.SPENDP2SHWITNESS
                      # get_address(client,coin_name,address_n,show_display=False,multisig=None,script_type=messages.InputScriptType.SPENDADDRESS,)
                      if bip == "44":
                          scriptType = messages.InputScriptType.SPENDADDRESS
                      elif bip == "49":
                          scriptType = messages.InputScriptType.SPENDP2SHWITNESS
                      elif bip == "84":
                          scriptType = messages.InputScriptType.SPENDWITNESS
                      else:
                          sys.exit("Error: Unknown bip, unknown purpose-field %s in BIP32 address path. Quitting.", bip)

                      address = btc.get_address(client, coin, bip32_path, showOnScreen, multisig=None, script_type=scriptType)
                      print("Coin: %s, path: m/%s, address: %s" % (coin, pathString, address))

if __name__ == "__main__":
    main()
