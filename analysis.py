# 22f2000199@ds.study.iitm.ac.in
# Marimo notebook: interactive demo showing relationship between variables
# (This file is a Marimo notebook stored as plain Python.)

import marimo as mo
import statistics
import random

# ---- Cell 1: Base data ----
# This cell creates the base dataset. Other cells depend on `data`.
# Data flow: data -> subset -> stats -> md
data = [round(random.gauss(50, 15), 2) for _ in range(100)]
# (In a real notebook you'd load a CSV or dataframe here.)

# ---- Cell 2: Interactive slider ----
# Slider controls how many points to show from `data`.
# This cell defines `slider`, which is referenced by `subset`.
slider = mo.ui.slider(1, 100, value=20)  # start=1, stop=100, default 20

# ---- Cell 3: Dependent variable (subset) ----
# This cell depends on `data` and `slider`.
# When slider.value changes, marimo will re-run this cell and downstream cells.
subset = data[: slider.value]

# ---- Cell 4: Computed stats (depends on subset) ----
# Compute simple statistics from the subset.
mean_val = statistics.mean(subset) if subset else 0
median_val = statistics.median(subset) if subset else 0
n = len(subset)

# ---- Cell 5: Dynamic Markdown output (depends on slider, mean_val, subset) ----
# This outputs reactive markdown that updates automatically when slider moves.
mo.md(
    f"# Interactive Marimo demo\n\n"
    f"Showing first **{slider.value}** values (n={n})\n\n"
    f"- Mean: **{mean_val:.2f}**\n"
    f"- Median: **{median_val:.2f}**\n\n"
    f"Values: `{subset}`\n\n"
    f"{'🟢' * min(slider.value, 50)}"
)
