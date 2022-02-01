import argparse
from re import T
from po_utils.base_objects import Page
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome import service
import sys
import time
import argparse
from random import choice as rand_choice


def _log_into_twitter_with_credentials(page: Page, username: str, password: str) -> bool:
    page.go_to_url('https://twitter.com/i/flow/login')
    time.sleep(1)
    page.send_text_to_element(('xpath', '//input[@type="text"]'), username)
    page.click_element(('xpath', '//*[text()="Next"]'))
    time.sleep(2)
    page.send_text_to_element(('xpath', '//input[@name="password"]'), password)
    page.click_element(('xpath', '//*[@data-testid="LoginForm_Login_Button"]'))
    return page.is_visible(('xpath', '//*[@data-testid="AppTabBar_Home_Link"]'))


def _write_tweet(page: Page, message):
    time.sleep(2)
    page.send_text_to_element(('xpath', '//*[@data-testid="tweetTextarea_0"]/div/div/div'), message)
    page.click_element(('xpath', '//*[@data-testid="tweetButtonInline"]'))


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', type=str)
    parser.add_argument('-p', type=str)
    parser.add_argument('-m', type=str, nargs='+')
    return parser.parse_args()


def main():
    args = _parse_args()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-dev-shm-usage')
    s = service.Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

    pg = Page(driver)

    is_logged_in = _log_into_twitter_with_credentials(pg, args.u, args.p)

    if not is_logged_in:
        print('something went wrong logging in')
        sys.exit(1)


    _write_tweet(pg, rand_choice(args.m))
    time.sleep(5)

    pg._driver.quit()

if __name__ == '__main__':
    main()
