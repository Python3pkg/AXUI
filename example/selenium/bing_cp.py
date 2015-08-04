
import AXUI

config_file = "selenium.cfg"
app_map = "www.bing.com.xml"

AXUI.Config(config_file)
appmap = AXUI.AppMap(app_map)

appmap.browser.start(browser_name="Firefox") 

appmap.browser.searchEdit.Keyboard.input("AXUI")
appmap.browser.goButton.Mouse.left_click()
