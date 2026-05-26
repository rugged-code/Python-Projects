# NATO Phonetic Alphabet Generator

Convert any word (A-Z) into the NATO phonetic alphabet (Alpha, Bravo, ...).

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/pandas-Required-blue?style=flat-square&logo=pandas)
![Beginner-Friendly](https://img.shields.io/badge/Beginner-Friendly-brightgreen?style=flat-square)
![Exception Handling](https://img.shields.io/badge/Exception%20Handling-Added-orange?style=flat-square)

## Features

- Uses `nato_phonetic_alphabet.csv` as the source of truth.
- Converts your input to uppercase and maps each letter to its phonetic word.
- Handles invalid characters by printing a helpful message and asking again.

## Requirements

- Python 3.x
- `pandas`

## Setup

From this project folder:

```bash
pip install pandas
```

## Run

```bash
python main.py
```

### Example

If you enter:

```text
NATO
```

The program prints the list of phonetic words (based on your CSV values).

## What happens on invalid input?

If your input contains characters that aren't in `A-Z` (for example: digits, punctuation, or spaces),
the script catches the `KeyError` and prints:

```text
Invalid input. Please enter a valid word from the alphabets only.
```

Then it prompts you again by re-running the input flow.

## Files

- `main.py` - input loop + conversion logic + exception handling
- `nato_phonetic_alphabet.csv` - mapping of letters to NATO phonetic words

## How it works (quick)

1. `nato_phonetic_alphabet.csv` is loaded into a dictionary of `letter -> code`.
2. The script reads your input, uppercases it, and maps each character.
3. If a character is not in `A-Z`, a `KeyError` is raised, and the script prints a friendly error message and asks again.

## Note

Right now, "ask again" is implemented by re-calling the same input function (recursion). For normal use this is fine, but a loop-based approach would be more robust for repeated invalid inputs.

