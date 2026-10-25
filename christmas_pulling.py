import base64
import json
from pathlib import Path
import random
import sys

NAMES = [
    ("Gyula", 0),
    ("Eszterág", 0),
    ("Tibor", 1),
    ("Petra", 1),
    ("Dani", 1),
    ("Bence", 2),
    ("Adél", 2),
    ("Ábel", 3),
    ("Eszter", 3),
    ("Józsi", 4),
    ("Lili", 4),
]


def shuffle_assignments() -> list[tuple[str, str]]:
    names = NAMES.copy()
    while True:
        random.shuffle(names)
        if all(
            names[index][1] != names[(index + 1) % len(names)][1]
            for index in range(len(names))
        ):
            return [
                (names[index][0], names[(index + 1) % len(names)][0])
                for index in range(len(names))
            ]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    result_path = Path(__file__).with_name("result.json")
    assignments = shuffle_assignments()
    codes = iter(
        random.sample(range(10000), len(assignments))
    )
    result = [
        {
            "person": giver,
            "code": f"{next(codes):04d}",
            "pulled": base64.b64encode(receiver.encode("utf-8")).decode("ascii"),
        }
        for giver, receiver in assignments
    ]
    result_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Az új véletlenszerű húzás elkészült: {result_path}")
    print("Személyes kódok:")
    for assignment in result:
        print(f"- {assignment['person']}: {assignment['code']}")