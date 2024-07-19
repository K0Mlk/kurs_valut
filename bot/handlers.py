from aiogram import types
from aiogram.enums import ParseMode
from services.exchange_rates import ExchangeRates

exchange_rates = ExchangeRates()

async def cmd_start(message: types.Message):
    
    await message.answer(
        f"""Приветствую тебя, <b>{message.from_user.full_name}</b>
        \n\nЭтот бот отрабатывает по командам:
        \nПоказывает актуальный курс - /rates
        Определяет стоимость валюты - /exchange 
        \nФормат использования /exchange:
        \n/exchange USD RUB 10
        \nДанная команда отображает стоимость 10 долларов в рублях""",
        parse_mode=ParseMode.HTML
    )

async def cmd_exchange(message: types.Message):
    args = message.text.split()
    
    if len(args) != 4:
        await message.answer("Пример использования: /exchange USD RUB 10")
        return
    
    from_currency, to_currency, amount_str = args[1], args[2], args[3]
    
    try:
        amount = float(amount_str)
    except ValueError:
        await message.answer("Количество должно быть числом")
        return
    
    from_rate = exchange_rates.get_rate(from_currency)
    to_rate = exchange_rates.get_rate(to_currency)

    if from_rate is None or to_rate is None:
        await message.answer('Неверный код валюты!')
        return
    
    result = (from_rate / to_rate) * amount
    await message.answer(f"{amount} {from_currency} = {result:.2f} {to_currency}")

async def cmd_rates(message: types.Message):
    currencies = ["USD", "EUR", "RUB"]
    rates = {}
    for currency in currencies:
        rate = exchange_rates.get_rate(currency)
        if rate is None:
            await message.answer(f"Не удалось получить курс для {currency}")
            return
        rates[currency] = rate

    response = "\n".join([f"{currency}: {rates[currency]}" for currency in currencies])
    await message.answer(response)