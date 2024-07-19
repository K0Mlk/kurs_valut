from dotenv import load_dotenv
import aiohttp
import xml.etree.ElementTree as ET
import redis
import os 
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DB = os.getenv("REDIS_DB")
PRICES_CB = os.getenv("PRICES_CB")


class ExchangeRates:

    def __init__(self):
        try:
            self.redis_client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB
            )
            self.redis_client.ping()
            logging.info("Есть контакт!")
        except redis.RedisError as e:
            logging.error(f"Ошибка подключения к редиске: \n{e}")

    async def fetch_and_update_rates(self):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(PRICES_CB) as response:
                    data = await response.text()
                    await print(data)
                    self.update_rates(data)
                    
            except Exception as e:
                logging.error(f"Ошибка при получении данных с {PRICES_CB}: \n{e}")


    def update_rates(self, xml_data):
        try:
            root = ET.fromstring(xml_data)

            for currency in root.findall("Valute"):
                char_code = currency.find('CharCode').text
                value = currency.find('Value').text.replace(',', '.')
                self.redis_client.set(char_code, value)
        except ET.ParseError as e:
            logging.error(f"Ошибка при разборе XML данных: \n{e}")
        except Exception as e:
            logging.error(f"Ошибка при обновлении курсов: \n{e}")

    def get_rate(self, currency_code):
        try:
            rate = self.redis_client.get(currency_code)
            if rate is not None:
                return float(rate.decode('utf-8'))
            return None
        except redis.RedisError as e:
            logging.error(f"Ошибка при получении курса из Redis: \n{e}")
            return None