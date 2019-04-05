# -*-coding:utf-8-*-
from selenium import webdriver
import time


class Isqlplus():
    SQL = 'select * from cat;'
    driver = webdriver.Firefox()
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(15)
    ip = []
    username = ''
    password = ''
    sign = ''
    default_ip = []

    def __init__(self,  user, password, sign='rj2', ip=default_ip):
        self.ip = ip
        self.username = user
        self.password = password
        self.sign = sign

    def login(self):

        i = -1
        while True:
            if i >= 8:
                i = -1
            else:
                i += 1
            try:
                self.driver.get(self.ip[i])
                break
            except Exception:
                print(self.ip[i]+"connect failed")
                continue
        print("Ip : " + self.ip[i - 1])
        time.sleep(10)
        elem = self.driver.find_element_by_id('M__Id')
        elem.send_keys(self.username)
        elem = self.driver.find_element_by_id('M__Ida')
        elem.send_keys(self.password)
        elem = self.driver.find_element_by_id('M__Idb')
        elem.send_keys(self.sign)
        elem.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[7]/td[3]/a/img").click()
        return

    def sql(self, new_sql=SQL):

        new_elem = self.driver.find_element_by_tag_name('textarea')
        new_elem.clear()
        new_elem.send_keys(new_sql)
        new_elem.find_element_by_xpath("/html/body/div[1]/div[3]/form/a[1]/img").click()
        return

    def run(self):
        self.login()
        time.sleep(5)
        self.sql()
        return

    def always_run(self):
        self.login()
        time.sleep(15)
        while True:
            self.sql()
            time.sleep(10)
            self.sql('commit;')
            time.sleep(10)
        return


s = Isqlplus()
s.always_run()
