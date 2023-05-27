# Remove Password from OpenSSL or P12 Certificates

This Python script removes the password from OpenSSL or P12 certificates and saves them as a new file. The script uses the `cryptography` library to decrypt the certificate.

## Usage

To use the script, run the following command:

```bash
python openssl_decrypter.py file_path [--output output_path] [--password password]
```

- `file_path` (required): the path to the certificate file that you want to decrypt.
- `--output` (optional): the path to the output file where you want to save the decrypted certificate. If not specified, the script will save the new file with "_nopassword" appended to the original file name in the same directory as the original file.
- `--password` (optional): the password for the certificate. If not specified, the script will prompt for a password.

## Requirements

This script requires the `cryptography` library. You can install it using `pip`:

```bash
pip install cryptography
```

## Limitations

This script currently only supports OpenSSL or P12 certificates.

## Examples

Here are some examples of how to use the script:

```bash
# Remove password from an OpenSSL certificate with a specified password
python openssl_decrypter.py mycert.pem --password mypassword

# Remove password from an OpenSSL certificate witha specified output file
python openssl_decrypter.py mycert.pem --output mycert_nopassword.pem --password mypassword

# Remove password from an OpenSSL certificate and save it in the same directory as the original file
python openssl_decrypter.py /path/to/mycert.pem

# Remove password from a P12 certificate
python openssl_decrypter.py mycert.p12 --output mycert_nopassword.p12 --password mypassword
```

## License

This code is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions to this project are welcome. If you find any issues or have ideas for new features, please open an issue or submit a pull request.

## Credits

This script was created by [SeregonWar].
