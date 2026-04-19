import argparse
import secrets
import string

SYMBOLS = "!@#$%^&*()"
ALPHABET = string.ascii_letters + string.digits


def generate_secure_string(len, extra_chars=""):
    secure_string = ''.join(secrets.choice(ALPHABET + extra_chars) for _ in range(len))
    return secure_string


def main():
    parser = argparse.ArgumentParser(description="Generates Random Passwords to stdout, or a file")
    parser.add_argument("-n", "--number", help="Number of passwords to generate", type=int, default=1)
    parser.add_argument("-l", "--length", help="Length of the password(s) to generate", type=int, default=16)
    parser.add_argument("-s", "--symbols", action="store_true", help="Include symbols in generated passwords")
    parser.add_argument("-o", "--output-file", help="Output File if you don't want to output to stdout")
    args = parser.parse_args()

    passwords = []

    for iterations in range(args.number):
        passwords.append(generate_secure_string(args.length, extra_chars=SYMBOLS if args.symbols else ""))

    if args.output_file:
        with open(args.output_file, "w",  encoding="utf-8") as f:
            for password in passwords:
                f.write(password + "\n")
            print(f"Passwords written to {args.output_file}")
    else:
        for password in passwords:
            print(password)

if __name__ == "__main__":
    main()
