from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import string_resource

from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # GUI 없이 실행
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

"""
# 옵션 설정
options = Options()
options.add_argument("--headless")  # GUI 없이 실행
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 드라이버 설정
chromedriver_path = '/usr/lib/chromium-browser/chromedriver'
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# 웹사이트 접근
driver.get("http://www.nsgportal.net/")

# 결과 출력
print("Title of the page is:", driver.title)


# 콤보 박스에서 '농심엔지니어링' 선택
company_select = Select(driver.find_element(By.XPATH, string_resource.nongshim_group_list))
company_select.select_by_visible_text('농심엔지니어링')

# 아이디와 비밀번호 입력
username = driver.find_element(By.XPATH,  string_resource.id_edit)
password = driver.find_element(By.XPATH, string_resource.ps_edit)

print('login in')
username.send_keys("2022037")
password.send_keys("j1995214!")

# 로그인 버튼 클릭
login_button = driver.find_element(By.XPATH, string_resource.login_button)
login_button.click()

print('login completed!!')
# 로그인 후 처리할 작업
# 예: 페이지 타이틀 출력
print("Logged in page title:", driver.title)


#업무 활동 탭
login_button = driver.find_element(By.XPATH, string_resource.test)
login_button.click()
print("업무 활동 탭")
"""


# 브라우저 종료
driver.quit()
