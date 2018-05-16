#!/usr/bin/python

from binascii import unhexlify

def hexToBase64(hex_str):
    byteSeq = unhexlify(hex_str)
    print byteSeq

if __name__ == "__main__":
    input_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    output_string = hexToBase64(input_string)
