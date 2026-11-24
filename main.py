import os

LINES = [
    "Do not buy the cheap umbrella. It will invert in the first wind.",
    "Buy two, because you will lose the first one the same week anyway.",
]

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = "\n".join(LINES)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {os.path.join(out_dir, 'entry.txt')} ({len(text)} characters)")

if __name__ == "__main__":
    main()
