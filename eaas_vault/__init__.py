from argparse import ArgumentParser

from hvac import Client as VaultClient


argument_parser = ArgumentParser()
argument_parser.add_argument('-t', '--token', help='Root token', required=True)
argument_parser.add_argument(
    '--vault-addr', help='Vault address', default='http://localhost:8200')
cli_args = argument_parser.parse_args()

vault = VaultClient(url=cli_args.vault_addr, token=cli_args.token)

while vault.is_sealed():
    print('Vault is sealed!')
    vault.unseal(input('key: '))

print('Is Vault Sealed?', vault.is_sealed())
