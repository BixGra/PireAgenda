import numpy as np
from matplotlib import colormaps

from src.tools.html_base import CATEGORIES, root
from src.tools.db_refresh import *


cmap = colormaps["hsv"]
gradient = np.linspace(0, 1, len(CATEGORIES))


def to_256(value: float) -> int:
    return int(value * 255)


def to_256_tint_1(value: float) -> int:
    return int((value + (1 - value) / 2) * 255)


def to_256_tint_2(value: float) -> int:
    return int((value + 3 * (1 - value) / 4) * 255)


db_refresh()


with open("./src/style/categories.css", "w") as f:
    f.write(f"""body {{
    background-image: url("{root}/src/img/background.png");
    background-size: 128px;
}}
""")
    for g, category in zip(cmap(gradient), CATEGORIES):
        if category.name == "angledroit":
            pass
        else:
            f.write(f"""
.{category.name} {{
    background: {("#%02x%02x%02x" % (to_256_tint_1(g[0]), to_256_tint_1(g[1]), to_256_tint_1(g[2]))).replace("-", "")};
}}

.{category.name}:hover {{
    background: {("#%02x%02x%02x" % (to_256_tint_2(g[0]), to_256_tint_2(g[1]), to_256_tint_2(g[2]))).replace("-", "")};
}}""")

