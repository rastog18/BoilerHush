import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pickle
import time
from selenium.webdriver import ActionChains


class Scraper(object):

    def __init__(self):
        self.action = None
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        # self.chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        # self.file = open("data.dat", "wb")

    def scrape(self, place):
        import time
        self.driver.get("https://www.google.com/")
        search_box = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        search_box.send_keys(place, Keys.ENTER)
        time.sleep(1)
        popular_times = self.driver.find_elements(By.CLASS_NAME, "kFDszc")
        pop_timing = []
        for time in popular_times:
            pop_timing.append(time.value_of_css_property("height"))
        if pop_timing:
            pop_timing = [math.floor(float(j.rstrip('px'))) for j in pop_timing]
        timing = self.driver.find_element(By.CLASS_NAME, "JjSWRd")
        timing = timing.text
        address = self.driver.find_element(By.CLASS_NAME, "LrzXr")
        address = address.text

        dict = {
            "name": place,
            "address": address,
            "Time": timing,
            "popular times": pop_timing
        }
        pickle.dump(dict, self.file)
        self.file.flush()

    def start_distance(self, building):
        url = "https://www.google.com/maps"
        self.action = ActionChains(self.driver)
        self.driver.get(url)
        self.distance(building)

    def distance(self, building):
        field = self.driver.find_element(By.ID, "searchboxinput")
        field.send_keys(building + ', Purdue University, West Lafayette IN 47906, United States', Keys.ENTER)
        time.sleep(1)
        # Method 2
        self.driver.maximize_window()
        time.sleep(15)
        canvas = self.driver.find_element(By.XPATH, '//*[@id="fDahXd"]')
        self.action.move_to_element(canvas).perform()
        self.action.context_click(canvas).perform()
        time.sleep(5)
        coords = self.driver.find_element(By.CSS_SELECTOR, '.mLuXec')
        print(f"{building}: {coords.text}")
        coords = coords.text.split(",")
        return coords

        # Method 1
        # wait = WebDriverWait(self.driver, 10)
        # main_canvas = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='canvas']")))
        # size = main_canvas.size
        # w, h = size['width'], size['height']
        # new_w = w / 2
        # new_h = h / 2
        # # ActionChains(self.driver).move_by_offset(new_w, new_h).pause(5).perform()
        # # time.sleep(2)
        # ActionChains(self.driver).move_by_offset(new_h, new_h).pause(1).perform()
        # wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='canvas']"))).click()

    def close(self):
        # self.file.close()
        self.driver.close()
        # url = self.driver.find_element()
        # data = requests.get()
        # soup = BeautifulSoup(data, "html.parser")
        # soup.prettify()
