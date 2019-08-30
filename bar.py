import pygame ,time
# #pygame初始化
pygame.init()
def showBar(name,total,cumN):
    #設定視窗
    width, height = 600, 150                       #遊戲畫面寬和高
    screen = pygame.display.set_mode((width, height))   #依設定顯示視窗
    pygame.display.set_caption(name+"進度條")           #設定程式標題
    #取得視窗尺寸,建立畫布
    desk=pygame.Surface(screen.get_size())
    #convert()建立副本,加快畫布在視窗的顯示速度
    desk=desk.convert()
    desk.fill((255,255,255)) #畫布顏色白色
    #顯示固定進度條
    pygame.draw.rect(desk,(192,192,192),[50,50,500,60],0) #線寬0為實心
    #顯示動態進度條
    k=int((cumN/total)*500)
    pygame.draw.rect(desk,(0,255,127),[50,50,k,60],0) #線寬0為實心
    #改字體、大小
    #字體變數 = pygame.font.SysFont(字體名稱, 字體尺寸)
    font = pygame.font.SysFont("simhei", 20)
    ProgNum=int((cumN/total)*100)
    num=str(ProgNum)+"%"
    #print(num)
    #文字變數 = 字體變數.render(文字, 平滑值, 文字顏色, 背景顏色)
    if ProgNum>=48:
        text = font.render(num, True, (0,0,0),(0,255,127))
    else:
        text = font.render(num, True, (0,0,0),(192,192,192))
    #顯示文字
    desk.blit(text, (275,70))
    #顯示畫布
    screen.blit(desk,(0,0))
    
    clock=pygame.time.Clock()

    pygame.display.update()
    time.sleep(0.05)
    #每秒執行30次
    clock.tick(5)
    pygame.display.quit
#showBar("test",sc,len(total))