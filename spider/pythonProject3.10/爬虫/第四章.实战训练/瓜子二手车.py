from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()
driver.get("https://m.guazi.com/list?tk_p_mti=5.1.c2c_wap_mall.app_index.gold_fixed-fixed.0")
wait = WebDriverWait(driver,10)
before = driver.current_window_handle
confirm_btn = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR,'#tab2-2 > div.btn-center > a')
    )
)
confirm_btn.click() #点击查看更多
