import os

file_path = r"C:\Users\ishan\Documents\Projects\Awesome-Data-Centric-AI\README.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# First block replacement
first_old = """```mermaid
[Ad-Hoc Model-Centric Era] ───> [Automated Label Auditing (Cleanlab, 2021)] ───> [Synthetic Data Curations (Self-Instruct)] ───> [RLVR Programmatic Hard-locks](Unvetted Noise & Baseline Drops)      (Programmatic Label Quality Scans)            (Web-Scale High-Fidelity Generations)        (Compiler-Verified Quality Gates)
```"""

first_new = """```mermaid
flowchart LR
    A["Ad-Hoc Model-Centric Era (Unvetted Noise & Baseline Drops)"] --> B["Automated Label Auditing (Cleanlab, 2021) (Programmatic Label Quality Scans)"]
    B --> C["Synthetic Data Curations (Self-Instruct) (Web-Scale High-Fidelity Generations)"]
    C --> D["RLVR Programmatic Hard-locks (Compiler-Verified Quality Gates)"]
```"""

# Second block replacement
second_old = """```mermaid
The Continuous Data-Centric Engineering Loop[Raw Data Ingestion] ───> [Confident Learning Scan] ───> [Prune Redundant Elements via CoreSet]│▼[Optimal Post-Training Alignment] <─── [RLVR Quality Gate Check] <─── [Generate Synthetic Edge Cases]
```"""

second_new = """```mermaid
flowchart TB
    A["Raw Data Ingestion"] --> B["Confident Learning Scan"]
    B --> C["Prune Redundant Elements via CoreSet"]
    C --> D["Generate Synthetic Edge Cases"]
    D --> E["RLVR Quality Gate Check"]
    E --> F["Optimal Post-Training Alignment"]
```"""

if first_old in content:
    content = content.replace(first_old, first_new)
    print("First block replaced.")
else:
    print("First block NOT found. Might be due to newline variations.")
    # Let's try splitting the old block's line 15 by `\n` to see if there was a hidden newline.

if second_old in content:
    content = content.replace(second_old, second_new)
    print("Second block replaced.")
else:
    print("Second block NOT found.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
