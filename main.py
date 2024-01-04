import pygame
import sys
import random


class Snake:

    def __init__(self):

        pygame.display.set_caption('Snake')
        pygame.init()
        self.map_width = 1920
        self.map_height = 1080
        self.screen = pygame.display.set_mode((self.map_width, self.map_height))
        self.snake_length = 30
        self.snake = pygame.Rect(100, 100, 30, 30)
        self.snake_colour = (255, 0, 255)
        self.points = pygame.Rect(random.randint(0, 1870), random.randint(0, 1000), 30, 30)
        self.count = 15
        self.direction = 0
        self.speed = 3
        self.number_of_deths = 0
        self.enemy1 = pygame.Rect(900, 50, 30, 30)  # Stage 2
        self.enemy2 = pygame.Rect(50, 500, 30, 30)  # Stage 2

        self.enemy3 = pygame.Rect(700, 50, 50, 50)  # Stage 3
        self.enemy4 = pygame.Rect(50, 500, 50, 50)  # Stage 3
        self.enemy5 = pygame.Rect(300, 50, 50, 50)  # Stage 3
        self.enemy6 = pygame.Rect(50, 500, 50, 50)  # Stage 3

    def run_game(self):
        while True:
            self.keyboard_check_events()
            self.update_screen()
            self.draw_point_counter()
            self.draw_deth_counter()
            self.draw_stage_text_and_rules()
            self.end_game_text()
            self.end_game_text()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    sys.exit()

    def keyboard_check_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction = 1
        if keys[pygame.K_a]:
            self.direction = 2
        if keys[pygame.K_w]:
            self.direction = 3
        if keys[pygame.K_s]:
            self.direction = 4

        if self.direction == 1 and self.direction == 3:
            self.direction = 0
        if self.direction == 2 and self.direction == 4:
            self.direction = 0
        if self.direction == 2 and self.direction == 1:
            self.direction = 0

        if self.direction == 1:
            self.snake.x += self.speed
        if self.direction == 2:
            self.snake.x -= self.speed
        if self.direction == 3:
            self.snake.y -= self.speed
        if self.direction == 4:
            self.snake.y += self.speed

    def draw_point_counter(self):
        self.font = pygame.font.Font(None, 36)
        self.point_text = self.font.render(f"Points: {self.count}", True, (0, 0, 255))
        self.screen.blit(self.point_text, (10, 10))

    def draw_deth_counter(self):
        self.font = pygame.font.Font(None, 36)
        self.death_text = self.font.render(f"Deths: {self.number_of_deths}", True, (255, 0, 0))
        self.screen.blit(self.death_text, (10, 50))

    def draw_stage_text_and_rules(self):
        self.font = pygame.font.Font(None, 28)
        self.stage_text1 = self.font.render("First Stage (1-9 points)", True, (255, 0, 0))
        self.stage_text2 = self.font.render("Second Stage (10-19 points)", True, (255, 0, 0))
        self.stage_text3 = self.font.render("Third Stage (20-29 points)", True, (255, 0, 0))
        self.q_to_exit_text = self.font.render("Press Q to exit", True, (255, 0, 0))
        self.screen.blit(self.stage_text1, (1650, 10))
        self.screen.blit(self.stage_text2, (1650, 40))
        self.screen.blit(self.stage_text3, (1650, 70))
        self.screen.blit(self.q_to_exit_text, (1650, 100))

    def end_game_text(self):
        self.font = pygame.font.Font(None, 54)
        self.won_text = self.font.render("You won :D", True, (0, 255, 0))

    def update_screen(self):

        # Border
        self.line1 = pygame.draw.line(self.screen, (0, 250, 0), (0, 0), (0, 1080))
        self.line2 = pygame.draw.line(self.screen, (0, 250, 0), (0, 0), (1920, 0))
        self.line3 = pygame.draw.line(self.screen, (0, 250, 0), (0, 1075), (1940, 1075))
        self.line4 = pygame.draw.line(self.screen, (0, 250, 0), (1917, 1075), (1917, 0))

        # Stage 2
        if self.count >= 10:
            self.speed = 3
            self.snake_colour = (0, 0, 255)
            pygame.draw.rect(self.screen, (255, 0, 0), self.enemy1)
            pygame.draw.rect(self.screen, (255, 0, 0), self.enemy2)
            self.enemy1.y += 2
            self.enemy2.x += 4
            if self.snake.colliderect(self.enemy1) or self.snake.colliderect(self.enemy1):
                self.number_of_deths += 1
                self.snake.size = (30, 30)
                self.snake.x = 100
                self.snake.y = 100
                self.count = 0
                self.speed = 4

        # Stage 3
        if self.count >= 20:
            self.speed = 4
            self.snake_colour = (150, 0, 255)
            pygame.draw.rect(self.screen, (255, 0, 0), self.enemy3)
            pygame.draw.rect(self.screen, (255, 0, 0), self.enemy4)
            pygame.draw.rect(self.screen, (255, 0, 0), self.enemy5)
            pygame.draw.rect(self.screen, (255, 0, 0), self.enemy6)
            self.enemy3.y += 2
            self.enemy4.y += 2
            self.enemy5.y += 2
            self.enemy6.y += 2
            self.enemy3.x += 4
            self.enemy4.x += 4
            self.enemy5.x += 4
            self.enemy6.x += 4

            if self.snake.colliderect(self.enemy3) or self.snake.colliderect(self.enemy4)\
                    or self.snake.colliderect(self.enemy5) or self.snake.colliderect(self.enemy6):
                self.number_of_deths += 1
                self.snake.size = (30, 30)
                self.snake.x = 100
                self.snake.y = 100
                self.count = 0
                self.speed = 5

        if self.count >= 30:
            self.screen.blit(self.won_text, (800, 500))
            pygame.display.flip()
            pygame.time.delay(3000)
            sys.exit()

        # Border collidate
        if self.snake.colliderect(self.line1) or self.snake.colliderect(self.line2) or self.snake.colliderect(
                self.line3) or self.snake.colliderect(self.line4):
            self.number_of_deths += 1
            self.snake.size = (30, 30)
            self.snake.x = 100
            self.snake.y = 100
            self.count = 0
            self.speed = 2


        # Points
        if self.snake.colliderect(self.points):
            self.count += 1
            self.points.x = random.randint(0, 1890)
            self.points.y = random.randint(0, 1050)
            self.snake.size = (self.snake_length + self.count * 5, self.snake_length + self.count * 5)

        pygame.draw.rect(self.screen, (0, 255, 0), self.points)
        pygame.draw.rect(self.screen, self.snake_colour, self.snake)
        pygame.display.flip()
        self.screen.fill((0, 0, 0))


if __name__ == '__main__':
    game = Snake()
    game.run_game()
