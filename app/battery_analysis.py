import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

def analyze_battery_csv(filepath, output_dir="uploads"):
    df = pd.read_csv(filepath)

    # Clean column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Drop empty or unnamed columns
    df.dropna(axis=1, how='all', inplace=True)
    df = df.loc[:, ~df.columns.str.contains('^unnamed')]

    # Detect key columns
    voltage_cols = [col for col in df.columns if "volt" in col]
    capacity_cols = [col for col in df.columns if "cap" in col]
    cycle_cols = [col for col in df.columns if "cycle" in col]
    time_cols = [col for col in df.columns if "time" in col or "timestamp" in col]

    # Plotting logic
    plots = []

    def save_plot(fig, name):
        path = os.path.join(output_dir, name)
        fig.savefig(path)
        plt.close(fig)
        plots.append(path)

    # Voltage vs Time
    if voltage_cols and time_cols:
        fig, ax = plt.subplots(figsize=(8, 5))
        for v in voltage_cols:
            ax.plot(df[time_cols[0]], df[v], label=v)
        ax.set_title("Voltage vs Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Voltage (V)")
        ax.legend()
        save_plot(fig, "voltage_time.png")

    # Capacity vs Cycle
    if capacity_cols and cycle_cols:
        fig, ax = plt.subplots(figsize=(8, 5))
        for c in capacity_cols:
            ax.plot(df[cycle_cols[0]], df[c], label=c)
        ax.set_title("Capacity vs Cycle")
        ax.set_xlabel("Cycle")
        ax.set_ylabel("Capacity (Ah)")
        ax.legend()
        save_plot(fig, "capacity_cycle.png")

    # Voltage vs Cycle
    if voltage_cols and cycle_cols:
        fig, ax = plt.subplots(figsize=(8, 5))
        for v in voltage_cols:
            ax.plot(df[cycle_cols[0]], df[v], label=v)
        ax.set_title("Voltage vs Cycle")
        ax.set_xlabel("Cycle")
        ax.set_ylabel("Voltage (V)")
        ax.legend()
        save_plot(fig, "voltage_cycle.png")

    # Capacity vs Time
    if capacity_cols and time_cols:
        fig, ax = plt.subplots(figsize=(8, 5))
        for c in capacity_cols:
            ax.plot(df[time_cols[0]], df[c], label=c)
        ax.set_title("Capacity vs Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Capacity (Ah)")
        ax.legend()
        save_plot(fig, "capacity_time.png")

    return plots
