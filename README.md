# Algorithm_HW3_huffman_code
Learn how to use Python to implement the Huffman code.

#### There are two function of this program.

1. Encoder : Convert digit 0~9 to huffman code.
2. Decoder : Convert huffman code to digit 0~9

## How to use

1. Encoder:
    python huffman.py -e  # Should to tell the program you want to use encoder by typing the sequence '-e'.

2. Decoder(default):
    python huffman.py     # I set the decoder default
    python huffman.py -d  # You don't need to typing the sequence '-d' when you want to use decoder.

## Input type

    0.0239 0.1470 0.1450 0.0735 0.1212 0.0215 0.0639 0.1387 0.1200 0.1453  # First line is the weight of digit 0~9
    1011011100010011011111100000000000000  # Second line is a sequence need to be encode/decode.

## Output type

    886277341111  # The sequence after encode/decode.
