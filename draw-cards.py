import random
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def create_deck():
    suits = ['\u2665', '\u2666', '\u2663', '\u2660']  # Hearts, Diamonds, Clubs, Spades
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [f'{value} {suit}' for suit in suits for value in values]
    return deck

def draw_unique_value_cards(deck, num_cards, used_values=None):
    """Draw cards ensuring unique values within the game and no card repeats across games"""
    if used_values is None:
        used_values = set()
    
    selected_cards = []
    selected_values = set()
    
    while len(selected_cards) < num_cards:
        card = random.choice(deck)
        value = card.split(' ')[0]
        
        # Check if value is unique within this game and not in used_values
        if value not in selected_values and value not in used_values:
            selected_cards.append(card)
            selected_values.add(value)
            deck.remove(card)
    
    return selected_cards, selected_values

def get_card_value_order(card):
    """Return numeric order for card value (2=2, 3=3, ..., 10=10, J=11, Q=12, K=13)"""
    value = card.split(' ')[0]
    value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                 '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    return value_map.get(value, 0)

def sort_cards_by_value(cards):
    """Sort cards from lowest to highest value"""
    return sorted(cards, key=get_card_value_order)

def get_card_color(card):
    """Return red for hearts/diamonds, black for clubs/spades"""
    if '\u2665' in card or '\u2666' in card:  # Hearts or Diamonds
        return colors.red
    else:  # Clubs or Spades
        return colors.black

def create_pdf_table(game_data, filename):
    """Create a PDF table in landscape mode with card data for each game"""
    doc = SimpleDocTemplate(filename, pagesize=landscape(letter))
    story = []
    
    # Create styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        alignment=1  # Center alignment
    )
    
    # Add title
    title = Paragraph("Good Bad Ugly Card Draw", title_style)
    story.append(title)
    story.append(Spacer(1, 20))
    
    # Create table data
    table_data = []
    
    # Headers
    headers = ['Game 1', 'Game 1', 'Game 2', 'Game 2', 'Game 3', 'Game 3']
    subheaders = ['Bad', 'Ugly', 'Bad', 'Ugly', 'Bad', 'Ugly']
    table_data.append(headers)
    table_data.append(subheaders)
    
    # Find the maximum number of cards in any category to determine table height
    max_cards = max(len(game_data['game1_bad']), len(game_data['game1_ugly']),
                   len(game_data['game2_bad']), len(game_data['game2_ugly']),
                   len(game_data['game3_bad']), len(game_data['game3_ugly']))
    
    # Add card data rows
    for row in range(max_cards):
        row_data = []
        
        # Game 1
        if row < len(game_data['game1_bad']):
            row_data.append(game_data['game1_bad'][row])
        else:
            row_data.append('')
            
        if row < len(game_data['game1_ugly']):
            row_data.append(game_data['game1_ugly'][row])
        else:
            row_data.append('')
        
        # Game 2
        if row < len(game_data['game2_bad']):
            row_data.append(game_data['game2_bad'][row])
        else:
            row_data.append('')
            
        if row < len(game_data['game2_ugly']):
            row_data.append(game_data['game2_ugly'][row])
        else:
            row_data.append('')
        
        # Game 3
        if row < len(game_data['game3_bad']):
            row_data.append(game_data['game3_bad'][row])
        else:
            row_data.append('')
            
        if row < len(game_data['game3_ugly']):
            row_data.append(game_data['game3_ugly'][row])
        else:
            row_data.append('')
        
        table_data.append(row_data)
    
    # Create table
    table = Table(table_data, colWidths=[1.6*inch]*6)
    
    # Create table style
    table_style = TableStyle([
        # Header styling
        ('BACKGROUND', (0, 0), (-1, 1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 1), 20),
        ('BOTTOMPADDING', (0, 0), (-1, 1), 15),
        
        # Grid lines
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        
        # Data row styling
        ('FONTNAME', (0, 2), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 2), (-1, -1), 24),
        ('ALIGN', (0, 2), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 2), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 2), (-1, -1), 20),
        ('ROWBACKGROUNDS', (0, 2), (-1, -1), [colors.white, colors.lightgrey]),
    ])
    
    # Apply color coding to individual cells
    for row_idx in range(2, len(table_data)):  # Skip header rows
        for col_idx in range(6):
            cell_value = table_data[row_idx][col_idx]
            if cell_value:  # If cell is not empty
                card_color = get_card_color(cell_value)
                table_style.add('TEXTCOLOR', (col_idx, row_idx), (col_idx, row_idx), card_color)
    
    table.setStyle(table_style)
    story.append(table)
    
    # Build PDF
    doc.build(story)

def main():
    deck = create_deck()
    random.shuffle(deck)  # Shuffle the deck before drawing cards
    # Draw cards for three games, ensuring unique values within each game
    # Game 1
    game1_bad, game1_bad_values = draw_unique_value_cards(deck, 4)
    game1_bad = sort_cards_by_value(game1_bad)
    game1_ugly, game1_ugly_values = draw_unique_value_cards(deck, 3, game1_bad_values)
    game1_ugly = sort_cards_by_value(game1_ugly)
    
    # Game 2
    game2_bad, game2_bad_values = draw_unique_value_cards(deck, 5)
    game2_bad = sort_cards_by_value(game2_bad)
    game2_ugly, game2_ugly_values = draw_unique_value_cards(deck, 4, game2_bad_values)
    game2_ugly = sort_cards_by_value(game2_ugly)
    
    # Game 3
    game3_bad, game3_bad_values = draw_unique_value_cards(deck, 4)
    game3_bad = sort_cards_by_value(game3_bad)
    game3_ugly, game3_ugly_values = draw_unique_value_cards(deck, 5, game3_bad_values)
    game3_ugly = sort_cards_by_value(game3_ugly)

    # Organize game data
    game_data = {
        'game1_bad': game1_bad,
        'game1_ugly': game1_ugly,
        'game2_bad': game2_bad,
        'game2_ugly': game2_ugly,
        'game3_bad': game3_bad,
        'game3_ugly': game3_ugly
    }
    
    # Create PDF
    filename = "good_bad_ugly_cards.pdf"
    create_pdf_table(game_data, filename)
    print(f"PDF generated successfully: {filename}")

if __name__ == "__main__":
    main()