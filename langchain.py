from langchain_community.chat_models.fireworks import ChatFireworks
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
import os
import asyncio

# 安全配置（使用環境變量管理密鑰）
os.environ["FIREWORKS_API_KEY"] = "sk-9b7ac00915ea4a7a84310c2d6bbcad9b"


def build_translation_chain():
    """构建翻译链"""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一台专业级翻译机器，遵循以下规则："
                   "\n1. 自动检测输入语言"
                   "\n2. 严格保持{style}风格"
                   "\n3. 保留专业术语"),
        ("human", "请将以下内容翻译为{target_lang}：\n{text}")
    ])

    model = ChatFireworks(
        model="accounts/fireworks/models/fireworks-chat-ultra",
        temperature=0.2,
        max_tokens=2048,
        streaming=True
    )

    return (
            RunnablePassthrough.assign(
                style=lambda x: x.get("style", "专业"),
                target_lang=lambda x: x["target_lang"].upper()
            )
            | prompt
            | model
    )


async def translation_service():
    """交互式翻译服务核心逻辑"""
    chain = build_translation_chain()

    print("🗣️ 智能翻译引擎就绪（输入'exit'退出）")
    while True:
        try:
            command = input("\n格式：目标语言 文本（例：JA 量子计算机）\n> ").strip()
            if command.lower() in ('exit', 'quit'):
                break

            if ' ' not in command:
                raise ValueError("请输入：目标语言 + 空格 + 文本")

            target_lang, text = command.split(' ', 1)
            response = await chain.ainvoke({
                "target_lang": target_lang,
                "text": text
            })

            print(f"\n🔍 翻译结果：{response.content}")

        except Exception as e:
            print(f"🚨 错误：{str(e)}")


if __name__ == "__main__":
    asyncio.run(translation_service())