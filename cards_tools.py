card_list=[]
def show_menu():
    print('欢迎使用【菜单管理系统】V1.0')
    print('1.新建名片\n2.显示全部\n3.查询名片/n0.退出系统')
def new_card():
    name=input('请输入姓名：')
    phone=input('请输入你的联系电话：')
    qq=input('请输入你的QQ：')
    email=input('请输入邮件')
    #a=[name,phone,qq,email]
    card_dict={'name':name,'phone':phone,'qq':qq,'email':email}
    card_list.append(card_dict)
    print(card_list)
    print('信息输入成功')
def show_all():
    if len(card_list)==0:
        print('没有认合名片的记录')
    print(card_list)
def search_card():
    #按名字查询
    name_info=input('请输入你要查询的名字：')
    for card_dict in card_list:
        if name_info==card_dict['name']:
            print(card_dict['name'])
            print(card_dict['phone'])
            print(card_dict['qq'])
            print(card_dict['email'])
    else:
            print('没有相符和的信息')
