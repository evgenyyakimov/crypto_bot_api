import requests
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Введите название криптовалюты')


@dp.message_handler()
async def get_coin(message:types.message):
    try:
        headers = {
            'cache - control': 'max - age = 30, public, must - revalidate, s - maxage = 30',
            'content - type': 'application / json'
        }

        r = requests.get(url=f'https://api.coingecko.com/api/v3/coins/{message.text}', headers=headers)

        coin = r.json()['symbol']
        price = r.json()["market_data"]["current_price"]["usd"]
        price_percentage_24h = r.json()["market_data"]["price_change_percentage_24h_in_currency"]["usd"]

        await message.reply(f'Монета: {coin}\n Цена: {price}\n Изменение цены за 24 ч в %: {price_percentage_24h}\n')
    except:
        await message.reply('Проверьте название монеты!')

if __name__ == '__main__':
    executor.start_polling(dp)