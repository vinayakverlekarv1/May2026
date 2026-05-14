def decode_ascii(encoded: str) -> str:
    return ''.join(chr(int(code)) for code in encoded.split('-'))

print(decode_ascii("72-101-108-108-111"))  # Hello