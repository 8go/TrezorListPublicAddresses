# :page_with_curl: TrezorListPublicAddresses :lock:

This is a tiny utility tool to list batches of public Bitcoin addresses from your Trezor device. 
This small Python program by default lists the first 100 public Bitcoin addresses for the first 3 
accounts for all 3 address types (classic 1-addresses, p2sh-segwit 3-addresses, and native segwit bc1-addresses).

# Features

* You can print batches of public Bitcoin addresses, any number you want, 10, 100, 1000 or higher.
* You can print BIP44, BIP49 and BIP84 addresses. I.e. you can list classic 1-addresses, p2sh-segwit 3-addresses, and/or native segwit bc1-addresses.
* You can print the addresses for multiple accounts.
* You can print external and internal (change) addresses.
* It works offline. No internet needed.
* Just one small file of about 4KB.
* Easy to verify correctness yourself. This program really just has a single line of interesting code,
where it calls `btc.get_address(...)` from the Python trezorlib repeatedly with some 
appropriate arguments to ask the Trezor device for the public Bitcoin addresses.
* Works with Trezor passphrases, allows passphrase to be entered on the device (i.e. the Trezor itself) resulting in highest level of security.
* Written in Python
* Open source, you can view it and modify it.
 
# Runtime requirements

  * [Trezor](https://www.trezor.io) device, or compatible hardware wallet device
  * [Python](https://www.python.org/) v3.4+
  * [trezorlib from trezor-firmware](https://github.com/trezor/trezor-firmware/tree/master/python/src/trezorlib), If you have [python-trezor](https://wiki.trezor.io/Using_trezorctl_commands_with_Trezor#Install_python-trezor) installed on your PC or if you have [trezorctl](https://wiki.trezor.io/Using_trezorctl_commands_with_Trezor) working, then you have this already installed. 

# Building

* These is nothing to build. It is just a single Python file. Copy it anywhere. 

# Running it, Using it

* After downloading or copying the file, change the file permissions such that you can execute the file. E.g. on Linux do a `chmod 544` or similar.
* Connect your Trezor device and start program with `TrezorListPublicAddresses.py` or `./TrezorListPublicAddresses.py` or `python TrezorListPublicAddresses.py` or `python3 TrezorListPublicAddresses.py`.
* If and only if desired you can edit it with your favorite text editor to change some parameters like amount of addresses, accounts, etc.
* Tell your friends :)

# Alternatives

If you don't like this program you can use the following alternatives:
* [trezorctl](https://wiki.trezor.io/Using_trezorctl_commands_with_Trezor), read also [How to create bulk of addresses](https://wiki.trezor.io/Create_a_bulk_of_addresses_using_the_trezorctl_command). This is ok for Trezor One. This works also for Trezor Model T if you have no passphrase or you are entering the passphrase on the host. However, `trezorctl` will *not* work (as of March 2020 with latest firmware updates) if you have a passphrase and want to enter it on the device, because in this case the Trezor Model T will ask you for the passphrase at the generation of *every single address*! However, entering the passphrass on the host, i.e. keyboard, is *not* the safest option, and hence not recommended for high security.
* If you have your extended public key for a given address type and a given account then you can use tools like these two to compute your public addresses. But just for getting addresses these tools are not as convenient. 
  * https://github.com/dan-da/hd-wallet-derive : offline, computes addresses given some info (e.g. xpub, xpriv, etc.)
  * https://github.com/dan-da/hd-wallet-addrs : offline computes addresses, online computes balances for some given input (xpub, xpriv, etc.)
  
</> on :octocat: with :heart:
