import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('9tCt4xaZGm45WAqnWBPs3GdaNt++EDAw2hvGZcCNxVM0BdJhwWmtM6Ut3HWTMB8xhRRg0IaMZ91PXL7fC3zwrlP+rKeMlk23IdzM2OHO1KStqQvOnamzuxVsLNahtVDTYMwruMWu2wZucPJ3iLyD8QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7d4cbf295eaecce53055692d3165cc61')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message="Apakah ,apakah ")
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="iya , bisa jadi , tidak , mungkin , coba sekali lagi"))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
