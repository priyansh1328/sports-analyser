"""
charts.py
Creates and saves all charts and graphs.
"""

import logging
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import pandas as pd

logger = logging.getLogger(__name__)

sns.set_theme(style="darkgrid")
CHARTS_DIR = "charts"


def _save(filename: str) -> None:
    """Save chart to the charts folder."""
    os.makedirs(CHARTS_DIR, exist_ok=True)
    path = os.path.join(CHARTS_DIR, filename)
    plt.savefig(path, bbox_inches="tight", dpi=150)
    logger.info("Chart saved: %s", path)
    plt.close()


def plot_top_batters(df: pd.DataFrame, n: int = 10) -> None:
    """Bar chart of top N batters by runs."""
    top = df.sort_values("Runs", ascending=False).head(n)
    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("rocket", len(top))
    bars = plt.bar(top["Player"], top["Runs"],
                   color=colors, edgecolor="white")
    plt.title(f"IPL Top {n} Run Scorers (All Time)",
              fontsize=16, fontweight="bold")
    plt.xlabel("Player", fontsize=12)
    plt.ylabel("Total Runs", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    for bar, val in zip(bars, top["Runs"]):
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + 50,
                 str(val), ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    _save("top_batters_runs.png")
    print("  ✅ Chart saved: charts/top_batters_runs.png")


def plot_strike_rate_vs_average(df: pd.DataFrame) -> None:
    """Scatter plot of strike rate vs batting average."""
    plt.figure(figsize=(12, 7))
    scatter = plt.scatter(
        df["Average"], df["Strike_Rate"],
        c=df["Runs"], cmap="YlOrRd",
        s=df["Runs"] / 30, alpha=0.8, edgecolors="gray"
    )
    for _, row in df.iterrows():
        plt.annotate(row["Player"].split()[-1],
                     (row["Average"], row["Strike_Rate"]),
                     textcoords="offset points",
                     xytext=(5, 5), fontsize=8)
    plt.colorbar(scatter, label="Total Runs")
    plt.title("Strike Rate vs Batting Average",
              fontsize=14, fontweight="bold")
    plt.xlabel("Batting Average", fontsize=12)
    plt.ylabel("Strike Rate", fontsize=12)
    plt.tight_layout()
    _save("strike_rate_vs_average.png")
    print("  ✅ Chart saved: charts/strike_rate_vs_average.png")


def plot_team_runs(df: pd.DataFrame) -> None:
    """Horizontal bar chart of total runs by team."""
    team_data = (
        df.groupby("Team")["Runs"]
        .sum()
        .sort_values(ascending=True)
    )
    plt.figure(figsize=(10, 6))
    colors = sns.color_palette("mako", len(team_data))
    bars = plt.barh(team_data.index, team_data.values,
                    color=colors, edgecolor="white")
    plt.title("Total IPL Runs by Team",
              fontsize=14, fontweight="bold")
    plt.xlabel("Total Runs", fontsize=12)
    for bar, val in zip(bars, team_data.values):
        plt.text(val + 50, bar.get_y() + bar.get_height() / 2,
                 str(val), va="center", fontsize=9)
    plt.tight_layout()
    _save("team_total_runs.png")
    print("  ✅ Chart saved: charts/team_total_runs.png")


def plot_top_bowlers(df: pd.DataFrame, n: int = 10) -> None:
    """Bar chart of top N bowlers by wickets."""
    top = df.sort_values("Wickets", ascending=False).head(n)
    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("flare", len(top))
    bars = plt.bar(top["Player"], top["Wickets"],
                   color=colors, edgecolor="white")
    plt.title(f"IPL Top {n} Wicket Takers (All Time)",
              fontsize=16, fontweight="bold")
    plt.xlabel("Player", fontsize=12)
    plt.ylabel("Total Wickets", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    for bar, val in zip(bars, top["Wickets"]):
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + 2,
                 str(val), ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    _save("top_bowlers_wickets.png")
    print("  ✅ Chart saved: charts/top_bowlers_wickets.png")


def plot_economy_vs_wickets(df: pd.DataFrame) -> None:
    """Scatter plot of economy rate vs wickets."""
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        df["Economy"], df["Wickets"],
        c=df["Wickets"], cmap="Blues",
        s=100, alpha=0.8, edgecolors="gray"
    )
    for _, row in df.iterrows():
        plt.annotate(row["Player"].split()[-1],
                     (row["Economy"], row["Wickets"]),
                     textcoords="offset points",
                     xytext=(5, 5), fontsize=8)
    plt.colorbar(scatter, label="Wickets")
    plt.title("Economy Rate vs Total Wickets",
              fontsize=14, fontweight="bold")
    plt.xlabel("Economy Rate", fontsize=12)
    plt.ylabel("Total Wickets", fontsize=12)
    plt.tight_layout()
    _save("economy_vs_wickets.png")
    print("  ✅ Chart saved: charts/economy_vs_wickets.png")


def plot_football_goals(df: pd.DataFrame, n: int = 10) -> None:
    """Bar chart of top N Premier League scorers."""
    top = df.sort_values("Goals", ascending=False).head(n)
    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("viridis", len(top))
    bars = plt.bar(top["Player"], top["Goals"],
                   color=colors, edgecolor="white")
    plt.title(f"Premier League Top {n} Scorers 2023/24",
              fontsize=16, fontweight="bold")
    plt.xlabel("Player", fontsize=12)
    plt.ylabel("Goals", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    for bar, val in zip(bars, top["Goals"]):
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + 0.3,
                 str(val), ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    _save("football_top_scorers.png")
    print("  ✅ Chart saved: charts/football_top_scorers.png")


def plot_goals_vs_assists(df: pd.DataFrame) -> None:
    """Scatter plot of goals vs assists."""
    plt.figure(figsize=(10, 7))
    clubs = df["Club"].unique()
    colors = sns.color_palette("tab10", len(clubs))
    club_color = dict(zip(clubs, colors))

    for _, row in df.iterrows():
        plt.scatter(row["Goals"], row["Assists"],
                    color=club_color[row["Club"]],
                    s=120, edgecolors="gray", alpha=0.85)
        plt.annotate(row["Player"].split()[-1],
                     (row["Goals"], row["Assists"]),
                     textcoords="offset points",
                     xytext=(5, 5), fontsize=8)

    legend_patches = [
        mpatches.Patch(color=club_color[club], label=club)
        for club in clubs
    ]
    plt.legend(handles=legend_patches, loc="upper right",
               fontsize=8, title="Club")
    plt.title("Premier League Goals vs Assists 2023/24",
              fontsize=14, fontweight="bold")
    plt.xlabel("Goals", fontsize=12)
    plt.ylabel("Assists", fontsize=12)
    plt.tight_layout()
    _save("goals_vs_assists.png")
    print("  ✅ Chart saved: charts/goals_vs_assists.png")


def plot_club_goals(df: pd.DataFrame) -> None:
    """Bar chart of total goals per club."""
    club_data = (
        df.groupby("Club")["Goals"]
        .sum()
        .sort_values(ascending=False)
    )
    plt.figure(figsize=(10, 5))
    colors = sns.color_palette("coolwarm", len(club_data))
    bars = plt.bar(club_data.index, club_data.values,
                   color=colors, edgecolor="white")
    plt.title("Total Goals by Club 2023/24",
              fontsize=14, fontweight="bold")
    plt.xlabel("Club", fontsize=12)
    plt.ylabel("Total Goals", fontsize=12)
    plt.xticks(rotation=30, ha="right")
    for bar, val in zip(bars, club_data.values):
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + 0.2,
                 str(val), ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    _save("club_total_goals.png")
    print("  ✅ Chart saved: charts/club_total_goals.png")