from selenium import webdriver
import time

login = ''
password = ''



def ya_aouth(login,password):
    driver = webdriver.Chrome('C:\pets\chromedriver.exe')
    driver.get("https://passport.yandex.ru/auth/")
    login_str = driver.find_element_by_xpath('//*[@id="passp-field-login"]').send_keys(login)
    login_button = driver.find_element_by_xpath('//*[@id="passp:sign-in"]').click()
    time.sleep(0.5)
    password_str = driver.find_element_by_xpath('//*[@id="passp-field-passwd"]').send_keys(password)
    password_button = driver.find_element_by_xpath('//*[@id="passp:sign-in"]').click()
    time.sleep(1)
    if driver.current_url == 'https://passport.yandex.ru/auth/phone':
        not_now_button = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div[3]/button').click()
    time.sleep(1)
    if driver.current_url == 'https://passport.yandex.ru/profile':
        return 'login'
    elif driver.current_url == 'https://passport.yandex.ru/auth/changepassword':
        recover_password_button = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/button').click()
        return ('Please, enter captcha - ', driver.current_url)
    else:
        time.sleep(1)
        return (f'Something wrong, current url - {driver.current_url}')


