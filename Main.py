import dash
from dash import Input, Output, State
from datetime import datetime
from Csv_Cleaning import load_issues, save_issue
from Graph import (
    generate_status_bar_chart,
    generate_priority_pie_chart,
    generate_issues_over_time,
    generate_resolution_status_pie,
    generate_assignee_bar
)
from UI import layout
import pandas as pd
import random
import string

app = dash.Dash(__name__)
app.title = "Issue Tracker Dashboard"
app.layout = layout

def generate_random_issue_id(existing_ids):
    while True:
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=4))
        new_id = f"{letters}{numbers}"
        if new_id not in existing_ids:
            return new_id

@app.callback(
    Output("form_response", "children"),
    Input("submit_button", "n_clicks"),
    State("issue_id", "value"),
    State("title", "value"),
    State("status", "value"),
    State("priority", "value"),
    State("assignee", "value"),
    State("created_at", "value"),
    State("resolved_at", "value"),
    State("description", "value")
)
def manage_issue(n_clicks, issue_id, title, status, priority, assignee, created, resolved, description):
    if not n_clicks:
        return ""
    
    df = load_issues()

   
    if issue_id and not title:
        if issue_id in df['issue_id'].values:
            df = df[df['issue_id'] != issue_id]
            df.to_csv("/Users/vedantbrahmbhatt/Desktop/Bug_Fix_Dash/updated_bug_tracker_data.csv", index=False)
            return f"Issue {issue_id} deleted successfully."
        else:
            return f"Issue ID {issue_id} not found. Cannot delete."
    
    
    if title:
        try:
            existing_ids = df['issue_id'].tolist()
            new_issue_id = generate_random_issue_id(existing_ids)
            created_dt = datetime.strptime(created, "%Y-%m-%d")
            resolved_dt = datetime.strptime(resolved, "%Y-%m-%d") if resolved else None
            save_issue({
                "issue_id": new_issue_id,
                "title": title,
                "status": status,
                "priority": priority,
                "assignee": assignee,
                "created_at": created_dt,
                "resolved_at": resolved_dt,
                "description": description or "No description provided"
            })
            return f"Issue {new_issue_id} added successfully."
        except Exception as e:
            return f"Error: {e}"

    return "Please enter valid inputs."

@app.callback(
    Output("issue_table", "data"),
    Output("issue_table", "columns"),
    Output("status_graph", "figure"),
    Output("priority_graph", "figure"),
    Output("timeline_graph", "figure"),
    Output("resolution_graph", "figure"),
    Output("assignee_graph", "figure"),
    Input("submit_button", "n_clicks")
)
def update_dashboard(n_clicks):
    df = load_issues()
    table_data = df.to_dict("records")
    table_columns = [{"name": col, "id": col} for col in df.columns]

    return (
        table_data,
        table_columns,
        generate_status_bar_chart(df),
        generate_priority_pie_chart(df),
        generate_issues_over_time(df),
        generate_resolution_status_pie(df),
        generate_assignee_bar(df)
    )

if __name__ == "__main__":
    app.run(debug=True)
