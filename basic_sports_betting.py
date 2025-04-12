# Basic-Sports-Betting-Platform-Script
import random

# Sample betting options
matches = {
    "Team A vs Team B": {"Team A": 1.8, "Team B": 2.2},
    "Team C vs Team D": {"Team C": 1.5, "Team D": 2.5},
}

def place_bet():
    print("Available matches:")
    for idx, match in enumerate(matches.keys(), start=1):
        print(f"{idx}. {match}")

    # Select match
    match_index = int(input("Select a match (1 or 2): ")) - 1
    match_name = list(matches.keys())[match_index]
    teams = matches[match_name]

    print(f"\n{match_name} - Odds:")
    for team, odds in teams.items():
        print(f"{team}: {odds}")

    # Select team
    team_choice = input("Enter the team you want to bet on: ")
    if team_choice not in teams:
        print("Invalid team selection!")
        return

    # Enter bet amount
    bet_amount = float(input("Enter your bet amount: $"))
    
    # Simulate match outcome
    winner = random.choice(list(teams.keys()))
    print(f"\nMatch Result: {winner} wins!")

    # Calculate winnings
    if team_choice == winner:
        winnings = bet_amount * teams[team_choice]
        print(f"Congratulations! You won ${winnings:.2f}")
    else:
        print("You lost the bet. Better luck next time!")

if __name__ == "__main__":
    place_bet()
