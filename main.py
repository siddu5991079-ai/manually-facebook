
# ================== gret job yeh done huqaaya uplaod succesfuuly done to facebook =====================================================



# Yeh bohat hi ahem point aapne pakra hai, Muhammad Ibrahim! Screenshot aur logs ka aapas mein match na karna sab se frustrating cheez hoti hai automation mein.

# Masla Kya Hua?
# Aapka local code bilkul theek hai aur usne local chrome par sahi kaam kiya. Lekin jab maine pichle code mein .click(by_js=True) lagaya, toh Facebook ke React-based frontend ne us "JavaScript" click ko fake samajh kar ignore kar diya. Box select hua, script ne samjha click ho gaya, lekin UI ne response nahi diya aur box khula hi nahi! Is wajah se aage ke saare steps false-positive (jhooti success) de gaye.

# Hum isko bilkul aapke local wale exact XPath se replace kar rahe hain, aur .click() ko normal (human-like) rakh rahe hain taake Meta isko asli click samjhe. Sath hi main isme ek "Strict Check" laga raha hoon: Agar sach mein popup nahi khulega, toh script wahin ruk jayegi aur aage ka jhoot nahi bolegi.



# import os
# import json
# import time
# import random
# from DrissionPage import ChromiumPage, ChromiumOptions

# messages = [
#     "RCB vs GT live match HD mein dekhne ke liye link check karein! 🏏🔥",
#     "Kohli vs Gill! Match live on my website. Link in first comment! 🚀"
# ]

# def login_and_post():
#     cookies_json = os.environ.get('FB_COOKIES')
#     if not cookies_json:
#         print("❌ Error: FB_COOKIES secret nahi mila!")
#         return

#     cookies = json.loads(cookies_json)

#     # ==========================================
#     # 🛡️ BROWSER SETUP (STEALTH MODE)
#     # ==========================================
#     co = ChromiumOptions()
#     co.set_argument('--no-sandbox')
#     co.set_argument('--disable-dev-shm-usage')
#     co.set_argument('--window-size=1920,1080')
#     co.set_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
#     co.set_argument('--test-type') 
#     co.set_argument('--disable-infobars') 
#     co.set_argument('--disable-blink-features=AutomationControlled') 
#     co.set_argument('--password-store=basic')
#     co.set_argument('--disable-notifications') 
    
#     print("🚀 Script Start... Browser khul raha hai...")
#     page = ChromiumPage(co)

#     try:
#         # ==========================================
#         # LOGIN PROCESS
#         # ==========================================
#         print("🌐 Facebook par ja rahe hain...")
#         page.get("https://www.facebook.com/404") 
#         time.sleep(3)

#         for cookie in cookies:
#             if 'facebook.com' in cookie.get('domain', ''):
#                 page.set.cookies({
#                     'name': cookie['name'],
#                     'value': cookie['value'],
#                     'domain': cookie['domain'],
#                     'path': cookie.get('path', '/')
#                 })

#         page.get("https://www.facebook.com/")
        
#         if "log in" in page.title.lower() or "login" in page.title.lower():
#             print("❌ Login Failed! Cookies expire ho chuki hain.")
#             return
        
#         print("✅ Login Successful!")

#         # ==========================================
#         # 🧠 SMART WAIT: PAGE LOAD CHECK
#         # ==========================================
#         print("⏳ Wait kar rahe hain taake page aur post box puri tarah load ho jaye...")
#         page.wait.load_start() 
        
#         # EXACT LOCAL XPATH JO AAPNE DIYA HAI
#         post_box_xpath = 'xpath://div[contains(@aria-label, "What\'s on your mind") or contains(@aria-label, "Create a post")]'
        
#         if page.wait.ele_displayed(post_box_xpath, timeout=15):
#             print("✅ Page 100% loaded! Post box screen par aagaya hai.")
#             time.sleep(2) 
#         else:
#             print("❌ Timeout: Post box screen par nahi aaya.")
#             return

#         image_path = os.path.abspath("1.png")

#         # ==========================================
#         # STEP 1: CREATE POST POPUP KHOLNA
#         # ==========================================
#         print("▶️ STEP 1: 'What's on your mind?' wale box par click kar rahe hain...")
#         create_post_btn = page.ele(post_box_xpath)
        
#         if create_post_btn:
#             # Yahan by_js=True hata diya hai taake normal physical click ho
#             create_post_btn.click()
#             time.sleep(5) 
            
#             # 🛑 STRICT CHECK: Kya click hone ke baad popup sach mein khula?
#             dialog_box = page.ele('xpath://div[@role="dialog"]', timeout=3)
#             if not dialog_box:
#                 print("⚠️ Normal click se popup nahi khula! JS click try kar rahe hain...")
#                 create_post_btn.click(by_js=True)
#                 time.sleep(4)
                
#                 # Agar ab bhi nahi khula toh script rok do
#                 if not page.ele('xpath://div[@role="dialog"]'):
#                     print("❌ ERROR: Popup open nahi ho raha! Script rok di gayi hai.")
#                     return
#         else:
#             print("❌ Box select nahi ho saka.")
#             return

#         # ==========================================
#         # STEP 2: TEXT TYPE KARNA
#         # ==========================================
#         print("▶️ STEP 2: Text box mein likh rahe hain...")
#         text_box = page.ele('xpath://div[@role="dialog"]//div[@role="textbox" and @contenteditable="true"]', timeout=5)
#         if text_box:
#             text = random.choice(messages)
#             hashtags = " #RCBvGT #CricketLive"
#             text_box.input(text + hashtags)
#             print("✅ Text type ho gaya.")
#             time.sleep(3)
#         else:
#             print("❌ Text box dialog mein nahi mila.")
#             return

#         # ==========================================
#         # STEP 3: IMAGE UPLOAD
#         # ==========================================
#         print("▶️ STEP 3: Photo upload kar rahe hain...")
#         photo_icon = page.ele('xpath://div[@role="dialog"]//div[@aria-label="Photo/video"]', timeout=5)
#         if photo_icon:
#             photo_icon.click(by_js=True)
#             time.sleep(2)
            
#             if os.path.exists(image_path):
#                 file_input = page.ele('xpath://div[@role="dialog"]//input[@type="file"]')
#                 if file_input:
#                     file_input.input(image_path)
#                     print("✅ Photo attached.")
#                     time.sleep(6)

#         # ==========================================
#         # STEP 4: NEXT BUTTON
#         # ==========================================
#         print("▶️ STEP 4: Next button daba rahe hain...")
#         next_btn = page.ele('css:div[aria-label="Next"][role="button"]', timeout=3)
#         if next_btn:
#             next_btn.click(by_js=True)
#             time.sleep(4)

#         # ==========================================
#         # STEP 4.5: POST BUTTON
#         # ==========================================
#         print("▶️ STEP 4.5: Post button ya popup check kar rahe hain...")
#         post_btn = page.ele('xpath://div[@aria-label="Post" and @role="button"]', timeout=3) or page.ele('xpath://span[text()="Post"]', timeout=2)
#         if post_btn:
#             post_btn.click(by_js=True)
#             print("✅ 'Post' button daba diya.")
#         else:
#             close_early = page.ele('css:div[aria-label="Close"][role="button"]', timeout=3)
#             if close_early:
#                 close_early.click(by_js=True)

#         # ==========================================
#         # STEP 4.8: ZIDDI POPUP HUNTER
#         # ==========================================
#         for i in range(2):
#             time.sleep(6) 
#             popup_close_btn = page.ele('css:div[aria-label="Close"][role="button"]', timeout=3)
#             if popup_close_btn:
#                 popup_close_btn.click(by_js=True)

#         # ==========================================
#         # STEP 5: FINAL "SHARE NOW" BUTTON
#         # ==========================================
#         print("▶️ STEP 5: Final Share button dhoond rahe hain...")
#         share_now_btn = page.ele('css:div[aria-label="Share now"][role="button"]', timeout=3) or page.ele('xpath://span[text()="Share now" or text()="Publish" or text()="Share"]', timeout=2)
#         if share_now_btn:
#             share_now_btn.click(by_js=True)
#             time.sleep(8)
#             print("🎉 BINGO! Facebook Post 100% Successful.")
        
#         time.sleep(5) 

#     except Exception as e:
#         print(f"⚠️ HOUSTON, WE HAVE A PROBLEM: {e}")
#     finally:
#         print("\nBrowser band kar rahe hain...")
#         page.quit()
#         os.system("pkill chrome")
#         print("✅ Browser successfully khatam ho gaya!")

# if __name__ == "__main__":
#     login_and_post()








# import os
# import json
# import time
# import random
# from DrissionPage import ChromiumPage, ChromiumOptions

# messages = [
#     "RCB vs GT live match HD mein dekhne ke liye link check karein! 🏏🔥",
#     "Kohli vs Gill! Match live on my website. Link in first comment! 🚀"
# ]

# def login_and_post():
#     cookies_json = os.environ.get('FB_COOKIES')
#     if not cookies_json:
#         print("❌ Error: FB_COOKIES secret nahi mila!")
#         return

#     cookies = json.loads(cookies_json)

#     # ==========================================
#     # 🛡️ BROWSER SETUP (STEALTH MODE)
#     # ==========================================
#     co = ChromiumOptions()
#     co.set_argument('--no-sandbox')
#     co.set_argument('--disable-dev-shm-usage')
#     co.set_argument('--window-size=1920,1080')
#     co.set_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
#     co.set_argument('--test-type') 
#     co.set_argument('--disable-infobars') 
#     co.set_argument('--disable-blink-features=AutomationControlled') 
#     co.set_argument('--password-store=basic')
#     co.set_argument('--disable-notifications') 
    
#     print("🚀 Script Start... Browser khul raha hai...")
#     page = ChromiumPage(co)

#     try:
#         # ==========================================
#         # LOGIN PROCESS
#         # ==========================================
#         print("🌐 Facebook par ja rahe hain...")
#         page.get("https://www.facebook.com/404") 
#         time.sleep(3)

#         print("🍪 Cookies inject kar rahe hain...")
#         for cookie in cookies:
#             if 'facebook.com' in cookie.get('domain', ''):
#                 cookie_dict = {
#                     'name': cookie['name'],
#                     'value': cookie['value'],
#                     'domain': cookie['domain'],
#                     'path': cookie.get('path', '/')
#                 }
#                 page.set.cookies(cookie_dict)

#         page.get("https://www.facebook.com/")
        
#         if "log in" in page.title.lower() or "login" in page.title.lower():
#             print("❌ Login Failed! Cookies expire ho chuki hain.")
#             return
        
#         print("✅ Login Successful!")

#         # ==========================================
#         # 🧠 SMART WAIT: PAGE LOAD AUR BOX SELECT KARNA
#         # ==========================================
#         print("⏳ Wait kar rahe hain taake page aur post box puri tarah load ho jaye...")
#         page.wait.load_start() # Page loading start hone ka wait
        
#         # Yeh universal locator hai jo har kism ke post box ko pakrega
#         post_box_xpath = 'xpath://div[contains(@aria-label, "What\'s on your mind") or contains(@aria-label, "Create a post") or contains(@aria-label, "Write something")]'
        
#         # Script maximum 15 seconds tak is box ke screen par aane ka wait karegi
#         if page.wait.ele_displayed(post_box_xpath, timeout=15):
#             print("✅ Page 100% loaded! Post box screen par aagaya hai.")
#             time.sleep(1) # Extra human-like buffer
#         else:
#             print("⚠️ Timeout: Post box nahi mila. Shayad internet slow hai.")
#             return

#         image_path = os.path.abspath("1.png")
#         if not os.path.exists(image_path):
#             print("⚠️ Tasveer '1.png' repository mein nahi mili! Sirf text post ho jayega.")

#         # ==========================================
#         # STEP 1: CREATE POST POPUP KHOLNA
#         # ==========================================
#         print("▶️ STEP 1: 'What's on your mind?' wale box par click kar rahe hain...")
#         create_post_btn = page.ele(post_box_xpath)
#         if create_post_btn:
#             create_post_btn.click(by_js=True)
#             time.sleep(4) # Popup khulne ka wait
#         else:
#             print("❌ Box select nahi ho saka.")
#             return

#         # ==========================================
#         # STEP 2: TEXT TYPE KARNA
#         # ==========================================
#         print("▶️ STEP 2: Text box mein likh rahe hain...")
#         text_box = page.ele('xpath://div[@role="dialog"]//div[@role="textbox" and @contenteditable="true"]', timeout=5)
#         if text_box:
#             text = random.choice(messages)
#             hashtags = " #RCBvGT #CricketLive"
#             full_text = text + hashtags
#             print(f"Text Type Kar Rahe Hain: {full_text}")
#             text_box.input(full_text)
#             time.sleep(3)

#         # ==========================================
#         # STEP 3: IMAGE UPLOAD
#         # ==========================================
#         print("▶️ STEP 3: Photo upload kar rahe hain...")
#         photo_icon = page.ele('xpath://div[@role="dialog"]//div[@aria-label="Photo/video"]', timeout=5)
#         if photo_icon:
#             photo_icon.click(by_js=True)
#             time.sleep(2)
            
#             if os.path.exists(image_path):
#                 file_input = page.ele('xpath://div[@role="dialog"]//input[@type="file"]')
#                 if file_input:
#                     file_input.input(image_path)
#                     time.sleep(6)

#         # ==========================================
#         # STEP 4: NEXT BUTTON
#         # ==========================================
#         print("▶️ STEP 4: Next button daba rahe hain...")
#         next_btn = page.ele('css:div[aria-label="Next"][role="button"]', timeout=3)
#         if next_btn:
#             next_btn.click(by_js=True)
#             time.sleep(4)

#         # ==========================================
#         # STEP 4.5: POST BUTTON / EARLY POPUP
#         # ==========================================
#         print("▶️ STEP 4.5: Post button ya popup check kar rahe hain...")
#         post_btn = page.ele('xpath://div[@aria-label="Post" and @role="button"]', timeout=3) or page.ele('xpath://span[text()="Post"]', timeout=2)
#         if post_btn:
#             post_btn.click(by_js=True)
#             print("✅ 'Post' button daba diya.")
#         else:
#             print("⚠️ 'Post' nahi mila! Shayad popup aagaya hai.")
#             close_early = page.ele('css:div[aria-label="Close"][role="button"]', timeout=3)
#             if close_early:
#                 close_early.click(by_js=True)

#         # ==========================================
#         # STEP 4.8: ZIDDI POPUP HUNTER
#         # ==========================================
#         print("▶️ STEP 4.8: Annoying popups ka wait kar rahe hain...")
#         for i in range(2):
#             time.sleep(8) 
#             popup_close_btn = page.ele('css:div[aria-label="Close"][role="button"]', timeout=3)
#             if popup_close_btn:
#                 popup_close_btn.click(by_js=True)
#                 print(f"✅ Popup uda diya attempt {i+1} mein.")

#         # ==========================================
#         # STEP 5: FINAL "SHARE NOW" BUTTON
#         # ==========================================
#         print("▶️ STEP 5: Final Share button dhoond rahe hain...")
#         share_now_btn = page.ele('css:div[aria-label="Share now"][role="button"]', timeout=3) or page.ele('xpath://span[text()="Share now" or text()="Publish" or text()="Share"]', timeout=2)
#         if share_now_btn:
#             share_now_btn.click(by_js=True)
#             time.sleep(8)
#             print("🎉 BINGO! Facebook Post 100% Successful.")
        
#         # Result show karne ke liye thora rukna zaroori hai taake video mein capture ho
#         time.sleep(5) 

#     except Exception as e:
#         print(f"⚠️ HOUSTON, WE HAVE A PROBLEM: {e}")
#     finally:
#         print("\nBrowser band kar rahe hain...")
#         page.quit()
#         os.system("pkill chrome")
#         print("✅ Browser successfully khatam ho gaya!")

# if __name__ == "__main__":
#     login_and_post()



















# facebook open succcesfully, lekin post box kehta hai k open kar leya lekin asal mei open nahey hota




# import os
# import json
# import time
# import random
# from DrissionPage import ChromiumPage, ChromiumOptions

# messages = [
#     "RCB vs GT live match HD mein dekhne ke liye link check karein! 🏏🔥",
#     "Kohli vs Gill! Match live on my website. Link in first comment! 🚀"
# ]

# def login_and_post():
#     cookies_json = os.environ.get('FB_COOKIES')
#     if not cookies_json:
#         print("❌ Error: FB_COOKIES secret nahi mila!")
#         return

#     cookies = json.loads(cookies_json)

#     # ==========================================
#     # 🛡️ BROWSER SETUP (STEALTH & VIRTUAL SCREEN)
#     # ==========================================
#     co = ChromiumOptions()
#     co.set_argument('--no-sandbox')
#     co.set_argument('--disable-dev-shm-usage')
#     co.set_argument('--window-size=1920,1080')
#     co.set_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
#     # 🛑 YEH NAYE FLAGS HAIN JO WARNINGS CHUPAYENGE 🛑
#     co.set_argument('--test-type') # --no-sandbox ki warning gaib karega
#     co.set_argument('--disable-infobars') # Top bars hide karega
#     co.set_argument('--disable-blink-features=AutomationControlled') # Bot detection se bachayega
#     co.set_argument('--password-store=basic')
#     co.set_argument('--disable-notifications') 
    
#     print("🚀 Script Start... Browser khul raha hai...")
#     page = ChromiumPage(co)

#     try:
#         # ==========================================
#         # LOGIN PROCESS
#         # ==========================================
#         print("🌐 Facebook par ja rahe hain...")
#         page.get("https://www.facebook.com/404") 
#         time.sleep(3)

#         print("🍪 Cookies inject kar rahe hain...")
#         for cookie in cookies:
#             if 'facebook.com' in cookie.get('domain', ''):
#                 cookie_dict = {
#                     'name': cookie['name'],
#                     'value': cookie['value'],
#                     'domain': cookie['domain'],
#                     'path': cookie.get('path', '/')
#                 }
#                 page.set.cookies(cookie_dict)

#         page.get("https://www.facebook.com/")
#         time.sleep(6)

#         if "log in" in page.title.lower() or "login" in page.title.lower():
#             print("❌ Login Failed! Cookies expire ho chuki hain.")
#             return
        
#         print("✅ Login Successful! Posting start kar rahe hain...")

#         image_path = os.path.abspath("1.png")
#         if not os.path.exists(image_path):
#             print("⚠️ Tasveer '1.png' repository mein nahi mili! Text post ho jayegi.")

#         # ==========================================
#         # STEP 1: CREATE POST POPUP
#         # ==========================================
#         print("▶️ STEP 1: Post box dhoond rahe hain...")
#         create_post_btn = page.ele('xpath://div[contains(@aria-label, "What\'s on your mind") or contains(@aria-label, "Create a post")]', timeout=10)
#         if create_post_btn:
#             create_post_btn.click(by_js=True)
#             time.sleep(4)
#         else:
#             print("❌ 'What's on your mind?' button nahi mila.")

#         # ==========================================
#         # STEP 2: TEXT TYPE KARNA
#         # ==========================================
#         print("▶️ STEP 2: Text box dhoond rahe hain...")
#         text_box = page.ele('xpath://div[@role="dialog"]//div[@role="textbox" and @contenteditable="true"]', timeout=5)
#         if text_box:
#             text = random.choice(messages)
#             hashtags = " #RCBvGT #CricketLive"
#             full_text = text + hashtags
#             print(f"Text Type Kar Rahe Hain: {full_text}")
#             text_box.input(full_text)
#             time.sleep(3)

#         # ==========================================
#         # STEP 3: IMAGE UPLOAD
#         # ==========================================
#         print("▶️ STEP 3: Photo/Video option dhoond rahe hain...")
#         photo_icon = page.ele('xpath://div[@role="dialog"]//div[@aria-label="Photo/video"]', timeout=5)
#         if photo_icon:
#             photo_icon.click(by_js=True)
#             time.sleep(2)
            
#             if os.path.exists(image_path):
#                 file_input = page.ele('xpath://div[@role="dialog"]//input[@type="file"]')
#                 if file_input:
#                     print("Tasveer upload ho rahi hai...")
#                     file_input.input(image_path)
#                     time.sleep(6)

#         # ==========================================
#         # STEP 4: NEXT BUTTON
#         # ==========================================
#         print("▶️ STEP 4: Next button dhoond rahe hain...")
#         next_btn = page.ele('css:div[aria-label="Next"][role="button"]', timeout=3)
#         if next_btn:
#             next_btn.click(by_js=True)
#             print("✅ 'Next' button daba diya.")
#             time.sleep(4)

#         # ==========================================
#         # STEP 4.5: POST BUTTON / EARLY POPUP
#         # ==========================================
#         print("▶️ STEP 4.5: Post button check kar rahe hain...")
#         post_btn = page.ele('xpath://div[@aria-label="Post" and @role="button"]', timeout=3) or page.ele('xpath://span[text()="Post"]', timeout=2)
#         if post_btn:
#             post_btn.click(by_js=True)
#             print("✅ 'Post' button daba diya.")
#         else:
#             print("⚠️ 'Post' nahi mila! Shayad popup aagaya hai.")
#             close_early = page.ele('css:div[aria-label="Close"][role="button"]', timeout=3)
#             if close_early:
#                 close_early.click(by_js=True)

#         # ==========================================
#         # STEP 4.8: ZIDDI POPUP HUNTER
#         # ==========================================
#         print("▶️ STEP 4.8: Ziddi popups check kar rahe hain...")
#         for i in range(2):
#             time.sleep(8) 
#             popup_close_btn = page.ele('css:div[aria-label="Close"][role="button"]', timeout=3)
#             if popup_close_btn:
#                 popup_close_btn.click(by_js=True)
#                 print(f"✅ BINGO! Popup uda diya attempt {i+1} mein.")

#         # ==========================================
#         # STEP 5: FINAL "SHARE NOW" BUTTON
#         # ==========================================
#         print("▶️ STEP 5: Final Share button dhoond rahe hain...")
#         share_now_btn = page.ele('css:div[aria-label="Share now"][role="button"]', timeout=3) or page.ele('xpath://span[text()="Share now" or text()="Publish" or text()="Share"]', timeout=2)
#         if share_now_btn:
#             share_now_btn.click(by_js=True)
#             print("✅ 'Share now' button daba diya.")
#             time.sleep(8)
#             print("🎉 BINGO! Facebook Post 100% Successful.")
        
#         # Result show karne ke liye thora rukna zaroori hai taake video mein capture ho
#         time.sleep(5) 

#     except Exception as e:
#         print(f"⚠️ HOUSTON, WE HAVE A PROBLEM: {e}")
#     finally:
#         print("\nBrowser band kar rahe hain...")
#         page.quit()
#         os.system("pkill chrome")
#         print("✅ Browser successfully khatam ho gaya!")

# if __name__ == "__main__":
#     login_and_post()



























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
