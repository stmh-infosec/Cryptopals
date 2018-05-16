#!/usr/bin/python3
import binascii
import base64

# Expected input  String : "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
# Expected output String : "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def hexToBase64(hex_str):
	byteSeq = binascii.unhexlify(hex_str) #Coverts Hex string to Bytes
	encoded = base64.b64encode(byteSeq)
	return encoded
if __name__ == "__main__":
	input_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	output_string = hexToBase64(input_string)
	print(output_string)


