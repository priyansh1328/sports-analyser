"""
fetch_data.py
Fetches cricket and football stats.
"""

import logging
import pandas as pd

logger = logging.getLogger(__name__)


def fetch_ipl_batting_stats() -> pd.DataFrame:
    """Returns IPL all-time batting stats as a DataFrame."""
    logger.info("Fetching IPL batting stats...")

    data = {
        "Player": [
            "Virat Kohli", "Shikhar Dhawan", "Rohit Sharma",
            "David Warner", "Suresh Raina", "MS Dhoni",
            "AB de Villiers", "Chris Gayle", "KL Rahul",
            "Faf du Plessis", "Rishabh Pant", "Hardik Pandya",
            "Ambati Rayudu", "Robin Uthappa", "Dinesh Karthik"
        ],
        "Team": [
            "RCB", "DC", "MI",
            "SRH", "CSK", "CSK",
            "RCB", "RCB", "PBKS",
            "RCB", "DC", "MI",
            "CSK", "KKR", "KKR"
        ],
        "Matches": [
            237, 206, 243, 184, 205, 234,
            184, 142, 115, 130, 111, 115,
            205, 205, 229
        ],
        "Runs": [
            7263, 6769, 6628, 6565, 6239, 5243,
            5162, 4965, 4163, 4162, 3284, 3068,
            4349, 4952, 4843
        ],
        "Average": [
            37.25, 35.18, 30.22, 42.00, 33.15, 38.09,
            39.70, 40.69, 47.87, 37.50, 35.69, 29.89,
            28.81, 27.08, 25.75
        ],
        "Strike_Rate": [
            129.95, 127.09, 130.45, 142.35, 136.73, 135.92,
            151.68, 148.96, 136.22, 135.84, 148.67, 144.73,
            121.75, 130.98, 133.89
        ],
        "Hundreds": [5, 2, 1, 4, 1, 0, 3, 6, 2, 2, 1, 0, 0, 0, 0],
        "Fifties": [
            50, 42, 40, 58, 38, 24,
            35, 30, 28, 32, 18, 12,
            21, 34, 28
        ],
        "Highest_Score": [
            113, 106, 109, 126, 100, 84,
            133, 175, 132, 96, 128, 91,
            100, 88, 97
        ]
    }

    df = pd.DataFrame(data)
    logger.info("Loaded %d IPL batting records", len(df))
    return df


def fetch_ipl_bowling_stats() -> pd.DataFrame:
    """Returns IPL all-time bowling stats as a DataFrame."""
    logger.info("Fetching IPL bowling stats...")

    data = {
        "Player": [
            "Lasith Malinga", "Dwayne Bravo", "Amit Mishra",
            "Piyush Chawla", "Harbhajan Singh", "Bhuvneshwar Kumar",
            "Sunil Narine", "Ravichandran Ashwin", "Mohammed Shami",
            "Jasprit Bumrah", "Yuzvendra Chahal", "Imran Tahir",
            "AB McDonald", "Pragyan Ojha", "Irfan Pathan"
        ],
        "Team": [
            "MI", "CSK", "DC",
            "KKR", "MI", "SRH",
            "KKR", "CSK", "PBKS",
            "MI", "RCB", "CSK",
            "RCB", "SRH", "MI"
        ],
        "Matches": [
            122, 161, 154, 175, 163, 157,
            162, 154, 87, 120, 131, 99,
            59, 89, 100
        ],
        "Wickets": [
            170, 183, 166, 157, 150, 142,
            163, 125, 96, 130, 187, 99,
            55, 113, 69
        ],
        "Economy": [
            7.14, 8.38, 7.36, 7.89, 7.05, 7.31,
            6.67, 6.97, 8.07, 7.41, 7.73, 6.96,
            7.61, 7.33, 8.21
        ],
        "Average": [
            18.92, 23.64, 21.77, 26.88, 24.50, 25.30,
            22.30, 27.10, 23.87, 21.72, 19.51, 21.77,
            25.60, 22.91, 28.56
        ],
        "Best_Figures": [
            "5/13", "4/22", "5/17", "4/17", "5/18", "5/19",
            "5/19", "4/16", "4/12", "5/10", "5/40", "4/9",
            "3/19", "4/14", "3/12"
        ]
    }

    df = pd.DataFrame(data)
    logger.info("Loaded %d IPL bowling records", len(df))
    return df


def fetch_football_stats() -> pd.DataFrame:
    """Returns Premier League 2023/24 top scorer stats."""
    logger.info("Fetching Premier League stats...")

    data = {
        "Player": [
            "Erling Haaland", "Cole Palmer", "Alexander Isak",
            "Dominic Solanke", "Jarrod Bowen", "Ollie Watkins",
            "Phil Foden", "Mohamed Salah", "Son Heung-min",
            "Bukayo Saka", "Marcus Rashford", "Darwin Nunez",
            "Callum Wilson", "Leandro Trossard", "Richarlison"
        ],
        "Club": [
            "Man City", "Chelsea", "Newcastle",
            "Bournemouth", "West Ham", "Aston Villa",
            "Man City", "Liverpool", "Spurs",
            "Arsenal", "Man Utd", "Liverpool",
            "Newcastle", "Arsenal", "Spurs"
        ],
        "Goals": [
            27, 22, 21, 19, 16, 19,
            19, 18, 17, 16, 7, 11,
            11, 10, 4
        ],
        "Assists": [
            5, 11, 2, 4, 8, 13,
            8, 10, 10, 14, 5, 6,
            3, 4, 2
        ],
        "Matches_Played": [
            31, 33, 30, 38, 38, 37,
            35, 32, 38, 38, 27, 32,
            22, 36, 18
        ],
        "Minutes_Played": [
            2559, 2727, 2455, 3185, 3125, 3020,
            2734, 2589, 3120, 3150, 1892, 2210,
            1655, 2540, 1250
        ],
        "Goals_Per_Game": [
            0.87, 0.67, 0.70, 0.50, 0.42, 0.51,
            0.54, 0.56, 0.45, 0.42, 0.26, 0.34,
            0.50, 0.28, 0.22
        ],
        "Nationality": [
            "Norwegian", "English", "Swedish",
            "English", "English", "English",
            "English", "Egyptian", "South Korean",
            "English", "English", "Uruguayan",
            "English", "Belgian", "Brazilian"
        ]
    }

    df = pd.DataFrame(data)
    logger.info("Loaded %d Premier League player records", len(df))
    return df