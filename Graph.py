import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

NEON_GREEN = "#39FF14"
BACKGROUND_COLOR = "black"

def apply_common_layout(fig, title=""):
    fig.update_layout(
        title=title,
        title_font_color=NEON_GREEN,
        plot_bgcolor=BACKGROUND_COLOR,
        paper_bgcolor=BACKGROUND_COLOR,
        font_color=NEON_GREEN,
        xaxis=dict(showgrid=False, linecolor=NEON_GREEN, tickfont=dict(color=NEON_GREEN)),
        yaxis=dict(showgrid=False, linecolor=NEON_GREEN, tickfont=dict(color=NEON_GREEN)),
        legend=dict(font=dict(color=NEON_GREEN)),
        margin=dict(l=40, r=40, t=60, b=40)
    )
    return fig

def generate_status_bar_chart(df):
    status_counts = df['status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    fig = px.bar(status_counts, x='Status', y='Count', color='Status', color_discrete_sequence=px.colors.qualitative.Bold)
    return apply_common_layout(fig, "Issues by Status")

def generate_priority_pie_chart(df):
    priority_counts = df['priority'].value_counts().reset_index()
    priority_counts.columns = ['Priority', 'Count']
    fig = px.pie(priority_counts, values='Count', names='Priority', color_discrete_sequence=px.colors.qualitative.Set3)
    return apply_common_layout(fig, "Issue Distribution by Priority")

def generate_issues_over_time(df):
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    monthly_df = df['created_at'].dt.to_period('M').value_counts().sort_index().reset_index()
    monthly_df.columns = ['Month', 'Issue Count']
    monthly_df['Month'] = monthly_df['Month'].astype(str)
    fig = px.line(monthly_df, x='Month', y='Issue Count', markers=True, line_shape='spline', color_discrete_sequence=[NEON_GREEN])
    return apply_common_layout(fig, "Issues Created Over Time")

def generate_resolution_status_pie(df):
    resolved = df['resolved_at'].notna().sum()
    unresolved = df['resolved_at'].isna().sum()
    fig = go.Figure(data=[go.Pie(labels=['Resolved', 'Pending'], values=[resolved, unresolved], hole=0.5, marker_colors=[NEON_GREEN, '#FF073A'])])
    return apply_common_layout(fig, "Resolved vs Pending Issues")

def generate_assignee_bar(df):
    assignee_counts = df['assignee'].value_counts().reset_index()
    assignee_counts.columns = ['Assignee', 'Count']
    fig = px.bar(assignee_counts, x='Assignee', y='Count', color='Assignee', color_discrete_sequence=px.colors.qualitative.D3)
    return apply_common_layout(fig, "Issues per Assignee")
