# khai báo các modul
import pygame, sys
pygame.init()
clock = pygame.time.Clock()
# Khởi tạo màn hình
pygame.display.set_caption("Dino Game(Phong_test)")
icon = pygame.image.load('assets/dinosaur.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((600, 300))
# Tạo các biến màu sắc
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Khởi tạo hình ảnh nhân vật và cảnh vật
bg = pygame.image.load('assets/background.jpg')
tree = pygame.image.load('assets/tree.png')
dino = pygame.image.load('assets/dinosaur.png')
# load âm thanh
sound1 = pygame.mixer.Sound('sound/tick.wav')
sound2 = pygame.mixer.Sound('sound/te.wav')
# Khởi tạo và định nghĩa hàm message
arialFont = pygame.font.SysFont("Arial", 30)
def message(msg, color, x, y):
    mesg = arialFont.render(msg, True, color)
    textRect = mesg.get_rect()
    textRect.center = (x, y)
    screen.blit(mesg, textRect)
# khởi tạo vị trí 
score, hscore = 0, 0
bg_x, bg_y = 0, 0
tree_x, tree_y = 550, 230
dino_x, dino_y = 10, 230
# tạo các biến trung gian
x_del = 5
y_del = 0
game_close = False
count = 0
up = False
down = False
while True:
    clock.tick(30)
    # Tạo hình ảnh chuyển động trong game
    bg_x -= x_del
    if bg_x == -600: bg_x = 0
    tree_x -= x_del
    if tree_x == -50: tree_x = 550  
           
    bg_list1 = [bg, bg_x, bg_y]
    bg_list2 = [bg, bg_x + 600, bg_y]
    tree_list = [tree, tree_x, tree_y]
    dino_list = [dino, dino_x, dino_y]
    list_image = [bg_list1, bg_list2, tree_list, dino_list]
    for image in list_image:
        screen.blit(image[0], [image[1], image[2]])
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #hscore = max(hscore, score)
            pygame.quit()
            sys.exit()

        # Bắt các sự kiện trong game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                up = True
                y_del = -10   
                pygame.mixer.Sound.play(sound1)                
            if event.key == pygame.K_DOWN:
                down = True
                y_del = 5
                pygame.mixer.Sound.play(sound1)
            # Ứng mạng 3 lần
            elif event.key == pygame.K_SPACE:
                count += 1
                if score > 0: 
                    score -= 1  # mỗi lần ứng mạng sẽ bị trừ 1 điểm
                game_close = (3 - count) < 0    

            else:
                pass
       
    if up == True:
        dino_y += y_del
        if dino_y < 100:
            y_del = 10
        elif dino_y >= 230:
            dino_y = 230 
            if tree_x + 20 < dino_x:
                score += 1
            up = False      
    if down == True:
        dino_y += y_del
        if dino_y > 245:
            y_del = -5
        elif dino_y <= 230:
            dino_y = 230
            if tree_x + 20 < dino_x:
                score += 1
            down = False

    if score >= hscore:
        hscore = score
    message(f"hscore: {hscore}   " + f"score: {score}", GREEN, 300, 50)

    # khi dino chạm cây thì thua
    if (tree_x >= 10) & (tree_x <= 50) & (dino_y >= 190) & (score>=0):
        game_close = True    
        pygame.mixer.Sound.play(sound2)   
    if game_close:
        if count <=3:
            show = "press key_space to continue!"
        else:
            show = "Game Over!"
        message(f"you lose! {show}", RED, 300, 100)       
        bg_x = 0
        tree_x = 550
    print(dino_y)        
    pygame.display.update()              
