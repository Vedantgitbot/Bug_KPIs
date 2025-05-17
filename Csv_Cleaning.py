import pandas as pd

CSV_FILE = "updated_bug_tracker_data.csv"

REQUIRED_COLUMNS = [
    'issue_id', 'title', 'status', 'priority', 'assignee',
    'created_at', 'resolved_at', 'description'
]

def load_issues():
    try:
        df = pd.read_csv(CSV_FILE)
        for col in REQUIRED_COLUMNS:
            if col not in df.columns:
                df[col] = None
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        df['resolved_at'] = pd.to_datetime(df['resolved_at'], errors='coerce')
        df.dropna(subset=['issue_id', 'title', 'status', 'priority', 'assignee', 'created_at'], inplace=True)
        df['description'] = df['description'].fillna('No description provided').astype(str).str.strip()
        df = df.drop_duplicates(subset=['issue_id'], keep='last')
        return df
    except Exception as e:
        print(f"[CSV Loader] Error: {e}")
        return pd.DataFrame(columns=REQUIRED_COLUMNS)

def save_issue(row_dict):
    try:
        df = load_issues()
        new_row = {col: row_dict.get(col, "") for col in REQUIRED_COLUMNS}
        new_row['created_at'] = pd.to_datetime(new_row['created_at'], errors='coerce')
        new_row['resolved_at'] = pd.to_datetime(new_row['resolved_at'], errors='coerce') if new_row['resolved_at'] else None
        new_row['description'] = new_row['description'] or 'No description provided'
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)
    except Exception as e:
        print(f"[CSV Saver] Error: {e}")
