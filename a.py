from redis import Redis



if __name__ == '__main__':
    try:
        redis_conn = Redis(db=0)
        # res = redis_conn.set('name', 'gsd')
        # res = redis_conn.get('name')
        # res = redis_conn.setex('aa', 30, 'aa')
        # res = redis_conn.mset({'name1':'zhangsan', 'name2':'lisi'})
        # res = redis_conn.mget('name1', 'name2')
        # res = redis_conn.append('name1', ' laowang')
        # res = redis_conn.rpush('l1', 'a', 'b', 'c', '老王')
        # redis_conn.linsert('l1', 'before', '老王', '老李')
        # redis_conn.linsert('l1', 'after', '老王', '老宋')
        # redis_conn.lset('l1', 1, '老胡')
        # redis_conn.lrem('l1', 1, 'a')
        # redis_conn.ltrim('l1', 1, -1)
        # redis_conn.hset('h1','name', '老于')
        # res = redis_conn.hkeys('h1')
        # res = redis_conn.hget('h1', 'age')
        # res = redis_conn.hmget('h1', 'age', 'name')
        # res = redis_conn.hvals('h1')
        # res = redis_conn.hdel('h1', 'age')
        # res = redis_conn.sadd('s1','1','2','3')
        # redis_conn.zadd('z1',{'d':'5','e':'6','f':'7'})
        # res = redis_conn.zrem('z1','a','b')
        # res = redis_conn.zrem('z1','a','b')
        res = redis_conn.zremrangebyscore('z1','3','5')
        print(res)
        # for i in res:
        #     print(i.decode('utf-8'))
        # print(res)
    except Exception as e:
        print(e)
