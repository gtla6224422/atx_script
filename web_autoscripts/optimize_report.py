# coding=utf-8
import logging
import time

def get_windows_img(driver):
        logger = logging.getLogger(__name__)
        file_path = 'D:/screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        print(screen_name)
        try:
            driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            #get_windows_img()