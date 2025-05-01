import requests

def send_telegram_message(message):
    token = '7936553385:AAFLT88_8rQJZ4cLqQyQ2vvNfavCnGD1Ly0'
    chat_id = '6657430178'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=payload)
    
send_telegram_message("✅ 任务完成，Python 脚本已执行完毕！")