import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# .envファイルを読み込む
load_dotenv()

# APIキーを取得
api_key = os.getenv("OPENAI_API_KEY")

# LLMの初期化
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, api_key=api_key)

# Streamlitアプリ
st.title("専門家に質問しよう！")

st.write("#####歴史上の人物について質問しよう！#####")
st.write("例：『織田信長はどのような人物ですか？』")
st.write("#####都道府県について質問しよう！#####")
st.write("例：『北海道の有名な観光地はどこですか？』")



# ラジオボタンで専門家を選択
expert_type = st.radio(
    "専門家を選択してください",
    ["日本の歴史", "都道府県"]
)

# プロンプトテンプレートの設定
if expert_type == "日本の歴史":
    system_message = "あなたは日本の歴史について詳しい専門家です。日本の歴史上の人物について入力された質問に答えてください。"
else:
    system_message = "あなたは都道府県に詳しい専門家です。都道府県について入力された質問に答えてください。"

# 入力フォーム
user_input = st.text_input("質問を入力してください")

# 送信ボタン
if st.button("送信"):
    if user_input:
        with st.spinner("回答を生成中..."):
            # プロンプトの作成
            prompt = ChatPromptTemplate.from_messages([
                ("system", system_message),
                ("user", "{input}")
            ])
            
            # チェーンの作成と実行
            chain = prompt | llm
            response = chain.invoke({"input": user_input})
            
            # 結果の表示
            st.write("### 回答:")
            st.write(response.content)
    else:
        st.warning("お聞きしたい質問を入れてください")
