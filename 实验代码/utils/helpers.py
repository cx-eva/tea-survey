from datetime import datetime

def get_current_time():
    """
    获取格式化的当前时间
    
    Returns:
        str: 格式化的当前时间字符串
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')