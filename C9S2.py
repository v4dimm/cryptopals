def pad_block(text, block_size):
    if len(text) < block_size:
        difference = block_size - len(text)
        text += bytes([difference] * difference)
    
    return text


def pad_text(text, block_size):
    blocks = [text[i:i+block_size] for i in range(0, len(text), block_size)]
    blocks[-1] = pad_block(blocks[-1], block_size)
    return b''.join(blocks)


if __name__ == "__main__":
    text = b"YELLOW SUBMARINE"
    print(pad_block(text, 20))