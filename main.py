"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to the entry output file.
Python 3 standard library only.
"""

import os

SENTENCE = (
    "The congressman who spent the morning grilling tech CEOs on "
    "accountability forwarded his own bill as a screenshot of a Word "
    "document and asked an intern to convert it, because the man writing "
    "the rules for the digital age still thinks Save As is a suggestion."
)


def resolve_output_path():
    """Resolve the output file path, honouring the documented env vars."""
    entry_output = os.environ.get("ENTRY_OUTPUT")
    if entry_output:
        return entry_output
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return os.path.join(os.sep, "output", "entry.txt")


def ensure_single_spacing(text):
    """Guard: no double spaces — a single sentence must be cleanly spaced."""
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    return text


def validate(text):
    """Gate: 1-320 UTF-8 characters, one sentence, not whitespace only."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if len(text) > 320:
        raise ValueError("entry exceeds 320 characters: %d" % len(text))
    stripped = text.strip()
    ensure_single_spacing(stripped)
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return stripped


def main():
    text = validate(SENTENCE)
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
