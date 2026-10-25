# Family Christmas Draw

This project randomly assigns each family member another person to buy a
Christmas gift for. People in the same group cannot be assigned to each other.
Assignments are stored as Base64-encoded signals.

## Usage

- Run `python christmas_pulling.py` to create a new draw.
- The script writes the assignments to `result.json`.
- Open `index.html` in a browser, select your name, and reveal the person
  assigned to you.