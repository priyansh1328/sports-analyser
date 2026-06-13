"""
stats.py
Analyses cricket and football data.
"""

import logging
import pandas as pd

logger = logging.getLogger(__name__)


def top_batters(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Return top N batters by total runs."""
    logger.info("Calculating top %d batters by runs", n)
    return (
        df.sort_values("Runs", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )


def team_batting_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return total runs and average strike rate per team."""
    logger.info("Calculating team batting summary")
    return (
        df.groupby("Team")
        .agg(
            Total_Runs=("Runs", "sum"),
            Avg_Strike_Rate=("Strike_Rate", "mean"),
            Total_Players=("Player", "count"),
            Avg_Average=("Average", "mean")
        )
        .round(2)
        .sort_values("Total_Runs", ascending=False)
        .reset_index()
    )


def top_bowlers(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Return top N bowlers by wickets."""
    logger.info("Calculating top %d bowlers by wickets", n)
    return (
        df.sort_values("Wickets", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )


def most_economical_bowlers(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Return top N most economical bowlers."""
    logger.info("Finding top %d most economical bowlers", n)
    return (
        df.sort_values("Economy", ascending=True)
        .head(n)
        .reset_index(drop=True)
    )


def top_football_scorers(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Return top N football players by goals."""
    logger.info("Calculating top %d scorers", n)
    return (
        df.sort_values("Goals", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )


def top_football_assisters(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Return top N football players by assists."""
    logger.info("Calculating top %d assisters", n)
    return (
        df.sort_values("Assists", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )


def goal_contributions(df: pd.DataFrame) -> pd.DataFrame:
    """Add goal contributions column (goals + assists)."""
    logger.info("Calculating goal contributions")
    df = df.copy()
    df["Goal_Contributions"] = df["Goals"] + df["Assists"]
    return (
        df.sort_values("Goal_Contributions", ascending=False)
        .reset_index(drop=True)
    )


def club_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return total goals and assists per club."""
    logger.info("Calculating club summary")
    return (
        df.groupby("Club")
        .agg(
            Total_Goals=("Goals", "sum"),
            Total_Assists=("Assists", "sum"),
            Total_Players=("Player", "count")
        )
        .sort_values("Total_Goals", ascending=False)
        .reset_index()
    )