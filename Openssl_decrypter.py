import argparse
import sys
import os
from cryptography.hazmat.backends import default_backend
default_backend = default_backend()
def main():
    parser = argparse.ArgumentParser(description='Remove password from openssl or p12 certificates')
    parser.add_argument('file_path', type=str, help='Path to certificate file')
    parser.add_argument('--output', '-o', type=str, help='Output path for certificate file', default=None)
    parser.add_argument('--password', '-p', type=str, help='Password foril certificato')
    args = parser.parse_args()

    # Verifica la presenza della libreria pyOpenSSL o cryptography
    try:
        from OpenSSL import crypto
    except ImportError:
        try:
            from cryptography.hazmat.primitives.serialization import load_pem_private_key, Encoding, PrivateFormat, NoEncryption
        except ImportError:
            print('Error: pyOpenSSL or cryptography library not found.')
            return

    # Verifica se il file esiste
    if not os.path.exists(args.file_path):
        print(f'Error: file {args.file_path} not found')
        return

    # Verifica se il file è un certificato valido openssl o p12
    if not (args.file_path.lower().endswith('.p12') or args.file_path.lower().endswith('.pem') or args.file_path.lower().endswith('.key')):
        print(f'Error: file {args.file_path} is not a valid openssl or p12 certificate')
        return

    # Verifica se l'argomento --output è stato specificato
    if args.output and os.path.exists(args.output):
        print(f'Error: output file {args.output} already exists')
        return

    # Richiede la password se non fornita come argomento
    if not args.password:
        args.password = input('Enter password for certificate: ')

    # Rimuove la password dal certificatoContinuo la risposta al codice modificato:


    with open(args.file_path, 'rb') as f:
        cert_bytes = f.read()

    try:
        if args.file_path.lower().endswith('.p12'):

            cert = crypto.load_pkcs12(cert_bytes, args.password)

            if not args.output:
                args.output = os.path.splitext(args.file_path)[0] + '_nopassword.p12'

            with open(args.output, 'wb') as f:
                f.write(crypto.dump_pkcs12(cert, key=None))

        else:
            
            key = load_pem_private_key(cert_bytes, args.password.encode(), backend=default_backend())

            if not args.output:
                args.output = os.path.splitext(args.file_path)[0] + '_nopassword.pem'

            with open(args.output, 'wb') as f:
                f.write(key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()))

        print(f'Password removed successfully. Certificate saved to {args.output}')

    except ValueError as e:
        print('Error: invalid password')
    except Exception as e:
        print(f'Error removing password: {e}')
        sys.exit(0)