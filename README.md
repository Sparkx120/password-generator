# password-generator

A simple password generator cli program written in python. Can output to a file, your clipboard, or stdout.

## Usage

Output a single secure password to the console with default length (16)

```bash
./password-generator.py
```

Output 20 secure passwords of lenght 20 with symbols and text and numbers to a file called passwords.txt

```bash
./password-generator.py --number 20 --length 20 --symbols --output-file passwords.txt
```
