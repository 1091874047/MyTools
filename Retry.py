import time


# 重试装饰器

def MyRetry(func):
    def wrapper(*args, **kwargs):
        flage = 0  # 重试次数标志
        max_time = 1  # 最大重试次数
        while True:
            if flage >= max_time:
                raise Exception('超过重试次数')
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # pass
                print(e)
            flage += 1
            time.sleep(3)

    return wrapper
