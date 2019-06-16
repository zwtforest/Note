# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(cache_path = True)
print('正在运行：')
todayWords = '文字介绍'
todayImage = 'D:\\中国美术馆\\人物画馆\\314.jpeg'


# 对所有好友群发图文消息
def GroupSends(todayWords,todayImage):
    FRIENDS = bot.friends()
    for FRIEND in FRIENDS:
        if FRIEND != FRIENDS[0]:
            try:
                FRIEND.send(todayWords)
                FRIEND.send_image(todayImage)
            except:
                print('error')

GroupSends(todayWords,todayImage)


# 回复 单独 my_friend 的加急消息 (优先匹配后注册的函数!)
@bot.register()
def reply_my_friend(msg):
    if msg.text != 'wali':
        MyMsg = '你好 我已保存该消息,看到后会及时回复，加急消息请发送指令：wali'
        return '{}\n你的消息：{} \n消息类型为({})'.format(MyMsg,msg.text, msg.type)
    
    else:
        
        wali = bot.friends().search('wali')[0]
        wali.send('{}启动了人工服务'.format(msg))
        return '你的消息：{} \n消息类型为({})已加急，小生会尽快为您服务'.format(msg.text, msg.type)

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('你好，我已经自动接受了你的好友请求')

bot.join()


