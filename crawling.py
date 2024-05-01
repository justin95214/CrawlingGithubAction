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
import time

import openai


# OpenAI API 키 설정
openai.api_key = ''  # 실제 API 키로 변경해야 합니다.

# ChatGPT 모델과 대화하는 함수 정의
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 선택한 모델로 교체
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']



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
password.send_keys("j1995214!!")


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
from selenium.webdriver.common.alert import Alert


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
    project_title.send_keys("VIS 검사프로그램 개발")

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

    #코드 입력
    project_code = driver.find_element(By.XPATH, '/html/body/form/div/div[2]/fieldset/div[1]/input')
    project_code.send_keys("20240060")

    #코드 이름 클릭
    find_search = driver.find_element(By.XPATH,'/html/body/form/div/div[2]/fieldset/div[3]/input')
    find_search.click()
    
    #코드 이름 클릭
    find_project_name = driver.find_element(By.XPATH,'/html/body/form/div/div[3]/table/tbody/tr/td[2]')
    find_project_name.click()

    time.sleep(3)
    da = Alert(driver)
    da.accept()

    print('selected project name')

    #업무 일지 이동
    driver.switch_to.window(driver.window_handles[1])
    #수행시간
    project_time = driver.find_element(By.XPATH, '/html/body/div/div[3]/form/table[1]/tbody/tr[4]/td[1]/input')
    project_time.send_keys("8")

    written_date = driver.find_element(By.XPATH, '/html/body/div/div[3]/form/table[1]/tbody/tr[1]/td[2]/input')
    print(written_date.text)

    prompt_text = "vis 프로그램 테스트 및 머신러닝 의사결정 트리 알고리즘 개선에 대해서 2문장으로 요약해줘 "
    answer = "오전에 설계미팅 및 양면 검사 장비 및 슈트형 검사 장비 형정으로 이송. 초분광 머신러닝 모델 시스템 CI/CD -docker, mlflow 설치 및 구동 적용 "#chat_with_gpt(prompt_text)
    print(answer)
    
    #프로젝트 내용 
    project_content = driver.find_element(By.XPATH, '/html/body')
    project_content.send_keys(answer)
    print("내용 입력 완료")

    #프로젝트 저장
    project_save = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[4]/a[1]')
    project_save.click()
    print("프로젝트 업무일지 저장")

except TimeoutException:
    print("요청한 요소를 찾는 데 시간이 너무 오래 걸립니다.")
except NoSuchElementException:
    print("요소를 찾을 수 없습니다.")
finally:
    driver.quit()


# 브라우저 종료
driver.quit()
