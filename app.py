import openai
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.exceptions import LineBotApiError

# Line Messaging APIの設定
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

# ChatGPT APIの設定
openai.api_key = "YOUR_API_KEY"
model_engine = "text-davinci-002"

# メッセージイベントが発生した場合に実行される関数
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # ユーザーからのメッセージを取得
    user_message = event.message.text
    try:
        # ChatGPT APIを使用して応答を生成
        response = openai.Completion.create(
          engine=model_engine,
          prompt=user_message,
          max_tokens=60
        )
        # 応答を取得
        bot_response = response.choices[0].text.strip()
        # Lineに応答を返信する
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=bot_response))
    except:
        # エラーが発生した場合は、エラーメッセージを返信する
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Sorry, something went wrong.'))
if __name__ == '__main__':
    app.run()
