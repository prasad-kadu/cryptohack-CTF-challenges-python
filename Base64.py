#base64.b64encode()
import base64
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

decode_hex = bytes.fromhex(hex_string)
print("The bytes we got after decode from the hex string", decode_hex)

decode_bytes = base64.b64encode(decode_hex)
print("The flag we got after decoding from bytes", decode_bytes)