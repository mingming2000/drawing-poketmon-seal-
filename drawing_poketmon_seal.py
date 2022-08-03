import random

global want
global money


def printinBox(x,y):
    
    print('\n\n\n\n=====================================\n\n\n\n')
    print('\n\n',x,'\n\n 남은 돈 :',y,'원\n\n')
    print('\n\n\n\n=====================================')

def printinBox_list(x):
    print('=====================================')
    for i in range (0, len(x)):
        print('             ',x[i])
        
    print('=====================================')    

def draw():
    global money
    global want 
    if( money < 1500 ):
        x = '아쉽게도 돈이 다 떨어졌네요. 원하는 포켓몬 뽑기 실패~!~!'
        printinBox(x, money)
    
    else:
        money -= 1500
        
        choice = random.choice(poketmon)
        
        result = '쨔잔~! 야생의 '+choice+' (이)가 나타났다~!'
        printinBox(result, money)


        if( want == choice ):
            print('당신은 이제',want,'의 주인! 축하합니다!')
            
        else:
            respond = input('종료하시려면 s, 계속 뽑으시려면 다른 문자를 아무거나 눌러주세요.')
            if(respond == 's'):
                x = '소듕한 나의 돈 ...'
                printinBox(x, money)
            else:
                draw()
            



poketmon = ['이상해씨', '파이리', '피카츄', '라이츄', '푸린', '뚜벅초', '고라파덕', '냐옹', '야도란', '팬텀', '메타몽', '마자용', '우츠동', '멍파치', '잠만보', '망냐뇽']
money = 8000

print('가진 돈 : 8000원')
print('\n\n\n띠부띠부씰 뽑기~!~!(1500원)')
printinBox_list(poketmon)


want = input('\n\n위의 항목 중, 랜덤으로 하나를 뽑을 수 있습니다. \n간절한 마음을 담아, 뽑고 싶은 포켓몬 이름을 입력해주세요. : ')
draw()
