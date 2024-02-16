import asyncio

async def async_function(items: list) -> list:
    
    for value in items:
        # A cada iteração o index do value é buscado e a quantidade de segundos crescerá exponencialmente na base 2
        seconds = 2 ** items.index(value)
        # Delay adicionado a cada iteração do loop
        await asyncio.sleep(seconds)
        print(value)

# Example:
list = ["a", "b", "c", "d", "e", "f"]
asyncio.run(async_function(list))

