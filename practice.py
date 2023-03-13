import pygame

# 초기화
pygame.init()

# 창 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 폰트 정의
font = pygame.font.Font(None, 36)

# 시작 메뉴
def start_menu():
    # 메뉴 아이템 설정
    menu_items = [
        ("Start Game", (300, 250)),
        ("Quit", (300, 300))
    ]
    
    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 마우스 클릭한 위치
                pos = pygame.mouse.get_pos()
                for item in menu_items:
                    text_rect = font.render(item[0], True, BLACK).get_rect(center=item[1])
                    if text_rect.collidepoint(pos):
                        if item[0] == "Start Game":
                            game_loop()
                        elif item[0] == "Quit":
                            pygame.quit()
                            quit()
        
        # 화면 그리기
        screen.fill(WHITE)
        for item in menu_items:
            text = font.render(item[0], True, BLACK)
            text_rect = text.get_rect(center=item[1])
            screen.blit(text, text_rect)
        pygame.display.update()

# 게임 루프
def game_loop():
    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # 화면 그리기
        screen.fill(BLACK) #신입 수정부분
        pygame.display.update()

# 시작 메뉴 호출
start_menu()

# 종료
pygame.quit()
quit()
