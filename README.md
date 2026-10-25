# Family Christmas Pulling

This project is for my family's Christmas pulling. It randomly assigns each
family member another person to buy a Christmas gift for. People in the same
group are not allowed to be assigned to each other. The assignments are
encoded as Base64 signals.

## How it works

- Run `python christmas_pulling.py` to create a new draw.
- The script writes the assignments to `result.json`.
- Open `index.html` in a browser to select a name and reveal that person's
  encoded result.
- Select a name to show its encoded value, then use the built-in decoder
  sequence to slowly cycle through every possible name before revealing the
  assigned person.