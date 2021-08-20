from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/driver/chromedriver.exe")
driver.maximize_window();

driver.get("http://localhost/form.php")
driver.find_element_by_name("NIP").send_keys("12345")
driver.find_element_by_name("Nama").send_keys("John Wick")
driver.find_element_by_name("NIK").send_keys("061120301")
driver.find_element_by_name("Alamat").send_keys("Tangerang")
driver.find_element_by_name("Perusahaan").send_keys("Fiktif Inc.")
driver.find_element_by_name("Tanggal").send_keys("01/01/2021")
driver.find_element_by_name("Divisi").send_keys("HRD")
driver.find_element_by_name("Posisi").send_keys("staff")
driver.find_element_by_name("Gaji").send_keys("1000000")
driver.find_element_by_name("Atasan").send_keys("Jack Reacher")
driver.find_element_by_name("Submit").click()