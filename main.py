from dingtalkchatbot.chatbot import DingtalkChatbot

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=c59f24fc2866621ba9244dce43ad16a3519e3033a2dd73459ddbd962024a9f1e'
xiaoding = DingtalkChatbot(webhook)
xiaoding.send_text(msg='Привет, ебалайки!', is_at_all=True)