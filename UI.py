from dash import html, dcc, dash_table
from Styles import input_style, button_style, container_style

layout = html.Div([
    html.H1("Issue Tracker Dashboard"),

    html.Div([
        html.H3("Manage Issues (Add / Delete)"),
        html.Div(" To Add: Fill 'Title' and other fields."),
        html.Div(" To Delete: Enter 'Issue ID' and leave 'Title' blank."),
        html.Br(),
        
        dcc.Input(id="issue_id", placeholder="Issue ID (e.g., AB1234)", type="text", style=input_style),
        dcc.Input(id="title", placeholder="Issue Title (Leave blank to Delete)", type="text", style=input_style),
        dcc.Input(id="status", placeholder="Open/In Progress/Closed", type="text", style=input_style),
        dcc.Input(id="priority", placeholder="High/Medium/Low", type="text", style=input_style),
        dcc.Input(id="assignee", placeholder="Assigned To", type="text", style=input_style),
        dcc.Input(id="created_at", placeholder="YYYY-MM-DD", type="text", style=input_style),
        dcc.Input(id="resolved_at", placeholder="YYYY-MM-DD or blank", type="text", style=input_style),
        dcc.Input(id="description", placeholder="Issue Description", type="text", style=input_style),
        
        html.Button("Submit", id="submit_button", n_clicks=0, style=button_style),
        html.Div(id="form_response")
    ], style={"marginBottom": "20px", "marginTop": "10px"}),

    html.H3("Issues Table"),
    dash_table.DataTable(id="issue_table", page_size=10, style_table={"overflowX": "auto"}),

    html.Div([
        html.H3("Issue KPIs"),
        dcc.Graph(id="status_graph"),
        dcc.Graph(id="priority_graph"),
        dcc.Graph(id="timeline_graph"), 
        dcc.Graph(id="resolution_graph"),
        dcc.Graph(id="assignee_graph")
    ])
], style=container_style)
