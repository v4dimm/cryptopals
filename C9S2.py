def pad_block(text, block_size):
    if len(text) < block_size:
        difference = block_size - len(text)
        text += bytes([difference] * difference)
    
    return text


if __name__ == "__main__":
    text = b"YELLOW SUBMARINE"
    print(pad_block(text, 20))