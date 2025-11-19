import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# APIキーを取得
api_key = os.getenv("OPENAI_API_KEY")
