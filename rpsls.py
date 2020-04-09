'''
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：田皓予
日期：2020.4.9
'''

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    number=-1 
    if name=="rock": 
        number=0
    elif name=="Spock":
        number=1
    elif name=="paper":
        number=2
    elif name=="lizard":
        number=3
    elif name=="scissors":
        number=4
    if number==-1:
        err="Error: No Correct Name "+ "\"" +name + "\"."
        return err
    else:
        return number
    
def number_to_name(number):
    name="none" 
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0: 
        name="rock"
    elif number==1:
        name="Spock"
    elif number==2:
        name="paper"
    elif number==3:
        name="lizard"
    elif number==4:
        name="scissors"
    if name=="none": 
        err="the number \""+ str(number) + "\" is not a valid input."
        return err
    else:
        return name
    
def compare_player_comp_m1(player_number,comp_number):
    diff = player_number - comp_number
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    if (diff>2):
        player_number -= 5
    elif (diff<-2):
        player_number += 5
    if player_number>comp_number:
        winner="player"
    elif player_number<comp_number:
        winner="computer"
    else:
        winner="nobody"
    print(winner + " wins!")
        
def compare_player_comp_m2(player_number,comp_number):
    diff = player_number - comp_number
    diff_module = diff % 5
    if (diff_module==1) or (diff_module==2):
        winner="player"
    elif (diff_module==3) or (diff_module==4):
        winner="computer"
    else:
        winner="nobody"
    print (winner + " wins!")
    
import random    
    
def rpsls(player_choice):
    print ("Player chooses " + player_choice)
    player_number=name_to_number(player_choice)
    if str(player_number).isdigit()==True: 
        comp_number= random.randrange(0,5,1) 
        comp_choice=number_to_name(comp_number)
        print ("Computer chooses "+ comp_choice)
        compare_player_comp_m2(player_number,comp_number) 
        print (" ")
    else:
        print(player_number)

# 对程序进行测试    
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
