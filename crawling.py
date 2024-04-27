from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import string_resource

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
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


print('login in window')
# 아이디와 비밀번호 입력
username = driver.find_element(By.XPATH,  string_resource.id_edit)
password = driver.find_element(By.XPATH, string_resource.ps_edit)

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
from selenium.webdriver.common.action_chains import ActionChains
# '업무활동' 메뉴 클릭
# 요소가 나타날 때까지 대기
try:
    # 새 탭을 열고 싶은 경우, Body에서 Control + T를 보내기
    driver.execute_script("window.open('');")
    
    # 새로 열린 탭으로 이동
    driver.switch_to.window(driver.window_handles[1])
    
    # 새 탭에서 다른 웹 사이트 열기
    #https://www.nsgportal.net/ekp/workDiary/workDiary.do?cmd=eng_wd_write
    driver.get("http://www.nsgportal.net/ekp/workDiary/workDiary.do?cmd=eng_wd_write")

    # 업무 일지 화면 확인
    work_title = driver.find_element(By.XPATH, '/html/body/div/div[1]/h3').text
    print(work_title)

    #프로젝트 제목 입력
    project_title = driver.find_element(By.XPATH, '/html/body/div/div[3]/form/table[1]/tbody/tr[1]/td[1]/input')
    project_title.send_keys("VIS 검사프로그램 개발")

    # 검색 버튼 클릭
    search_button = driver.find_element(By.XPATH, '/html/body/div/div[3]/form/table[1]/tbody/tr[3]/td[1]/a[1]')
    search_button.click()
    
    #프로젝트 코드 검색 창
    # 새로 열린 탭으로 이동
    driver.switch_to.window(driver.window_handles[2])
    driver.get('https://www.nsgportal.net/ekp/workDiary/workDiary.do?cmd=eng_wd_pj_pop')

    # 프로젝트 검색 창 이동 확인
    project_window = driver.find_element(By.XPATH, '/html/body/form/div/div[1]/h3').text
    print(project_window)


except TimeoutException:
    print("요청한 요소를 찾는 데 시간이 너무 오래 걸립니다.")
except NoSuchElementException:
    print("요소를 찾을 수 없습니다.")
finally:
    driver.quit()


# 브라우저 종료
driver.quit()
