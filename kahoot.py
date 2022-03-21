import time
import threading
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class KahootBotter:

    def __init__(self):
        self.running = False

    def dispatch_bot(self, pin, name):
        options = Options()

        options.add_argument('--incognito')

        options.add_argument("--headless")

        options.add_argument("--enable-precise-memory-info")

        options.add_argument("--disable-default-apps")

        options.add_argument("--use-fake-ui-for-media-stream")

        options.add_argument("test-type")

        options.add_argument("--js-flags=--expose-gc")

        options.add_argument("--log-level=3")
        

        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(driver, 20)

        driver.get("https://kahoot.it")

        wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div[3]/div[2]/main/div/form/button')))

        driver.find_element(by=By.XPATH, value='//*[@id="game-input"]').send_keys(pin)

        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/div/div[3]/div[2]/main/div/form/button').click()

        wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="nickname"]')))

        driver.find_element(by=By.XPATH, value='//*[@id="nickname"]').send_keys(u'\u200b'.join(name))

        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/div/div[3]/div[2]/main/div/form/button').click()

        while self.running:

            time.sleep(1)

        driver.close()

        driver.quit()

    def start(self, gamepin, botcount, prefix):

        self.running = True

        for i in range(botcount):

            threading.Thread(target=self.dispatch_bot, args=(gamepin, f'{prefix}-{i}')).start()

    def stop(self):

        self.running = False


if __name__ == '__main__':

    pininput = str(input("Kahoot Game Pin: "))

    countinput = int(input("Amount of Bots: "))

    prefixinput = str(input("Prefix for Bots: "))

    botter = KahootBotter()

    try:
        print('Starting Bots')

        botter.start(pininput, countinput, prefix)

    except KeyboardInterrupt:
        print('Stopping', end='')

        botter.stop()

        print('Succesfully Botted!')
