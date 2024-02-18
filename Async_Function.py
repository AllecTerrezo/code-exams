import asyncio

async def async_function(items: list) -> list:
    
    for value in items:
        # With each iteration the value index is fetched and the number of seconds will grow exponentially in base 2
        seconds = 2 ** items.index(value)
        # Delay adicionado a cada iteração do loop
        await asyncio.sleep(seconds)
        print(value)

# Example:
list = ["a", "b", "c", "d", "e", "f"]
asyncio.run(async_function(list))

