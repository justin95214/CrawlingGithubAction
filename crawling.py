from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import string_resource

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 브라우저를 머리없이 실행
options.add_argument("--no-sandbox")
options.add_argument('--window-size=1920,1080')  # 창 크기 지정
options.add_argument("--disable-dev-shm-usage")

# ChromeDriverManager를 사용하여 ChromeDriver 설치
service = Service(ChromeDriverManager().install())

# 수정된 드라이버 생성 코드
driver = webdriver.Chrome(service=service, options=options)

# 웹사이트 접근
driver.get("http://www.nsgportal.net/")
print(driver.title.encode('cp850', 'replace').decode('cp850'))


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

print(driver.title.encode('cp850', 'replace').decode('cp850'))
print('login completed!!')

# 로그인 후 처리할 작업
#work_activity_button = driver.find_element(By.XPATH, string_resource.work_activity)
#work_activity_button.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# '업무활동' 메뉴 클릭
# 요소가 나타날 때까지 대기
try:
    # 페이지의 JavaScript가 완료될 때까지 대기
    WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete'
    )

    # 이제 동적으로 생성된 요소에 대해 명시적 대기를 사용
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div/ul/li[3]/a'))
    )
    element.click()
except TimeoutException:
    print("요청한 요소를 찾는 데 시간이 너무 오래 걸립니다.")
except NoSuchElementException:
    print("요소를 찾을 수 없습니다.")
finally:
    driver.quit()


# 브라우저 종료
driver.quit()
