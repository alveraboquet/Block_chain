
from nb_log import LogManager, get_logger

# logger = LogManager('log_demo').get_logger_and_add_handlers(log_filename='APITest.log')
logger = get_logger(name="all_log", is_add_stream_handler=True, log_path="./",
                    log_filename='practice.log',
                    ding_talk_token = '1cae5e2214fe56e209086ca20c3e0d7b3fc8128a9442289a85ab52cdc2996cd6',
                    ding_talk_time_interval =0.1,
                    formatter_template=2)

a = "wolrd"
print("这是一段话")
logger.info(f'你好{a}')
logger.warning("监控报警: 这是警号第2次")


i = 0
def area(x, y):
    global i
    i = x * y
    return i
a = b = 3
print(area(a, b),i)  # i输出为9

