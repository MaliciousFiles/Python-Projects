import os.path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from time import sleep
import sys

def playZork():
    global browser
    with open('zork.txt', 'r+') as zorkFile:
        if zorkFile.read() != '':
            restart = input('Would you like to continue with your previous save?(y/n)\n')
            while restart != "y" and restart != "n":
                restart = input('Would you like to continue with your previous save?(y/n)\n')
            if restart == "n":
                check = input("Are you sure you want to wipe your save data?(y/n)\n")
                while check != "y" and check != "n":
                    check = input("Are you sure you want to wipe your save data?(y/n)\n")

    try:
        if check == "y":
            open('/Users/malcolmroalson/Documents/Python/zork.txt', 'w').close()
    except NameError:
        pass

    PROJECT_ROOT = os.path.abspath(os.path.dirname('chromedriver'))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver")

    options = webdriver.ChromeOptions();
    options.add_argument("--kiosk");
    browser = webdriver.Chrome(executable_path = DRIVER_BIN, options=options)

    browser.get("http://zorkonline.net/play.html?story=stories/zork1.z3")

    sleep(2)

    def zork(zorkCommand):
        command = "document.getElementsByClassName('TextInput')[0].value = '%s'"%zorkCommand
        browser.execute_script(command)
        browser.find_element_by_class_name('TextInput').send_keys(Keys.RETURN)

    with open('/Users/malcolmroalson/Documents/Python/zork.txt', 'r') as zorkFile:
            for line in zorkFile:
                    index = 0
                    run = ''
                    for char in line:
                            try:
                                    if char=='\n':
                                            pass
                                    else:
                                            run += char
                                    index += 1
                            except IndexError:
                                    run += char
                                    index += 1
                    try:
                        if ' ****  You have died  **** ' in browser.find_element_by_class_name('lastinput').find_element_by_xpath('..').get_attribute("innerHTML"):
                            browser.close()
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    zork(run)

    lastinput = ''

    try:
        while True:
            try:
                if lastinput != browser.find_element_by_class_name('lastinput').find_element_by_xpath('..').get_attribute("innerHTML"):
                    with open('zork.txt', 'a+') as zorkFile:
                        save=''
                        for char in browser.find_element_by_class_name('lastinput').find_element_by_xpath('..').get_attribute("innerHTML"):
                            if char == '\n':
                                break
                            else:
                                save += char
                        if not 'ZORK' in save:
                            zorkFile.write(save+'\n')
                    lastinput = browser.find_element_by_class_name('lastinput').find_element_by_xpath('..').get_attribute("innerHTML")
            except (AttributeError, selenium.common.exceptions.NoSuchElementException):
                pass
    except (AttributeError, selenium.common.exceptions.NoSuchWindowException):
        try:
            browser.close()
        except selenium.common.exceptions.NoSuchWindowException:
            pass
playZork()
playAgain = input("Would you like to play again?(y/n)\n")
while playAgain != "y" and playAgain != "n":
    playAgain = input("Would you like to play again?(y/n)\n")
if playAgain == "y":
    playZork()
else:
    sys.exit()
