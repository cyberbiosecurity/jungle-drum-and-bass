from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random
import requests
import winsound as ws

def alarm():
    m = 2
    c = 0
    return
    #ws.Beep(3000, 3000)
    #while c < m:
    #    ws.Beep(3000, 3000)
    #    time.sleep(10)
    #    c = c + 1

BOT_URL = "https://t.me/pirate_pigeon_bot"
BOT_API = "7767333296:drum-and-bass-battle-bot-logistics"
tickets = ['div[data-ti-train-card*="2004001|21:05:00|11:56:00"] div.column.right_block div[data-ti*="card_category"].top_bottom_prices_wrapper div div.column.card_price:not([data-ti="popup_card_price"]) span.seats_price','div[data-ti-train-card*="768А|2006004|2004001|16:44:00|12:28:00"] div.column.right_block div[data-ti*="card_category"].top_bottom_prices_wrapper div div.column.card_price:not([data-ti="popup_card_price"]) span.seats_price']

chat_ids = ['567274953','5426987331']

def parse_price(raw_text):
    clean_text = (
        raw_text
        .replace("\xa0", " ")
        .replace(" ", "")
        .replace("₽", "")
        .strip()
    )
    return int(clean_text) if clean_text.isdigit() else None


def send_telegram_alert(prices, chat_id=None):
    BOT_API = "8167324246:fuckyeahZGLYhIzJPTbSlmcc8goMsf7BrMKqa8"
    url = f"https://api.telegram.org/bot{BOT_API}/sendMessage"
    site_url = "https://www.tutu.ru/poezda/rasp_d.php?nnst1=2000000&nnst2=2004000&date=19.04.2025&date_second=20.04.2025"
    #message = f"🚨 CHEAP TICKET FOUND: {price} RUB!"
    message = f"🚨 Обновились билеты на 12-28!: {prices}!\n" + site_url
    if chat_id == None:
        chat_id = '5426987331'
    
    payload = {
        'chat_id': chat_id,
        'text': message
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Telegram alert sent successfully.")
        else:
            print(f"Failed to send alert: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error sending Telegram alert: {e}")


class Sniper():
    def __init__(self):
        self.cnt = 0
        self.BOT_URL = "https://t.me/pirate_pigeon_bot"
        self.BOT_API = "8167242396:fdfdfZGLYhIzJPTbSlmcc8goMsf7fdfMKqa8"
        self.tickets = ['div[data-ti-train-card*="2004001|21:05:00|11:56:00"] div.column.right_block div[data-ti*="card_category"].top_bottom_prices_wrapper div div.column.card_price:not([data-ti="popup_card_price"]) span.seats_price','div[data-ti-train-card*="768А|2006004|2004001|16:44:00|12:28:00"] div.column.right_block div[data-ti*="card_category"].top_bottom_prices_wrapper div div.column.card_price:not([data-ti="popup_card_price"]) span.seats_price']
        
        self.selector_template = 'div[data-ti-train-card*="XXXXXXX"] div.column.right_block div[data-ti*="card_category"].top_bottom_prices_wrapper div div.column.card_price:not([data-ti="popup_card_price"]) span.seats_price'
        #ticket date data
        #div[data-ti-train-card*="768А|2006004|2004001|16:44:00|12:28:00"] div.column.right_block div[data-ti*="card_category"].top_bottom_prices_wrapper div div.column.card_price:not([data-ti="popup_card_price"]) span.seats_price
        #div[data-ti-train-card*="2004001|21:05:00|11:56:00"] div.column.right_block div[data-ti*="card_category"].top_bottom_prices_wrapper div div.column.card_price:not([data-ti="popup_card_price"]) span.seats_price
        self.data = 'div[data-ti-train-card*="2004001|21:05:00|11:56:00"] div.column.right_block div[data-ti*="card_category"].top_bottom_prices_wrapper div div.column.card_price:not([data-ti="popup_card_price"]) span.seats_price'
        self.dates = ['2004001|21:05:00|11:56:00', '768А|2006004|2004001|16:44:00|12:28:00']
        
        self.data = 'div[data-ti-train-card*="768А|2006004|2004001|16:44:00|12:28:00"] div.column.right_block div[data-ti*="card_category"].top_bottom_prices_wrapper div div.column.card_price:not([data-ti="popup_card_price"]) span.seats_price'
        
        self.chat_ids = ['567274953','5426987331']
        self.last_tickets = []
        self.URL = 'https://www.tutu.ru/poezda/rasp_d.php?nnst1=2000000&nnst2=2004000&date=19.04.2025&date_second=20.04.2025'


    def get_prices(self, driver):
        try:
            #price_spans = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.selector_template.replace("XXXXXXX", self.tickets[0]))))
            driver.get("https://www.tutu.ru/poezda/rasp_d.php?nnst1=2000000&nnst2=2004000&date=19.04.2025&date_second=20.04.2025")
            price_spans = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.data)))
            
            cheapest_price = None
            prices = []
            for span in price_spans:
                raw_text = span.get_attribute("textContent")
                price = parse_price(raw_text)
                prices.append(price)
                print("PRICE: " + str(price))
                print("PRICES: " + str(prices))
                #if self.last_tickets != prices
                #if price and (cheapest_price is None or price < cheapest_price):
                #    cheapest_price = price
            
            return prices
        
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def monitor_tickets(self):
        driver = webdriver.Chrome()
        #driver.get("https://www.tutu.ru/poezda/rasp_d.php?nnst1=2000000&nnst2=2004000&date=19.04.2025&date_second=20.04.2025")
        
        try:
            while True:
                self.cnt = self.cnt + 1
                print(self.cnt, time.ctime())
                prices = self.get_prices(driver)
                

                if prices != self.last_tickets: #new prices??
                    self.last_tickets = prices
                    print(f"🚨 TICKETs updated: {str(prices)}")
                    for chat in self.chat_ids:
                        #send_telegram_alert(str(prices))  # Send alert to Telegram
                        send_telegram_alert(str(prices), chat_id=chat)
                        
                        time.sleep(1)
                    print("b4 alarm")
                    alarm()
                    print("after alarm")
                delay = 10 + random.randint(0, 30)
                print("start sleep")
                time.sleep(delay)
                print("done sleep")
        finally:
            driver.quit()


if __name__ == "__main__":
    sniper = Sniper()
    sniper.monitor_tickets()