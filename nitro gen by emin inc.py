import random
import string
import requests

def generate_code(length=19):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

def generate_gift_codes(num_codes):
    codes = []
    for _ in range(num_codes):
        code = generate_code()
        code = 'https://discord.gift/' + code
        codes.append(code)
    return codes

def check_code_validity(code):
    url = f"https://discord.com/api/v8/entitlements/gift-codes/{code.split('/')[-1]}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def main():
    num_codes = int(input("Üretecek kod miktarını girin: "))
    codes = generate_gift_codes(num_codes)
    
    print("Kodların geçerliliği kontrol ediliyor...")
    for code in codes:
        if check_code_validity(code):
            print(f"{code} - Geçerli")
        else:
            print(f"{code} - Geçersiz")

if __name__ == "__main__":
    main()

