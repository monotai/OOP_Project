import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Load images
X_IMAGE = pygame.image.load('x.png')
O_IMAGE = pygame.image.load('o.png')
X_IMAGE = pygame.transform.scale(X_IMAGE, (SQUARE_SIZE, SQUARE_SIZE))
O_IMAGE = pygame.transform.scale(O_IMAGE, (SQUARE_SIZE, SQUARE_SIZE))

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Board
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Draw lines
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw figures
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                screen.blit(X_IMAGE, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif board[row][col] == 'O':
                screen.blit(O_IMAGE, (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Mark square
def mark_square(row, col, player):
    board[row][col] = player

# Check if square is available
def available_square(row, col):
    return board[row][col] is None

# Check if board is full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

# Check for win
def check_win(player):
    # Vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    # Ascending diagonal win check
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True

    # Descending diagonal win check
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    return False

# Main loop
draw_lines()
player = 'X'
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = 'O' if player == 'X' else 'X'

                draw_figures()

    pygame.display.update()