# password-generator

A very simple password generator cli program written in python. Can output to a file or stdout and should work on a base python installation.

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

Output a single secure password composed of text and numbers to the console with default length (16)

```bash
password-generator
```

Output 20 secure passwords of length 20 composed of symbols, text, and numbers; to a file called passwords.txt

```bash
password-generator --number 20 --length 20 --symbols --output-file passwords.txt
```
