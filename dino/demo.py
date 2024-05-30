import pygame   #import thư viện
pygame.init()
clock = pygame.time.Clock()

# tiêu đề & icon
pygame.display.set_caption('Dino game')
icon = pygame.image.load('assets/dinosaur.png')
pygame.display.set_icon(icon)

# cửa sổ game
screen = pygame.display.set_mode((600, 300))

# load hình ảnh
bg = pygame.image.load('assets/background.jpg')
tree = pygame.image.load('assets/tree.png')
dino = pygame.image.load('assets/dinosaur.png')

# load âm thanh
sound1 = pygame.mixer.Sound('sound/tick.wav')
sound2 = pygame.mixer.Sound('sound/te.wav')

# khởi tạo
score, hscore = 0, 0
bg_x, bg_y = 0, 0
tree_x, tree_y = 550, 230
dino_x, dino_y = 10, 230
x_def = 5  # tốc độ chạy của tree
y_def = 7  # tốc độ rơi
jump = False
gameplay = True

# check va chạm
def checkvc():
    if dino_hcn.colliderect(tree_hcn):
        pygame.mixer.Sound.play(sound2)
        return True
    return False

# điểm số
game_font = pygame.font.Font('04B_19.TTF', 20)
def score_view():
    if gameplay:
        score_txt = game_font.render(f'Score: {int(score)}', True, (255, 0, 0))
        screen.blit(score_txt, (250, 50))
        hscore_txt = game_font.render(f'High Score: {int(hscore)}', True, (255, 0, 0))
        screen.blit(hscore_txt, (350, 50))
    else:
        score_txt = game_font.render(f'Score: {int(score)}', True, (255, 0, 0))
        screen.blit(score_txt, (250, 50))
        hscore_txt = game_font.render(f'High Score: {int(hscore)}', True, (255, 0, 0))
        screen.blit(hscore_txt, (350, 50))
        over_txt = game_font.render('Game Over', True, (255, 0, 0))
        screen.blit(over_txt, (250, 200))

# xử lý vòng lặp game
running = True

while running:
    clock.tick(60)  # chỉnh khung hình trên giây FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gameplay:
                if dino_y == 230:
                    jump = True
                    pygame.mixer.Sound.play(sound1)
            if event.key == pygame.K_SPACE and not gameplay:
                gameplay = True

    if gameplay:
        # bg
        bg_hcn = screen.blit(bg, [bg_x, bg_y])
        bg2_hcn = screen.blit(bg, [bg_x + 600, bg_y])
        bg_x -= x_def
        if bg_x == -600: bg_x = 0

        # tree
        tree_hcn = screen.blit(tree, [tree_x, tree_y])
        tree_x -= x_def
        if tree_x == -20: tree_x = 550

        # dino
        dino_hcn = screen.blit(dino, [dino_x, dino_y])
        if dino_y >= 80 and jump:
            dino_y -= y_def
        else:
            jump = False
        if dino_y < 230 and not jump:
            dino_y += y_def

        score += 0.01
        if hscore < score: hscore = score
        gameplay = not checkvc()
        score_view()
    else:
        bg_x, bg_y = 0, 0
        tree_x, tree_y = 550, 230
        dino_x, dino_y = 10, 230
        bg_hcn = screen.blit(bg, [bg_x, bg_y])
        tree_hcn = screen.blit(tree, [tree_x, tree_y])
        dino_hcn = screen.blit(dino, [dino_x, dino_y])
        score = 0
        score_view()

    pygame.display.update()

pygame.quit()
