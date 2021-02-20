import random
import instaloader
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




cekilis = input("Lütfen Çekiliş postunun linkini yapıştırın: ")
kullanici_adi = input("Lütfen İnstagram kullanıcı adınızı giriniz: ")
sifre = input("Lütfen İnstagram Şifrenizi Yazınız: ")

driver = webdriver.Chrome("/Chrome/driver/Path")
driver.get('https://www.instagram.com/')
time.sleep(1.2)
driver.find_element_by_name("username").send_keys(kullanici_adi)
driver.find_element_by_name("password").send_keys(sifre)
driver.find_element_by_xpath("//button [contains(.,'Giriş Yap')]").click()
time.sleep(5)
driver.find_element_by_xpath("//button [contains(.,'Bilgileri Kaydet')]").click()
time.sleep(4)
driver.find_element_by_xpath("//button [contains(.,'Şimdi Değil')]").click()
time.sleep(2)

driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND+'t')
driver.get(cekilis)
try:
    daha_fazla_yorum= driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
    while daha_fazla_yorum.is_displayed():
        daha_fazla_yorum.click()
        time.sleep(1)
        daha_fazla_yorum= driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
except Exception as e:
    pass

kullanici_adlari = []
kullanici_yorumlari = []

comment = driver.find_elements_by_class_name('gElp9')
for c in comment:
    cerceve = c.find_element_by_class_name('C4VMK')
    ad = cerceve.find_element_by_class_name('_6lAjh').text
    yorum = cerceve.find_element_by_tag_name('span').text
    yorum = yorum.replace('\n','').strip().rstrip()
    kullanici_adlari.append(ad)
    kullanici_yorumlari.append(yorum)

kullanici_adlari.pop(0)
kullanici_yorumlari.pop(0)
a=0
# takipci kontrol
L = instaloader.Instaloader()
L.login(kullanici_adi,sifre)

profil = instaloader.Profile.from_username(L.context,"PageUserName")
post = instaloader.Post.from_shortcode(L.context,'/p/justPasteThisShortCodeWithout"/p/"')

post_likes = post.get_likes()
follower = []
liker =[]
for likee in post_likes:
    liker.append(likee.username)


for i in profil.get_followers():
    follower.append(i.username)


for x in kullanici_adlari:
    if(x in follower):
        pass
    else:
        kullanici_adlari.remove(x)



for j in kullanici_adlari:
    if(j in liker):
        pass
    else:
        kullanici_adlari.remove(j)


asil = kullanici_adlari[random.choice(range(0,len(kullanici_adlari)))]
for e in kullanici_adlari:
    if(asil == e):
        kullanici_adlari.remove(e)
    else:
        pass

asil2 = kullanici_adlari[random.choice(range(0,len(kullanici_adlari)))]
for e2 in kullanici_adlari:
    if(asil2 == e2):
        kullanici_adlari.remove(e2)
    else:
        pass
asil3 = kullanici_adlari[random.choice(range(0,len(kullanici_adlari)))]
for e3 in kullanici_adlari:
    if(asil3 == e3):
        kullanici_adlari.remove(e3)
    else:
        pass
asil4 = kullanici_adlari[random.choice(range(0,len(kullanici_adlari)))]
for e4 in kullanici_adlari:
    if(asil4 == e4):
        kullanici_adlari.remove(e4)
    else:
        pass
asil5 = kullanici_adlari[random.choice(range(0,len(kullanici_adlari)))]
for e5 in kullanici_adlari:
    if(asil5 == e5):
        kullanici_adlari.remove(e5)
    else:
        pass
asil6 = kullanici_adlari[random.choice(range(0,len(kullanici_adlari)))]
for e6 in kullanici_adlari:
    if(asil6 == e6):
        kullanici_adlari.remove(e6)
    else:
        pass


print("Asil Kazanan: {}\nYedek Kazanan:{}\nAsil 2.Kazanan: {}\nYedek 2.Kazanan: {}\nAsil 3.Kazanan: {}\nYedek 3.Kazanan: {}".format(asil,asil2,asil3,asil4,asil5,asil6))
driver.close()

