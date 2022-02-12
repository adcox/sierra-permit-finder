
"""
Useful docs:
    * https://selenium-python.readthedocs.io
"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def test():

    # NOTE - can set the permit type and date via the URL request - Have to decode
    # the numbers into trail IDs though...
    # GET https://www.recreation.gov/api/permitinyo/233262/availability?start_date=2022-02-01&end_date=2022-02-28&commercial_acct=false

    url = 'https://www.recreation.gov/permits/233262/registration/detailed-availability?type=overnight-permit&date=2022-02-11'

    driver = webdriver.Firefox()
    driver.get(url)

    # Select permit type
    permitSelect = Select(driver.find_element(By.ID, 'permit-type'))
    permitSelect.select_by_value('overnight-exiting-mt-whitney')
    #permitSelect.select_by_value('overnight')

    # Set group size to 1
    groupSizeEl = driver.find_element(By.ID, 'number-inpute')
    groupSizeEl.send_keys('1')

    # Clock the "No" on commercial trip option
    commTripRadio = driver.find_element(By.ID, 'prompt-answer-no1')
    commTripRadio.click()

    wait(5)

    rows = driver.find_elements(By.CSS_SELECTOR, '.rec-grid-grid .rec-grid-row')
    for row in rows:
        # Get cells
        cells = row.find_elements(By.CLASS_NAME, 'rec-grid-grid-cell')

        if len(cells) > 0:
            trailID = cells[0].text
            trailname = cells[1].text
            area = cells[2].text
            quota = cells[3].text
            print(f'{trailname} ({trailID}) in {area} area has {quota}')

    # #rec-grid-grid
    #   #rec-grid-row
    #     #rec-grid-grid-cell, role="gridcell"
    #       1st cell: ID
    #       2nd cell: Entry Points
    #       3rd cell: Area
    #       4th cell: quota for selected date (class .rec-availability-date)

    driver.close()
