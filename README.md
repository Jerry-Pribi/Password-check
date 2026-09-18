# Password Checker

A desktop password-strength checker built with Python's `tkinter`, featuring a custom gradient background and styled UI elements via `customtkinter`.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

## Features

- **Gradient background** — a smooth hand-drawn color fade rendered directly on a `Canvas` (no images required).
- **Password strength scoring** based on:
  - Minimum length (8+ characters)
  - Extended length bonus (12+ characters)
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
  - Penalty for repeated characters (e.g. `"aaa"`)
- **Live feedback** — tells you exactly what's missing from your password (length, symbols, casing, etc.)
- **Custom-styled button** using `customtkinter` for a modern look, layered on top of the gradient canvas.

## Requirements

- Python 3.8+
- `customtkinter`

Install the dependency with:

```bash
pip install customtkinter
```

`tkinter` and `re` are part of the Python standard library, so no extra installation is needed for those.

## Usage

Run the app with:

```bash
python password_checker.py
```

1. Type a password into the input field.
2. Click **Check**.
3. Your password's strength level and any improvement suggestions will appear below the input field.

## Strength Levels

| Score | Level          |
|-------|----------------|
| 0     | Very Weak      |
| 1     | Weak           |
| 2     | Fair           |
| 3     | Good           |
| 4     | Strong         |
| 5     | Very Strong    |
| 6     | Ultra Strong Password  |

## How It Works

- **Gradient rendering:** `draw_gradient()` interpolates RGB values line-by-line between two hex colors and draws them onto the canvas using `create_line()`, simulating a smooth color fade (tkinter has no native gradient support).
- **Password validation:** `Check()` runs the password through a series of regex checks (`re.search`), incrementing or decrementing a score based on which character classes are present.
- **Result display:** Feedback is rendered as canvas text. On repeated checks, the existing text item is updated in place with `itemconfig()` rather than stacking new text on top of the old.

## Known Limitations

- This is a **rule-based** strength check, not a true security estimate — a password can pass every rule here and still be easy to guess (e.g. `Password1!`). For a more realistic strength estimate, consider integrating the [`zxcvbn`](https://github.com/dwolfhub/zxcvbn-python) library, which estimates actual crack time.
- The window is a fixed size and not resizable (`root.resizable(False, False)`).

## License

Free to use and modify for personal or educational purposes.
