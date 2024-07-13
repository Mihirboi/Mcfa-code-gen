import random
import string

def generate_fake_xbox_codes(num_codes):
    codes = []
    for i in range(num_codes):
        # Generate a random code of length 25
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))
        # Ensure that the code starts with XBL
        code = 'XBL' + code
        codes.append(code)
    return codes


def main():
    num_codes = int(input("Enter the number of  Xbox codes you want to generate: "))
    codes = generate_fake_xbox_codes(num_codes)
    for code in codes:
        print(code)


if __name__ == "__main__":
    main()
