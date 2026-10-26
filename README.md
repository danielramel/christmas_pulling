# Family Christmas Draw

This project randomly assigns each family member another person to buy a
Christmas gift for. People in the same group cannot be assigned to each other.
Each assignment uses a manually assigned keyphrase. Because this is a static
GitHub Pages site, this provides casual privacy only: anyone who inspects
`result.json` can still discover all assignments.

## Usage

- Run `python christmas_pulling.py` to create a new draw.
- The script writes the assignments to `result.json`.
- Fill in a unique `keyphrase` for each person in `result.json`.
- Send each person only their own keyphrase.
- They open the GitHub Pages site, enter their keyphrase, confirm their name, and
  reveal the person assigned to them.