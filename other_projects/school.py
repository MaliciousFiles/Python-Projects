import subprocess

try:
    import pip
    del pip
except ModuleNotFoundError:
    subprocess.call("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py", shell=True)
    if subprocess.call("python get-pip.py") == 1:
        subprocess.call("python get-pip.py --user")

try:
    from playsound import playsound
except ModuleNotFoundError:
    subprocess.call("pip3 install playsound", shell=True)
    from playsound import playsound

try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import selenium.common.exceptions as exceptions
except ModuleNotFoundError:
    subprocess.call("pip3 install selenium", shell=True)
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import selenium.common.exceptions as exceptions

try:
    import sounddevice as sd
except ModuleNotFoundError:
    subprocess.call("pip3 install sounddevice", shell=True)
    import sounddevice as sd

try:
    import requests
except ModuleNotFoundError:
    subprocess.call("pip3 install requests", shell=True)
    import requests

try:
    from mkdir import mkdir
except ModuleNotFoundError:
    subprocess.call("pip3 install mkdir", shell=True)
    from mkdir import mkdir

try:
    from colorama import Back
    from colorama import Style
    import colorama
except ModuleNotFoundError:
    subprocess.call("pip3 install colorama", shell=True)
    from colorama import Back
    from colorama import Style
    import colorama

try:
    from win_toaster import create_toast
except ModuleNotFoundError:
    subprocess.call("pip3 install win_toaster", shell=True)
    from win_toaster import create_toast

from time import sleep
import sys
import datetime
import time
import os.path
import zipfile
import platform
import webbrowser

colorama.init()

# ----- To be able to change OS specific calls -----
WINDOWS = "Windows"
MACOS = "Darwin"
OPERATING_SYSTEM = platform.system()

if OPERATING_SYSTEM != WINDOWS and OPERATING_SYSTEM != MACOS:
    raise OSError(f"Unfortunately, this program does not support your operating system({OPERATING_SYSTEM}) yet.")

if OPERATING_SYSTEM == MACOS:
    try:
        from playsound import playsound
    except ModuleNotFoundError:
        subprocess.call("pip3 install playsound", shell=True)
        from playsound import playsound
# --------------------------------------------------

CLEAR = "cls" if OPERATING_SYSTEM == WINDOWS else "clear" if OPERATING_SYSTEM == MACOS else ""

CHROMEDRIVER_PATH = os.path.expanduser("~/Documents/Python/bin/chromedriver.exe") if OPERATING_SYSTEM == WINDOWS else os.path.expanduser("~/Documents/Python/bin/chromedriver") if OPERATING_SYSTEM == MACOS else ""
ALARM_PATH = os.path.expanduser("~/Documents/Python/Assets/Sounds/alarm.wav")
ICON_PATH = os.path.expanduser("~/Documents/Python/Assets/Icons/school.ico")
SYSTEMVOL_PATH = os.path.expanduser("~/Documents/Python/bin/systemvol.exe")

CHROMEDRIVER_PATH = os.path.abspath(CHROMEDRIVER_PATH)
ALARM_PATH = os.path.abspath(ALARM_PATH)
ICON_PATH = os.path.abspath(ICON_PATH)
SYSTEMVOL_PATH = os.path.abspath(SYSTEMVOL_PATH)

credentialsSaved = True
coursesSaved = True

activeClass = None

def changeLineByNumber(newText, *lines):
    content = []
    with open(__file__, "r") as f:
        for l in f:
            content.append(l)
    
    with open(__file__,"w") as f:
        for line in lines:
            content[line-1] = newText + "\n"
        for line in content:
            f.write(line)

def changeLineByText(oldText, newText, stopAfter=-1):
    sleep(0.5)
    content = []
    with open(__file__, "r") as f:
        for l in f:
            content.append(l)
            
    with open(__file__, "w") as f:
        for line in content:
            if oldText in line and stopAfter != 0:
                line = newText + "\n"
                stopAfter -= 1
                
            f.write(line)

courseNames = [['Spanish', 'Geometry', 'Wind Ensemble', 'US History'], ['Physical Education', 'Science', 'English Language Arts', 'Jazz Band']]
tuClub = 'D&D'
thClub = 'D&D'

subprocess.call(CLEAR, shell=True)

if len(courseNames[0]) != 4 or len(courseNames[1]) != 4:
    for x in range(1, 9):
        if x <= 4:
            courseNames[0] += [input(f"What the name for your A{x} in BLEND? ")]
        else:
            courseNames[1] += [input(('\n' if x == 5 else '') + f"What the name for your B{x} in BLEND? ")]

if tuClub == '':
    tuClub = input(f"\nWhat the name for your Tuesday Club in BLEND? ")
if thClub == '':
    thClub = input(f"What the name for your Thursday Club in BLEND? ")

if not coursesSaved:
    if input("\nSave the course names?(y[es]/n[o]) ").lower() == 'y':
        changeLineByText("courseNames = ", f"courseNames = {courseNames}", 1)
        changeLineByText("tuClub = ", f"tuClub = '{tuClub}'", 1)
        changeLineByText("thClub = ", f"thClub = '{thClub}'", 1)
        changeLineByText("coursesSaved = ", "coursesSaved = True", 1)

        coursesSaved = True
        
def installChromedriver():
    if not os.path.exists(os.path.dirname(CHROMEDRIVER_PATH)):
        mkdir(os.path.dirname(CHROMEDRIVER_PATH))
        
    if OPERATING_SYSTEM == WINDOWS:
        chromeversion = subprocess.check_output(r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value', shell=True).decode()
    elif OPERATING_SYSTEM == MACOS:
        chromeversion = subprocess.check_output("osascript -e 'get version of application \"Google Chrome\"'", shell=True).decode().replace("\n", "")

    url = "https://chromedriver.storage.googleapis.com/" + requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE_" + ".".join(chromeversion.replace("\r", "").replace("\n", "").split("=")[-1].split(".")[0:3])).text + ("/chromedriver_win32.zip" if OPERATING_SYSTEM == WINDOWS else "/chromedriver_mac64.zip" if OPERATING_SYSTEM == MACOS else "") 

    subprocess.call("curl %s -o %s"%(url, CHROMEDRIVER_PATH + ".zip"), shell=True)
    zipfile.ZipFile(CHROMEDRIVER_PATH + ".zip").extractall(os.path.abspath('bin'))

    subprocess.call(("del " if OPERATING_SYSTEM == WINDOWS else "rm " if OPERATING_SYSTEM == MACOS else "") + CHROMEDRIVER_PATH + ".zip", shell=True)
    if OPERATING_SYSTEM == MACOS:
        subprocess.call(f"chmod +x {CHROMEDRIVER_PATH}", shell=True)

if not os.path.exists(CHROMEDRIVER_PATH):
    installChromedriver()

options = webdriver.ChromeOptions()
options.add_argument("disable-gpu")
options.add_argument("disable-infobars")
options.add_argument("--disable-notifications")

while True:
    try:
        browser = webdriver.Chrome(executable_path = CHROMEDRIVER_PATH, options=options)
        break
    except OSError:
        installChromedriver()

browser.get("https://sites.google.com/a/kealingmiddleschool.org/kealing-middle-school/home")

mDay = str(time.localtime().tm_mday)
dateID = 'day-%s%s%s'%(time.localtime().tm_year, time.localtime().tm_mon, mDay if len(mDay) == 2 else '0' + mDay)

attCount = 0
while True:
    attCount += 1

    sleep(0.5)
    
    try:
        browser.switch_to.frame(0)
        browser.switch_to.frame(0)
        break
    except exceptions.NoSuchFrameException:
        pass

    if attCount >= 5:
        break

dayText = None

for x in range(15):
    sleep(0.2)
    try:
        try:
            dayText = browser.find_element_by_id(dateID).find_element_by_class_name("event-title").text.split()[0].lower()
        except IndexError:
            continue
    except exceptions.NoSuchElementException:
        pass
    
browser.switch_to.default_content()

if dayText == None:
    input("Today is not a school day! (ENTER/RETURN)\n")
    raise AssertionError("Today is not a school day!")
    quit()

aDay = True if 'a' in dayText else False if 'b' in dayText else None

if aDay == None:
    input("Today is not a school day! (ENTER/RETURN)\n")
    raise AssertionError("Today is not a school day!")
    quit()

zoomLinks = []
blendLinks = []
times = ["745", "920", "1055", "1300", "1430"]

courses = courseNames[not aDay] + [tuClub if time.localtime().tm_wday == 1 else thClub if time.localtime().tm_wday == 3 else "Advisory"]

## This is for web-scraping the times, if the site ever comes back up. ##
#
#browser.get("https://sites.google.com/a/kealingmiddleschool.org/kealing-middle-school/about-us/bell-schedule-a-b-rotation")
#fonts = browser.find_elements_by_tag_name("font")
#toggle = True
#for font in fonts:
#    if ("am" in font.text or "pm" in font.text) and font.get_attribute("color")== "#ff0000":
#        if toggle:
#            hrMin = ""
#            if "am" in font.text:
#                hrMin = font.text.replace(":", "").replace(" am", "")
#            elif "pm" in font.text:
#                split = font.text.replace(" pm", "").split(":")
#                hour = split[0]
#                hrMin = (hour if len(hour) == 2 else str(int(hour)+12)) + split[1]
#            if len(times) < len(courseNames[0]):
#                times.append(hrMin)
#        toggle = not toggle
try:
    browser.get("https://aisdblend.instructure.com")
except exceptions.WebDriverException as e:
    if "ERR_NAME_NOT_RESOLVED" in e:
        print(AssertionError("Could not connect to the internet. Check your connection and try again"))
        input("Press ENTER(RETURN) to continue")
        quit()
        
while True:
    usr = 's10020414'
    passwd = 'Tater2007aisd-8'

    if not credentialsSaved:
        usr = input ("AISD username: " )
        paswd = input("AISD password: ")
        
        if input("Save credentials?(y[es]/n[o]) ").lower() == 'y':
            changeLineByText("usr = ", f"    usr = '{usr}'", 1)
            changeLineByText("passwd = ", f"    passwd = '{passwd}'", 1)
            changeLineByText("credentialsSaved = ", "credentialsSaved = True", 1)
            credentialsSaved = True

    repeat = True
    while repeat:
        try:
            browser.find_element_by_id("identification").send_keys(usr + Keys.RETURN)
            repeat = False
        except exceptions.NoSuchElementException:
            pass
    sleep(0.1)
    repeat = True
    while repeat:
        try:
            browser.find_element_by_id("pwd").find_element_by_tag_name("div").find_element_by_tag_name("div").find_element_by_tag_name("input").send_keys(passwd + Keys.ENTER)
            repeat = False
        except exceptions.NoSuchElementException:
            pass
    try:
        sleep(0.1)
        browser.find_element_by_class_name("error-message")
        print("Credentials wrong!")
        if credentialsSaved:
            update = input("Update saved credentials?(y[es]/n[o]) ")
            if (update == 'y'):
                changeLineByText("usr = ", f"    usr = ''", 1)
                changeLineByText("passwd = ", f"    paswd = ''", 1)
                changeLineByText("credentialsSaved = ", "credentialsSaved = False", 1)
                credentialsSaved = False
        browser.find_element_by_id("authn-startover-button").click()
        for button in browser.find_elements_by_tag_name("button"):
            if button.text == "Ok":
                button.click()
                break
    except exceptions.NoSuchElementException:
        break

sleep(0.5)
browser.find_element_by_id("global_nav_profile_link").click()
sleep(0.5)
while True:
    try:
        name = browser.find_elements_by_class_name("emyav_fAVi")[0].text.split(" ")[0]
        break
    except IndexError:
        pass
dayIndex = 0 if aDay else 1

for courseIndex in range(len(courses)):
    course = courses[courseIndex]
    browser.find_element_by_id("global_nav_courses_link").click()

    tryCount = 0
    found = False
    while not found:
        tryCount += 1

        sleep(0.6)
        try:
            try:
                try:
                    try:
                        browser.find_element_by_link_text(course).click()
                        found = True
                    except exceptions.StaleElementReferenceException:
                        browser.find_element_by_id("global_nav_courses_link").click()
                except exceptions.ElementClickInterceptedException:
                        try:
                            browser.find_element_by_link_text(course).click()
                            found = True
                        except exceptions.ElementClickInterceptedException:
                            pass

            except exceptions.NoSuchElementException:
                try:
                    browser.find_element_by_id("global_nav_courses_link").click()
                    browser.find_element_by_link_text(course).click
                    found=True
                except exceptions.NoSuchElementException:
                    newCourse = input(f"Could not find course '{course}'. Would you like to re-enter it?(y[es]/n[o]/r[etry])").lower()
                    if tryCount >= 15 and coursesSaved and  newCourse == 'y':
                        newCourse = input("What is the new course name?\n")
                        courses[courseIndex] = newCourse
                        course = newCourse
                        courseNames[dayIndex][courseIndex] = newCourse
                        changeLineByText("courseNames = ", f"courseNames = {courseNames}", 1)

                    if newCourse == 'y' or newCourse == 'r':
                        tryCount = 0
                        continue

            if tryCount >= 15:
                break
        except exceptions.NoSuchElementException:
             browser.find_element_by_id("global_nav_courses_link").click()

    if not found:
        blendLinks.append('')
        zoomLinks.append('')
        continue
    
    blendLinks.append(browser.current_url)
    
    try:
        sleep(0.1)
        zooms = []
        url=''
        
        for a in browser.find_elements_by_tag_name("a"):
            if "zoom" in a.get_attribute("href").lower():
                zooms.append(a)
        for link in zooms:
            if "aisdblend" in link.get_attribute("href"):
                while True:
                    try:
                        try:
                            link.click()
                        except exceptions.ElementClickInterceptedException:
                            link.click()
                    except exceptions.StaleElementReferenceException:
                        browser.back()
                        sleep(0.2)
                        link.click()
                    sleep(0.1)
                    urls = []
                    try:
                        browser.find_element_by_partial_link_text("zoom")
                        urls += browser.find_elements_by_parital_link_text("zoom")
                    except exceptions.NoSuchElementException:
                        urls += browser.find_elements_by_partial_link_text("Zoom")
                    try:
                        url = urls[0]
                        break
                    except IndexError:
                        pass
                if len(urls) > 1:
                    for a in urls:
                        parent=a
                        stop=False
	
                        while True:
                            try:
                                parent = parent.find_element_by_xpath("..")
                            except exceptions.InvalidSelectorException:
                                break

                            for p in parent.find_elements_by_tag_name("p"):
                                if ("a" if aDay else "b") + str(courseIndex + 5 * (dayIndex)) in p.text.lower():
                                    url=a
                                    stop=True
                                    break
                        if stop: break

                if "aisdblend" in url.get_attribute("href"):
                    continue
    
                break
            else:
                url = zooms[0]
                if len(zooms) > 1:
                    try:
                        if name in link.get_attribute("alt"):
                            url = link
                        else:
                            tds = link.find_element_by_xpath("..").find_element_by_xpath("..").find_elements_by_tag_name("td")
                            for x in range(len(tds)):
                                try:
                                    if tds[x].find_element_by_tag_name("a") == link:
                                        if ("A" if aDay else "B") + str(courseIndex + 5 * (dayIndex)) in tds[x-2].find_element_by_tag_name("span").text:
                                            url = link
                                except exceptions.NoSuchElementException:
                                    pass
                    except TypeError:
                        pass
        zoomLinks.append(url.get_attribute("href"))
    except exceptions.NoSuchElementException as e:
        print(f"LINE {sys.exc_info()[2].tb_lineno}: {e}")
        input("Press ENTER(RETURN) to continue")
        continue

browser.close()
browser.quit()

readableTimes = [str(x[:-2] if int(x[:-2])<=12 else int(x[:-2])-12) + ":" + x[-2:] for x in times]

nameSize = max(len(name) for name in courses) + 3 # extra 3 spaces
timeSize = max(len(time) for time in readableTimes) + 1 # extra 1 space
dashLine = ""
for x in range(nameSize + timeSize + 3): dashLine += "-"

def printSchedule():    
    subprocess.call(CLEAR, shell=True)
    
    print(dashLine)
    for index in range(len(courses)):
        nameLine = courses[index]
        
        if zoomLinks[index] == "" and zoomLinks[index] == "":
            continue
        
        for x in range(nameSize - len(nameLine)): nameLine += " "
        timeLine = readableTimes[index]
        for x in range(timeSize - len(timeLine)): timeLine += " "
        print(f"{Style.BRIGHT+Back.GREEN if courses[index] == activeClass else ''}|{nameLine}|{timeLine}|{Style.RESET_ALL}")
    print(dashLine)

if OPERATING_SYSTEM == WINDOWS:
    mkdir(os.path.dirname(ICON_PATH))
    if not os.path.exists(ICON_PATH):
        subprocess.call(f"curl https://maliciousfiles.github.io/file-downloads/School.py/assets/school.ico -o {ICON_PATH}")
    mkdir(os.path.dirname(SYSTEMVOL_PATH))
    if not os.path.exists(SYSTEMVOL_PATH):
        subprocess.call(f"curl https://maliciousfiles.github.io/file-downloads/School.py/assets/systemvol.exe -o {SYSTEMVOL_PATH}")
    
    def getVolume():
        return subprocess.check_output(os.path.abspath("bin\systemvol.exe"))

    def setVolume(volume):
        subprocess.call(r'%s %s'%(os.path.abspath("bin\systemvol.exe"), volume))

elif OPERATING_SYSTEM == MACOS:
    def getVolume():
        return subprocess.check_output("osascript -e 'output volume of (get volume settings)'")

    def setVolume(volume):
        subprocess.call(f"osascript -e 'set volume {volume}'")

def timeToString(time):
    return str(time.hour) + ("0" if len(str(time.minute)) == 1 else "") + str(time.minute)

def openClasses(blendLink, zoomLink):
    if blendLink != "":
        webbrowser.open(blendLink)

    if zoomLink != "":
        webbrowser.open(zoomLink)

mkdir(os.path.dirname(ALARM_PATH))
if not os.path.exists(ALARM_PATH):
    subprocess.call(f"curl https://maliciousfiles.github.io/file-downloads/School.py/assets/alarm.wav -o {ALARM_PATH}")
printSchedule()

while True:
        try:
            now = datetime.datetime.now()
            hourMinute = timeToString(now)
            if hourMinute in times:
                index = times.index(hourMinute)
                zoomLink = zoomLinks[index]
                blendLink = blendLinks[index]
                if (zoomLink != "" or blendLink != "") and now.second == 0:
                    activeClass = courses[index]

                    oldVolume = str(int(getVolume()))
                    
                    setVolume(50)
                    if "headphones" in list(sd.query_devices())[sd.default.device[1]]['name'].lower():
                        setVolume(25)
                        
                    if OPERATING_SYSTEM == WINDOWS:
                        print("notifying")
                        create_toast(f"{activeClass} - {readableTimes[index]}",
                                     "Click to open the links",
                                     duration=15,
                                     icon_path=ICON_PATH,
                                     sound_path=ALARM_PATH,
                                     tooltip=f"School Reminders - {activeClass}",
                                     callback_on_click=lambda:openClasses(blendLink, zoomLink),
                                     kill_without_click=False
                                    ).display()
                    elif OPERATING_SYSTEM == MACOS:
                        playsound(ALARM_PATH)
                    
                    setVolume(oldVolume)
                    
                    printSchedule()

                    if OPERATING_SYSTEM == MACOS:
                        openClasses(blendLink, zoomLink)
                
                    if hourMinute == times[-1]:
                        exit()

            for hourMin in times:
                if now.second == 0 and hourMinute == timeToString(datetime.datetime(now.year, now.month, now.day, int(hourMin[:-2]), int(hourMin[-2:])) + datetime.timedelta(1/24, 30*60)):
                    activeClass = None

                    printSchedule()
        except Exception as e:
            print(f"LINE {sys.exc_info()[2].tb_lineno}: {e}")
            input("Press ENTER(RETURN) to continue")

