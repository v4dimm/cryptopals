from requests import get

def get_cipher_blocks():
    text = get('https://cryptopals.com/static/challenge-data/8.txt').text
    ciphertext = [bytes.fromhex(line.strip()) for line in text.split('\n')]
    return ciphertext


def get_repeating_block(ciphertext, block_size):
    numbers = []

    for block in ciphertext:
        chunks = [block[i:i + block_size] for i in range(0, len(block), block_size)]
        repeating = len(chunks) - len(set(chunks))
        numbers.append({
            'repeating': repeating,
            'block': block
        })
    
    most_repeating_block = sorted(numbers, key=lambda x: x['repeating'], reverse=True)[0]
    return most_repeating_block


def main():
    block_size = 16

    cipher_blocks = get_cipher_blocks()
    block = get_repeating_block(cipher_blocks, block_size)
    return block


if __name__ == "__main__":
    print(main())