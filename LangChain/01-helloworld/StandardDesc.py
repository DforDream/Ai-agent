"""
【案例】标准/工程化写法：用 LangChain 调用大模型（invoke + stream）

对应教程章节：第 10 章 - LangChain 快速上手与 HelloWorld → 6、实战：企业级封装与流式输出

本案例演示从零到一的完整工程化写法：
- 用通义/阿里云兼容接口通过 LangChain 发问，掌握 invoke（一次性返回）与 stream（流式返回）两种调用方式。
- 将「初始化模型」封装成函数便于复用；用 .env 存密钥、logging 打日志、try/except 区分错误，符合正式项目习惯。
- 运行前在项目根目录配置 .env 中的 QWEN_API_KEY，执行：python 案例与源码-2-LangChain框架/01-helloworld/StandardDesc.py

补充说明：
- 为了让工程化示例更直观，这里继续使用很多同学在旧资料里更常见的 `ChatOpenAI` 写法；若你想看 1.x 统一入口，请对照同目录下的 `LangChainV1.0.py`。
- 当前脚本使用的是“阿里百炼兼容端点 + DeepSeek 模型”这组组合，重点仍然是学习工程化写法，而不是限定某一个具体模型。
"""

from langchain.chat_models import (
    init_chat_model,
)
import os
from dotenv import load_dotenv
from langchain_core.exceptions import LangChainException

load_dotenv(encoding="utf-8")

import logging
_log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, _log_level, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

def init_llm_client() -> init_chat_model:
    api_key = os.getenv("QWEN_API_KEY")
    if not api_key:
        raise ValueError("环境变量 QWEN_API_KEY 未配置，请检查 .env 文件")
    return init_chat_model(
        model="qwen3.8-2.4t-a95b",
        model_provider="openai",  # 阿里百炼为 OpenAI 兼容接口
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,  # 控制「随机程度」：0 更确定、重复性高；1 更随机、更有创意。一般 0.5～0.8 即可。
        max_tokens=2048,  # 单次回复最多生成多少个 token（约等于字数），防止回复过长或超限。
    )

def main():
    try:
        llm = init_llm_client()
        logger.info("LLM客户端初始化成功")
        question = "你是谁"
        response = llm.invoke(question)
        logger.info(f"问题：{question}")
        logger.info(f"回答：{response.content}")
        print("==================== 以下是流式输出（另一种调用方式）")
        print("*" * 50)
        response_stream = llm.stream("介绍下 langchain，300字以内")
        for chunk in response_stream:
            print(chunk.content, end="")  # end="" 表示不换行，紧挨着打
        print()  # 流式结束后补一个换行，避免和后续输出粘在一起
    except ValueError as e:
        # 例如：.env 里没配 QWEN_API_KEY，init_llm_client 里会 raise ValueError
        logger.error(f"配置错误：{str(e)}")
    except LangChainException as e:
        # 例如：网络失败、API 限流、模型返回异常等，LangChain 会抛出 LangChainException
        logger.error(f"模型调用失败：{str(e)}")
    except Exception as e:
        # 其他没预料到的错误都归到这里，避免程序静默崩溃
        logger.error(f"未知错误：{str(e)}")

if __name__ == "__main__":
    main()