"""
main.py
Entry point — run this file to start the analyser.
"""

import logging
import os
import sys
import pandas as pd
from tabulate import tabulate

from scraper.fetch_data import (
    fetch_ipl_batting_stats,
    fetch_ipl_bowling_stats,
    fetch_football_stats,
)
from analyser.stats import (
    top_batters,
    team_batting_summary,
    top_bowlers,
    most_economical_bowlers,
    top_football_scorers,
    top_football_assisters,
    goal_contributions,
    club_summary,
)
from visualiser.charts import (
    plot_top_batters,
    plot_strike_rate_vs_average,
    plot_team_runs,
    plot_top_bowlers,
    plot_economy_vs_wickets,
    plot_football_goals,
    plot_goals_vs_assists,
    plot_club_goals,
)

# ── Logging setup ──────────────────────────────────────────────────
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s — %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs/sports_analyser.log"),
    ],
)
logger = logging.getLogger(__name__)

GREEN  = "\033[92m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
BOLD   = "\033[1m"
RESET  = "\033[0m"


def print_header(title: str) -> None:
    print(f"\n{CYAN}{BOLD}{'═' * 55}")
    print(f"  {title}")
    print(f"{'═' * 55}{RESET}\n")


def print_table(df: pd.DataFrame, title: str) -> None:
    print(f"{YELLOW}{BOLD}{title}{RESET}")
    print(tabulate(df, headers="keys",
                   tablefmt="rounded_outline",
                   showindex=False))
    print()


def save_csv(df: pd.DataFrame, filename: str) -> None:
    os.makedirs("data", exist_ok=True)
    path = os.path.join("data", filename)
    df.to_csv(path, index=False)
    print(f"  {GREEN}✅ Data saved: {path}{RESET}")


def run_cricket_analysis() -> None:
    print_header("🏏  IPL CRICKET STATS ANALYSER")

    batting_df = fetch_ipl_batting_stats()
    bowling_df = fetch_ipl_bowling_stats()

    print_header("BATTING ANALYSIS")
    top5 = top_batters(batting_df, n=5)
    print_table(
        top5[["Player", "Team", "Matches",
              "Runs", "Average", "Strike_Rate"]],
        "Top 5 IPL Run Scorers (All Time)"
    )

    team_sum = team_batting_summary(batting_df)
    print_table(team_sum, "Team Batting Summary")

    print_header("BOWLING ANALYSIS")
    top5_bowl = top_bowlers(bowling_df, n=5)
    print_table(
        top5_bowl[["Player", "Team", "Matches",
                   "Wickets", "Economy", "Average"]],
        "Top 5 IPL Wicket Takers (All Time)"
    )

    eco = most_economical_bowlers(bowling_df, n=5)
    print_table(
        eco[["Player", "Team", "Wickets",
             "Economy", "Best_Figures"]],
        "Top 5 Most Economical Bowlers"
    )

    print_header("GENERATING CRICKET CHARTS")
    plot_top_batters(batting_df)
    plot_strike_rate_vs_average(batting_df)
    plot_team_runs(batting_df)
    plot_top_bowlers(bowling_df)
    plot_economy_vs_wickets(bowling_df)

    print_header("SAVING CRICKET DATA")
    save_csv(batting_df,  "ipl_batting_stats.csv")
    save_csv(bowling_df,  "ipl_bowling_stats.csv")
    save_csv(team_sum,    "ipl_team_summary.csv")


def run_football_analysis() -> None:
    print_header("⚽  PREMIER LEAGUE STATS ANALYSER")

    football_df = fetch_football_stats()

    print_header("SCORING ANALYSIS")
    top5_score = top_football_scorers(football_df, n=5)
    print_table(
        top5_score[["Player", "Club", "Goals",
                    "Assists", "Matches_Played"]],
        "Top 5 Premier League Scorers 2023/24"
    )

    top5_assist = top_football_assisters(football_df, n=5)
    print_table(
        top5_assist[["Player", "Club", "Assists",
                     "Goals", "Matches_Played"]],
        "Top 5 Premier League Assisters 2023/24"
    )

    contrib = goal_contributions(football_df)
    print_table(
        contrib[["Player", "Club", "Goals",
                 "Assists", "Goal_Contributions"]].head(5),
        "Top 5 by Goal Contributions"
    )

    clubs = club_summary(football_df)
    print_table(clubs, "Goals by Club")

    print_header("GENERATING FOOTBALL CHARTS")
    plot_football_goals(football_df)
    plot_goals_vs_assists(football_df)
    plot_club_goals(football_df)

    print_header("SAVING FOOTBALL DATA")
    save_csv(football_df, "premier_league_stats.csv")
    save_csv(clubs,       "club_goals_summary.csv")


def main() -> None:
    print(f"\n{GREEN}{BOLD}")
    print("╔══════════════════════════════════════════════════════╗")
    print("║     CRICKET & FOOTBALL STATS ANALYSER               ║")
    print("║     IPL All-Time + Premier League 2023/24           ║")
    print("╚══════════════════════════════════════════════════════╝")
    print(RESET)

    print(f"{YELLOW}Choose what to analyse:{RESET}")
    print("  1 — Cricket (IPL Stats)")
    print("  2 — Football (Premier League Stats)")
    print("  3 — Both Cricket and Football")
    print("  4 — Exit")

    choice = input(
        f"\n{CYAN}Enter your choice (1/2/3/4): {RESET}"
    ).strip()

    if choice == "1":
        run_cricket_analysis()
    elif choice == "2":
        run_football_analysis()
    elif choice == "3":
        run_cricket_analysis()
        run_football_analysis()
    elif choice == "4":
        print(f"\n{GREEN}Goodbye!{RESET}")
        sys.exit(0)
    else:
        print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.")
        main()

    print(f"\n{GREEN}{BOLD}✅ Analysis complete!{RESET}")
    print(f"{CYAN}📁 Charts saved in:  charts/ folder")
    print(f"📁 Data saved in:    data/ folder")
    print(f"📁 Logs saved in:    logs/ folder{RESET}\n")


if __name__ == "__main__":
    main()