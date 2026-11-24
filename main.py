"""Write a two-line explanation of rain to /output/entry.txt.

Line 1 explains rain to a 10-year-old through one vivid analogy.
Line 2 says why that analogy works: what it maps and what it leaves out.
"""

import os

LINE_1 = (
    "Rain is the sky wringing out a giant sponge it soaked up from the sea, "
    "letting the water drip back down in millions of tiny drops."
)

LINE_2 = (
    "The sponge maps how clouds gather water and let it go a little at a "
    "time, but it leaves out that clouds are floating water vapour, not "
    "cloth, and that cooling air, not hands, squeezes the rain out."
)


def main() -> None:
    text = LINE_1 + "\n" + LINE_2 + "\n"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
