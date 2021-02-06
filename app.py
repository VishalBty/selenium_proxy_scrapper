from selenium import webdriver #to import selenium library
options = webdriver.ChromeOptions() # add options to chrome 
options.add_argument('headless') #hide chrome mode while scraping
driver = webdriver.Chrome(chrome_options=options) # start chrome

driver.get(input("Enter proxy list url: ")) #put url to scrap here
tbody = driver.find_element_by_tag_name("tbody") # store the table data to tbody 
cell = tbody.find_elements_by_tag_name("tr") # find all table rows and store it
for column in cell:
  column = column.text.split(" ") # split the now content with space as a separator
  print (column[0]+":"+column[1]) #print 1st and second column
driver.quit() # exit chrome
#done
