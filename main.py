import os
from pathlib import Path

SENTENCE = "On rainy afternoons Grandma let me stir the rice porridge with her wooden spoon, too big for my small hands, while the radio crackled and steam fogged the kitchen window where I had drawn my name."

def get_output_dir():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    output_dir = get_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(SENTENCE, encoding="utf-8")
