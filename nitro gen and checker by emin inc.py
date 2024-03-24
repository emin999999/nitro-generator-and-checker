import random
import string
import requests

print("Owned By Emin INC.")
print("Nitro Generator And Checker 1.0")
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

def save_valid_codes(codes):
    with open("valid_gift_codes.txt", "a") as file:
        for code in codes:
            file.write(code + "\n")

def main():
    num_codes = int(input("Üretecek kod miktarını girin: "))
    codes = generate_gift_codes(num_codes)
    
    print("Kodların geçerliliği kontrol ediliyor...")
    valid_codes = []
    for code in codes:
        if check_code_validity(code):
            print(f"{code} - Geçerli")
            valid_codes.append(code)
        else:
            print(f"{code} - Geçersiz")
    
    if valid_codes:
        save_valid_codes(valid_codes)
        print("Geçerli kodlar 'valid_gift_codes.txt' dosyasına kaydedildi.")

if __name__ == "__main__":
    main()
