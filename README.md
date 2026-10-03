# Personal Expense Tracker (CLI)

A lightweight, terminal-based **Personal Expense Tracker** built with Python. This application allows users to log daily financial transactions, categorize expenses dynamically, and view structural real-time summaries with multi-category breakdown aggregates.

---

## Key Features

* **Data Persistence:** Automatically stores data locally using a structured, tabular standard layout (`CSV`) without needing complex third-party databases.
* **Dynamic Breakdown Summaries:** Utilizes advanced hashing concepts (Python dictionaries) to aggregate spending across infinite custom user-defined categories dynamically.
* **Robust Input Validation:** Wrapped inside structured operational `try-except` blocks to proactively prevent script crashes from faulty string injections during numeric entries.
* **Cross-Platform Compatibility:** Configured with universal end-of-line abstractions (`newline=''`) to execute identically across Windows, macOS, and Linux kernels.

---

## Architecture & Data Flow

```text
       +------------------------------------+

       |       Terminal UI Menu Loop        |
       +------------------------------------+
              /                      \
      (Option 1)                 (Option 2)
            v                          v
  +------------------+       +------------------+

  |  add_expense()   |       |  view_summary()  |
  +------------------+       +------------------+

            |                          |
    [Validates input]          [Parses Rows via]
    [Appends data row]         [Hash Dictionary]

            |                          |
            v                          v
  +---------------------------------------------+

  |                expenses.csv                 |
  +---------------------------------------------+
```

1. **Initialization:** The script attempts an exclusive creation (`'x'` mode) flag layout to safely instantiate a clean ledger file with a standardized header schema without erasing historical storage.
2. **Writing Data:** Captures timestamps on the fly using `datetime` collections and serializes inputs safely into structural entries using the Python `csv` package pipeline.
3. **Reading Data:** Streams historical rows directly through a continuous memory loop, skipping tracking indices headers to calculate operational statistics instantly.

---

## Technical Defense Insights (For Reviewers)

* **Why CSV instead of SQLite?** CSV offers structural integrity inside an human-readable document form. It leaves zero deployment footprints, meaning it can be opened directly inside Excel or Google Sheets for independent accounting workflows right out of the box.
* **Error Prevention Strategy:** A custom `ValueError` trap is explicitly designed within data intake operations. If a malicious or accidental non-numeric string string (e.g. `"abc"`) is parsed, the execution safely flags the error and returns to root loops gracefully rather than terminating the session.
* **Algorithmic Complexity:** Tracking breakdowns are achieved in **O(N) linear time** relative to the file size using dynamic dictionary lookup algorithms, preventing slow matrix lag over extended usage periods.

---

## Quick Start & Installation

### Prerequisites
Make sure you have **Python 3.x** installed on your workstation.

### Step-by-Step Launch
1. Clone or download this project folder onto your local directory layout.
2. Open your command prompt or terminal and navigate into the folder directory:
   ```bash
   cd personal-expense-tracker
   ```
3. Boot the tracking terminal program directly:
   ```bash
   python main.py
   ```

---

## Core Project Structure
```text
personal-expense-tracker/
│
├── .gitignore          # Safeguards temporary cache and data files from versioning
├── main.py             # Principal Python script housing operational structures
└── README.md           # Professional project blueprint and overview document
```
