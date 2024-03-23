import random
import string
import requests

def generate_code(length=19):
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

def generate_gift_codes(num_codes):
    codes = []
    for _ in range(num_codes):
        code = generate_code()
        code = 'https://discord.gift/' + code
        codes.append(code)
    return codes

def main():
    num_codes = int(input("Üretilecek kod miktarını girin: "))
    codes = generate_gift_codes(num_codes)
    
    print("Üretilen Kodlar:")
    for code in codes:
        print(code)

if __name__ == "__main__":
    main()
