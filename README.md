
# Issue Tracker Dashboard

A lightweight and interactive issue tracking dashboard built using **Dash**, **Pandas**, and **Plotly**. It supports direct CSV-based data entry, deletion, and real-time visualization of key metrics.

## Features

- Add or delete issues through a form interface
- Data stored and updated in a local CSV file
- Live KPIs and charts:
  - Issues by status
  - Priority distribution
  - Timeline of created issues
  - Resolved vs pending issues
  - Issues per assignee
- Dark neon-themed UI for better readability

## Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/issue-tracker-dashboard.git
   cd issue-tracker-dashboard
````

2. **Install dependencies**
   ```bash
   pip install dash pandas plotly
   ```

3. **Run the app**

   ```bash
   python Main.py
   ```

   Open [http://localhost:8050](http://localhost:8050) in your browser.

## File Overview

* `Main.py` – App logic and callbacks
* `UI.py` – Layout components
* `Styles.py` – Input/button/theme styles
* `Graph.py` – Plotly graphs for KPIs
* `Csv_Cleaning.py` – CSV read/write logic
* `updated_bug_tracker_data.csv` – Persistent storage

## Author

**Vedant Brahmbhatt**

