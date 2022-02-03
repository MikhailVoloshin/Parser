from email.mime import image
from urllib import response
import requests
from bs4 import BeautifulSoup
import fake_useragent

image_number = 0
storage_number = 1
link = f"https://zastavok.net/"

for storage in range(12):
    responce = requests.get(f"{link}/{storage_number}").text
    soup = BeautifulSoup(responce, "lxml")
    block = soup.find("div", class_="block-photo")
    all_image = block.find_all("div", class_="short_full")

    for image in all_image:
        image_link = image.find("a").get("href")
        download_storage = requests.get(f"{link}{image_link}").text
        download_soup = BeautifulSoup(download_storage, "lxml")
        download_block = download_soup.find("div", class_="image_data").find(
            "div", class_="block_down"
        )
        result_link = download_block.find("a").get("href")

        image_bytes = requests.get(f"{link}{result_link}").content

        with open(f"image/{image_number}.jpg", "wb") as file:
            file.write(image_bytes)

        image_number += 1
        print(f"Image {image_number}.jpg sucssesful download")

    storage_number += 1


# session = requests.Session()
# link = "https://lms.ithillel.ua/api/lms/users/login"
# user = fake_useragent.UserAgent().random

# header = {
#     'user-agent': user
# }


# data = {
#     'form_sent': '1',
#     'email':'###',
#     'password':'###'
# }

# responce = session.post(link, data=data, headers=header).text
# profile_info = 'https://lms.ithillel.ua/'
# profile_responce = session.get(profile_info, headers=header).text

# print(profile_responce)


# cookies_dict = [
#     {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
#     for key in session.cookies
# ]

# session2 = requests.Session()

# for cookies in cookies_dict:
#     session2.cookies.set(**cookies)

# resp = session2.get(profile_info, headers=header)
# print(resp.text)


# user = fake_useragent.FakeUserAgent().random
# header = {'user-agent': user}


# link = 'https://browser-info.ru/'
# responce = requests.get(link, headers = header).text
# soup = BeautifulSoup(responce , 'lxml')
# block = soup.find('div', id = 'tool_padding')

# # Check js
# check_js = block.find('div', id = 'javascript_check')
# status_js = check_js.find_all('span')[1].text
# result_js = f'javascript : {status_js}'

# # Check flash
# check_flash = block.find('div', id = 'flash_version')
# status_flash = check_flash.find_all('span')[1].text
# result_flash = f'flash: {status_flash}'

# #Check user_agent
# check_user = block.find('div', id = 'user_agent').text


# print(result_js)
# print(result_flash)
# print(check_user)
