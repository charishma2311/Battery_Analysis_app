import plotly.express as px
import pandas as pd

def generate_plot(df: pd.DataFrame):
    fig = px.line(df, x=df.columns[0], y=df.columns[1], title="Battery Analysis")
    return fig.to_html(full_html=False)
