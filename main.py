
import os
import json
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

messages = [
    "RCB vs GT live match HD mein dekhne ke liye link check karein! 🏏🔥",
    "Kohli vs Gill! Match live on my website. Link in first comment! 🚀"
]

def login_and_post():
    # Screenshots folder setup
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
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 10)

    try:
        # ==========================================
        # LOGIN PROCESS (Already tested & working)
        # ==========================================
        print("🌐 Facebook par ja rahe hain...")
        driver.get("https://www.facebook.com/404") 
        time.sleep(3)

        for cookie in cookies:
            if 'facebook.com' in cookie.get('domain', ''):
                driver.add_cookie({
                    'name': cookie['name'],
                    'value': cookie['value'],
                    'domain': cookie['domain'],
                    'path': cookie['path']
                })

        driver.get("https://www.facebook.com/")
        time.sleep(6)

        if "log in" in driver.title.lower() or "login" in driver.title.lower():
            print("❌ Login Failed!")
            driver.save_screenshot("screenshots/0_Login_Failed.png")
            return
        
        print("✅ Login Successful! Posting start kar rahe hain...")
        driver.save_screenshot("screenshots/0_Login_Success.png")

        # Image path setup for GitHub Server (Requires '1.png' in the repo)
        image_path = os.path.abspath("1.png")
        if not os.path.exists(image_path):
            print("⚠️ Tasveer '1.png' repository mein nahi mili! Isko upload zaroor karein.")

        # ==========================================
        # STEP 1: CREATE POST POPUP KHOLNA
        # ==========================================
        print("\n▶️ STEP 1: Post box dhoond rahe hain...")
        driver.save_screenshot("screenshots/Step1_Start.png")
        try:
            create_post_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label, "What\'s on your mind") or contains(@aria-label, "Create a post")]')))
            driver.execute_script("arguments[0].click();", create_post_btn) # JS Click to avoid interception
            time.sleep(4)
        except Exception as e:
            print("❌ 'What's on your mind?' button nahi mila.")
        driver.save_screenshot("screenshots/Step1_End.png")

        # ==========================================
        # STEP 2: TEXT TYPE KARNA
        # ==========================================
        print("\n▶️ STEP 2: Text box dhoond rahe hain...")
        driver.save_screenshot("screenshots/Step2_Start.png")
        try:
            text_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]//div[@role="textbox" and @contenteditable="true"]')))
            text = random.choice(messages)
            hashtags = " #RCBvGT #CricketLive"
            full_text = text + hashtags
            print(f"Text Type Kar Rahe Hain: {full_text}")
            text_box.send_keys(full_text)
            time.sleep(3)
        except Exception as e:
            print("❌ Text box popup mein nahi mila.")
        driver.save_screenshot("screenshots/Step2_End.png")

        # ==========================================
        # STEP 3: IMAGE UPLOAD KARNI HAI
        # ==========================================
        print("\n▶️ STEP 3: Photo/Video option dhoond rahe hain...")
        driver.save_screenshot("screenshots/Step3_Start.png")
        try:
            photo_icon = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]//div[@aria-label="Photo/video"]')))
            driver.execute_script("arguments[0].click();", photo_icon)
            time.sleep(2)
            
            if os.path.exists(image_path):
                file_input = driver.find_element(By.XPATH, '//div[@role="dialog"]//input[@type="file"]')
                print("Tasveer upload ho rahi hai...")
                file_input.send_keys(image_path) # Selenium file upload
                time.sleep(6)
        except Exception as e:
            print("⚠️ File input ya photo icon nahi mila.")
        driver.save_screenshot("screenshots/Step3_End.png")

        # ==========================================
        # STEP 4: NEXT BUTTON DABANA
        # ==========================================
        print("\n▶️ STEP 4: Next button dhoond rahe hain...")
        driver.save_screenshot("screenshots/Step4_Start.png")
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Next"][role="button"]')
            driver.execute_script("arguments[0].click();", next_btn)
            print("✅ 'Next' button daba diya.")
            time.sleep(4)
        except Exception as e:
            print("❌ Next button nahi mila (Shayad direct Post button aa gaya ho).")
        driver.save_screenshot("screenshots/Step4_End.png")

        # ==========================================
        # STEP 4.5: POST BUTTON YA EARLY POPUP CLOSE 
        # ==========================================
        print("\n▶️ STEP 4.5: Post button check kar rahe hain...")
        driver.save_screenshot("screenshots/Step4.5_Start.png")
        try:
            post_btn = driver.find_elements(By.XPATH, '//div[@aria-label="Post" and @role="button"]')
            if not post_btn:
                post_btn = driver.find_elements(By.XPATH, '//span[text()="Post"]')
            
            if post_btn:
                driver.execute_script("arguments[0].click();", post_btn[0])
                print("✅ 'Post' button daba diya.")
            else:
                print("⚠️ 'Post' nahi mila! Shayad popup aagaya hai.")
                close_early = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Close"][role="button"]')
                if close_early:
                    driver.execute_script("arguments[0].click();", close_early[0])
                    print("✅ Pehla Popup 'Close' kar diya.")
        except Exception as e:
            pass
        driver.save_screenshot("screenshots/Step4.5_End.png")

        # ==========================================
        # STEP 4.8: ZIDDI POPUP HUNTER
        # ==========================================
        print("\n▶️ STEP 4.8: Ab 8 seconds wait karke 2 dafa annoying popups check karenge...")
        driver.save_screenshot("screenshots/Step4.8_Start.png")
        for i in range(2):
            time.sleep(8) 
            print(f"🔍 Check {i+1}/2: Popup 'Close' button dhoond rahe hain...")
            try:
                popup_close_btn = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Close"][role="button"]')
                if popup_close_btn:
                    driver.execute_script("arguments[0].click();", popup_close_btn[0])
                    print(f"✅ BINGO! Popup pakra gaya aur attempt {i+1} mein uda diya.")
                else:
                    print(f"☑️ Rasta saaf hai. Koi popup nahi mila.")
            except:
                pass
        driver.save_screenshot("screenshots/Step4.8_End.png")

        # ==========================================
        # STEP 5: FINAL "SHARE NOW" BUTTON
        # ==========================================
        print("\n▶️ STEP 5: Final Share button dhoond rahe hain...")
        driver.save_screenshot("screenshots/Step5_Start.png")
        try:
            share_now_btn = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Share now"][role="button"]')
            if not share_now_btn:
                share_now_btn = driver.find_elements(By.XPATH, '//span[text()="Share now" or text()="Publish" or text()="Share"]')

            if share_now_btn:
                driver.execute_script("arguments[0].click();", share_now_btn[0])
                print("✅ 'Share now' button daba diya.")
                time.sleep(8)
                print("🎉 BINGO! Facebook Post 100% Successful.")
            else:
                print("⚠️ Final Share button nahi mila (Shayad post pehle hi publish ho chuka hai).")
        except Exception as e:
            pass
        driver.save_screenshot("screenshots/Step5_End.png")

    except Exception as e:
        print(f"⚠️ HOUSTON, WE HAVE A PROBLEM: {e}")
    finally:
        print("\nScript ka kaam khatam ho gaya. Browser band kar rahe hain...")
        driver.quit()
        print("✅ Browser successfully khatam ho gaya!")

if __name__ == "__main__":
    login_and_post()



























# =========== Good job, facebook open hu raha hai and screenshot saaboot hai beloe code mei, aaabbb opper facebook uplaod waala system add akrty hai inshallah ================



# import os
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# def login_with_cookies():
#     # Screenshots save karne ke liye folder banayen
#     os.makedirs("screenshots", exist_ok=True)

#     cookies_json = os.environ.get('FB_COOKIES')
    
#     if not cookies_json:
#         print("❌ Error: FB_COOKIES secret nahi mila!")
#         return

#     cookies = json.loads(cookies_json)

#     chrome_options = Options()
#     chrome_options.add_argument("--headless=new") 
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
#     prefs = {"profile.default_content_setting_values.notifications": 2}
#     chrome_options.add_experimental_option("prefs", prefs)

#     driver = webdriver.Chrome(options=chrome_options)
#     # Headless mein full screen set karna zaroori hai taake screenshot acha aaye
#     driver.set_window_size(1920, 1080)

#     try:
#         print("🌐 Facebook par ja rahe hain...")
#         driver.get("https://www.facebook.com/404") 
#         time.sleep(3)

#         print("🍪 Cookies inject kar rahe hain...")
#         for cookie in cookies:
#             if 'facebook.com' in cookie.get('domain', ''):
#                 driver.add_cookie({
#                     'name': cookie['name'],
#                     'value': cookie['value'],
#                     'domain': cookie['domain'],
#                     'path': cookie['path']
#                 })

#         driver.get("https://www.facebook.com/")
#         print("⏳ Page load hone ka wait kar rahe hain...")
#         time.sleep(5)

#         if "log in" in driver.title.lower() or "login" in driver.title.lower():
#             print("❌ Login Failed! Cookies expire ho chuki hain ya galat hain.")
#             driver.save_screenshot("screenshots/error_login.png")
#         else:
#             print(f"✅ Login Successful! Current Page: {driver.title}")
            
#             # --- SABOOT K LIYE RECORDING & SCROLLING ---
#             print("📸 Saboot ke liye screenshots aur scrolling shuru...")
            
#             # Pehla screenshot login hoty hi
#             driver.save_screenshot("screenshots/1_login_done.png")
            
#             # 10 second tak loop chalega
#             end_time = time.time() + 10
#             count = 2
            
#             while time.time() < end_time:
#                 # Page ko 800 pixels neechay scroll karo
#                 driver.execute_script("window.scrollBy(0, 800);")
#                 print(f"🔽 Scrolling down... (Screenshot {count})")
#                 time.sleep(2) # 2 second ruko page load hone k liye
#                 driver.save_screenshot(f"screenshots/{count}_scrolling.png")
#                 count += 1
                
#             print("✅ 10 Second ki scrolling aur screenshots complete!")

#     except Exception as e:
#         print(f"❌ Koi masla aa gaya: {e}")
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     login_with_cookies()
















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
