from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import string_resource



options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 브라우저를 머리없이 실행
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# ChromeDriverManager를 사용하여 ChromeDriver 설치
service = Service(ChromeDriverManager().install())

# 수정된 드라이버 생성 코드
driver = webdriver.Chrome(service=service, options=options)

# 웹사이트 접근
driver.get("http://www.nsgportal.net/")

# 결과 출력
print("Title of the page is:", driver.title.encode('cp850', 'replace').decode('cp850'))

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
print("Logged in page title:", driver.title.encode('cp850', 'replace').decode('cp850'))


#업무 활동 탭
login_button = driver.find_element(By.XPATH, string_resource.test)
login_button.click()
print("업무 활동 탭")


# 브라우저 종료
driver.quit()
업무 활동 탭")



# 브라우저 종료
driver.quit()
