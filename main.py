import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def login_with_cookies():
    # Screenshots save karne ke liye folder banayen
    os.makedirs("screenshots", exist_ok=True)

    cookies_json = os.environ.get('FB_COOKIES')
    
    if not cookies_json:
        print("❌ Error: FB_COOKIES secret nahi mila!")
        return

    cookies = json.loads(cookies_json)

    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    # Headless mein full screen set karna zaroori hai taake screenshot acha aaye
    driver.set_window_size(1920, 1080)

    try:
        print("🌐 Facebook par ja rahe hain...")
        driver.get("https://www.facebook.com/404") 
        time.sleep(3)

        print("🍪 Cookies inject kar rahe hain...")
        for cookie in cookies:
            if 'facebook.com' in cookie.get('domain', ''):
                driver.add_cookie({
                    'name': cookie['name'],
                    'value': cookie['value'],
                    'domain': cookie['domain'],
                    'path': cookie['path']
                })

        driver.get("https://www.facebook.com/")
        print("⏳ Page load hone ka wait kar rahe hain...")
        time.sleep(5)

        if "log in" in driver.title.lower() or "login" in driver.title.lower():
            print("❌ Login Failed! Cookies expire ho chuki hain ya galat hain.")
            driver.save_screenshot("screenshots/error_login.png")
        else:
            print(f"✅ Login Successful! Current Page: {driver.title}")
            
            # --- SABOOT K LIYE RECORDING & SCROLLING ---
            print("📸 Saboot ke liye screenshots aur scrolling shuru...")
            
            # Pehla screenshot login hoty hi
            driver.save_screenshot("screenshots/1_login_done.png")
            
            # 10 second tak loop chalega
            end_time = time.time() + 10
            count = 2
            
            while time.time() < end_time:
                # Page ko 800 pixels neechay scroll karo
                driver.execute_script("window.scrollBy(0, 800);")
                print(f"🔽 Scrolling down... (Screenshot {count})")
                time.sleep(2) # 2 second ruko page load hone k liye
                driver.save_screenshot(f"screenshots/{count}_scrolling.png")
                count += 1
                
            print("✅ 10 Second ki scrolling aur screenshots complete!")

    except Exception as e:
        print(f"❌ Koi masla aa gaya: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    login_with_cookies()
















# import os
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# def login_with_cookies():
#     # GitHub Secrets se FB_COOKIES uthana
#     cookies_json = os.environ.get('FB_COOKIES')
    
#     if not cookies_json:
#         print("❌ Error: FB_COOKIES secret nahi mila!")
#         return

#     # JSON text ko Python list mein convert karna
#     cookies = json.loads(cookies_json)

#     # 2026 ke hisab se Headless aur Stealth options
#     chrome_options = Options()
#     chrome_options.add_argument("--headless=new") 
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
#     # Notifications aur popups block karna
#     prefs = {"profile.default_content_setting_values.notifications": 2}
#     chrome_options.add_experimental_option("prefs", prefs)

#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()

#     try:
#         print("🌐 Facebook par ja rahe hain...")
#         # Step 1: Facebook ke domain par jana (Cookies add karne se pehle zaroori hai)
#         driver.get("https://www.facebook.com/404") 
#         time.sleep(3)

#         # Step 2: Extract ki gayi cookies ko browser mein inject karna
#         print("🍪 Cookies inject kar rahe hain...")
#         for cookie in cookies:
#             if 'facebook.com' in cookie.get('domain', ''):
#                 driver.add_cookie({
#                     'name': cookie['name'],
#                     'value': cookie['value'],
#                     'domain': cookie['domain'],
#                     'path': cookie['path']
#                 })

#         # Step 3: Main page par wapas aana taake login confirm ho jaye
#         driver.get("https://www.facebook.com/")
#         time.sleep(5)

#         # Step 4: Login verify karna
#         if "log in" in driver.title.lower() or "login" in driver.title.lower():
#             print("❌ Login Failed! Cookies expire ho chuki hain ya galat hain.")
#         else:
#             print(f"✅ Login Successful! Current Page: {driver.title}")
            
#             # ---------------------------------------------------------
#             # Yahan se aage aap apni auto-posting ka automation laga sakte hain
#             # Example: driver.get("Aapke_Facebook_Group_Ya_Page_Ka_Link")
#             # ---------------------------------------------------------

#     except Exception as e:
#         print(f"❌ Koi masla aa gaya: {e}")
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     login_with_cookies()
