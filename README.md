# password-generator

A very simple password generator cli program written in python. Can output to a file, your clipboard, or stdout.

## Installation

Locally install into your python environment. Below are instructions when using pip (others such as uv or poetry should work)

1. Clone the Repo
```bash
git clone https://github.com/Sparkx120/password-generator.git
cd password-generator
```
2. Install the package using pip
```bash
pip install .
```

## Usage

Output a single secure password to the console with default length (16)

```bash
password-generator
```

Output 20 secure passwords of lenght 20 with symbols and text and numbers to a file called passwords.txt

```bash
password-generator --number 20 --length 20 --symbols --output-file passwords.txt
```
