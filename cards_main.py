import cards_tools
import pillow
while True:
    cards_tools.show_menu()
    anction=input('请输入您要选择的操作：')
    if anction in ['1','2','3']:
        if anction=='1':
            cards_tools.new_card()
        elif anction=='2':
            cards_tools.show_all()
        elif anction=='3':
            cards_tools.search_card()
    elif anction=='0':
        print('欢迎再次使用')
        break
