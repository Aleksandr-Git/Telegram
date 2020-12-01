import asyncio

async def fun():
    print('privet')
    return 'privet' 


#print(fun())


async def test():
#    t = "ASDFGHJKLQWERTYUIOPZXCVBNM"
    print('jr')


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(test()), ioloop.create_task(fun())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()

#print(A)