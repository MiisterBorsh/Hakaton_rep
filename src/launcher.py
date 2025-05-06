
import pygame
import sys
import subprocess

# --- Налаштування ---
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
BLUE = (50, 150, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню гри")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 36)


class Button:
    def __init__(self, text, pos, size=(250, 60)):
        self.text = text
        self.rect = pygame.Rect(pos, size)
        self.color_default = GRAY
        self.color_hover = BLUE
        self.color = self.color_default

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def update(self, mouse_pos):
        self.color = self.color_hover if self.rect.collidepoint(mouse_pos) else self.color_default

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)


class MainMenu:
    def __init__(self):
        self.buttons = [
            Button("Почати гру", (275, 150)),
            Button("Налаштування", (275, 230)),
            Button("Правила", (275, 310)),
            Button("Вийти", (275, 390)),
        ]

    def run(self):
        running = True
        while running:
            screen.fill(DARK_GRAY)
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for button in self.buttons:
                    if button.is_clicked(event):
                        if button.text == "Почати гру":
                            pygame.quit()
                            subprocess.run([sys.executable, "main.py"])
                            sys.exit()
                        elif button.text == "Налаштування":
                            SettingsMenu().run()
                        elif button.text == "Правила":
                            RulesMenu().run()
                        elif button.text == "Вийти":
                            running = False

            for button in self.buttons:
                button.update(mouse_pos)
                button.draw(screen)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()


class SettingsMenu:
    def run(self):
        running = True
        while running:
            screen.fill((30, 30, 30))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            text = font.render("Налаштування (Esc — назад)", True, WHITE)
            screen.blit(text, (100, 100))
            pygame.display.flip()
            clock.tick(FPS)


class RulesMenu:
    def run(self):
        running = True
        while running:
            screen.fill((50, 50, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            lines = [
                "Правила гри:",
                "1. Робіть те-то.",
                "2. Уникайте того-то.",
                "Натисніть Esc, щоб повернутись."
            ]
            for i, line in enumerate(lines):
                txt = font.render(line, True, WHITE)
                screen.blit(txt, (80, 100 + i * 50))

            pygame.display.flip()
            clock.tick(FPS)


if __name__ == "__main__":
    MainMenu().run()
