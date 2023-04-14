import pygame
import random

pygame.init()

WIDTH = 1400
HEIGHT = 600
FONT_SIZE = 32

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

font = pygame.font.Font(None, FONT_SIZE)

def get_quotes():
    with open('quotes.txt', 'r') as f:
        quotes = f.read().splitlines()
    return quotes

def add_quote(quote):
    with open('quotes.txt', 'a') as f:
        f.write(quote + '\n')

def get_random_quote():
    quotes = get_quotes()
    return random.choice(quotes)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('MotiQuotes')

    quote_text = get_random_quote()
    text_surface = font.render(quote_text, True, WHITE)

    input_active = False
    quote_input = ""
    input_rect = pygame.Rect((WIDTH - 800) // 2, (HEIGHT - FONT_SIZE) // 2 + FONT_SIZE + 20, 800, 45)

    # Define the buttons
    random_button = pygame.Rect((WIDTH - 300) // 2, input_rect.bottom + 20, 150, 50)
    add_button = pygame.Rect(random_button.right + 20, input_rect.bottom + 20, 150, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse was clicked on a button
                if random_button.collidepoint(event.pos):
                    quote_text = get_random_quote()
                    text_surface = font.render(quote_text, True, WHITE)
                elif add_button.collidepoint(event.pos):
                    input_active = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_active:
                        add_quote(quote_input)
                        print("Quote added!")
                        input_active = False
                        quote_input = ""
                        text_surface = font.render(get_random_quote(), True, WHITE)
                elif event.key == pygame.K_BACKSPACE:
                    if input_active:
                        quote_input = quote_input[:-1]
                else:
                    if input_active:
                        quote_input += event.unicode

        screen.fill(BLACK)
        screen.blit(text_surface, ((WIDTH - text_surface.get_width()) // 2, (HEIGHT - text_surface.get_height()) // 2))

        pygame.draw.rect(screen, WHITE, input_rect, 2)
        input_surface = font.render(quote_input, True, WHITE)
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

        # Draw the buttons
        pygame.draw.rect(screen, GRAY, random_button)
        pygame.draw.rect(screen, GRAY, add_button)
        random_text = font.render("Random", True, WHITE)
        add_text = font.render("Add Quote", True, WHITE)
        screen.blit(random_text, (random_button.x + 20, random_button.y + 10))
        screen.blit(add_text, (add_button.x + 20, add_button.y + 10))

        pygame.display.update()

if __name__ == '__main__':
    main()
    
