import logging

# 配置日志记录
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def important_function():
    logging.info("Starting important function")
    # 函数具体逻辑
    logging.info("Ending important function")