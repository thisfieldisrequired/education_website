import redis


redis_client = redis.Redis(host='localhost', port=6379, db=0)

print(redis_client)
redis_client.set('var', 2)
print(int(redis_client.get(name='var')))
redis_client.close()
