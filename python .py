from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Informasi login
email = "email_anda@gmail.com"
password = "password_anda"

# Mengatur opsi Chrome
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")  # Menjalankan Chrome dalam mode headless agar lebih hemat resource
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Proxy gratis
proxy = "http://your_proxy_here:port"  # Ganti dengan proxy Anda
chrome_options.add_argument(f'--proxy-server={proxy}')

# Inisialisasi WebDriver
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)  # Menggunakan WebDriverWait untuk menunggu elemen muncul

try:
    # Membuka YouTube
    logger.info("Membuka YouTube...")
    driver.get("https://www.youtube.com")
    time.sleep(2)

    # Klik tombol login
    logger.info("Menunggu tombol login YouTube...")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/a')))
    login_button.click()

    # Masukkan email
    logger.info("Memasukkan email...")
    email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
    email_input.send_keys(email)
    email_input.send_keys(Keys.RETURN)

    time.sleep(2)  # Tunggu untuk pengalihan halaman

    # Masukkan password
    logger.info("Memasukkan password...")
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)  # Tunggu proses login selesai

    # Menonton video (ubah URL sesuai kebutuhan)
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Ganti dengan URL video yang ingin Anda tonton
    logger.info(f"Menonton video: {video_url}")
    driver.get(video_url)
    time.sleep(60)  # Menonton selama 1 menit (ubah sesuai kebutuhan)

    logger.info("Selesai menonton video")

except Exception as e:
    logger.error(f"Terjadi kesalahan: {e}")

finally:
    driver.quit()
    logger.info("Browser ditutup")
