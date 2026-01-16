# Good, Bad, or Ugly Card Draw

This project is a Python script that generates a PDF document for the "Good, Bad, or Ugly"
card game, featuring a grid layout with color-coded suits.

## What is "Good, Bad, or Ugly"?

"Good, Bad, or Ugly" is a set of rules for bowling poker, a game of poker typically played by
league bowlers. It involves drawing cards from a deck based on how well one bowls. This game
serves as a handicap for games that may have bowlers that mark more than others by providing
random chances in which one or all players will have to discard their hands and start over.
Let's face it, bowling poker is more fun if the same person isn't always winning the pot.

The rules of this bowling poker game are:
- Draw two cards for bowling a strike.
- Draw one card for picking up a non-split spare.
- Draw two cards for picking up a split spare.
- If a player draws a "Bad" card then they discard their hand.
- If a player draws an "Ugly" card then all players discard their hands.
- Cards must be drawn in player bowl order.
- Draw cards one at a time and evaluate "Good, Bad, or Ugly" with each card in succession.
- Aces are always "Good".

Another good rule is to always mix up the bowling order so the same bowler isn't in the anchor
position each week of the league. Bowling last is an advantage in "Good, Bad, or Ugly."

## Features

- **Random Card Drawing**: Draws unique cards for three separate games
- **Unique Values Per Game**: Ensures no duplicate card values within each game
- **PDF Output**: Generates a PDF document for printing/displaying during the bowling match
- **Grid Layout**: Organizes each game into two columns (Bad and Ugly)
- **Color-Coded Suits**: 
  - Hearts (♥) and Diamonds (♦) displayed in **red**
  - Clubs (♣) and Spades (♠) displayed in **black**
- **Sorted Columns**: Cards are displayed lowest to highest value in each column for quick card checks

## Requirements

- Python 3.6+
- reportlab library

## Installation

1. Clone or download this repository
2. Install the required dependency:

```bash
pip install reportlab
```

## Usage

Run the script:

```bash
python draw-cards.py
```

This will generate a PDF file named `good_bad_ugly_cards.pdf` in the same directory.

## Game Structure

The script draws cards for three games with the following distribution:

- **Game 1**: 4 Bad cards, 3 Ugly cards
- **Game 2**: 5 Bad cards, 4 Ugly cards  
- **Game 3**: 4 Bad cards, 6 Ugly cards

## Card Rules

- Each game uses a 48-card deck (2-K, no Aces)
- Within each game, no card value can appear twice (regardless of suit)
- Cards are drawn randomly and uniquely for each category
- The deck is shuffled before each run

## Output

The generated PDF includes:
- Professional title header
- 6-column table layout (3 games × 2 categories each)
- Alternating row colors for readability
- Grid lines for clear separation
- Color-coded suits for easy identification

## File Structure

```
├── .gitignore            # Ingore generated PDF files
├── draw-cards.py         # Main script
├── LICENSE               # Governs use of this open source repo
├── README.md             # This file
└── good_bad_ugly_cards.pdf  # Generated output (after running)
```

## License

This project is open source and available under the MIT License.
