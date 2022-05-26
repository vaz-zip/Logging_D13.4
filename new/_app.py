import redis

red = redis.Redis(
    host='redis://:@127.0.0.1:6379/0',
    # 'redis://'+'127.0.0.1'+'6379'+'/0',  # 'redis-17188.c8.us-east-1-2.ec2.cloud.redislabs.com',  # 'localhost'
    port=6379,  # 17188,  # ,
    charset="UTF-8",
    decode_responses=True
    # db=0
    # password='jmPxy4TYtYlmyOzdt0B1EBbYU8pOKEPm'
)
