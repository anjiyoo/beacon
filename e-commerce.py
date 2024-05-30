from deco_time import time_logger
import time

@time_logger("dbconnection")
def sql():
    time.sleep(3)
    print("결제 되었습니다.")
sql()