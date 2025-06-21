from bs4 import BeautifulSoup
import requests
import pprint
import smtplib


URL = "https://www.amazon.in/dp/B0CQRQLJSR/ref=sspa_dk_detail_4?psc=1&pf_rd_p=67d3dec9-3503-44a1-a945-e969d04cca69&pf_rd_r=6SHTP9F1HED7NVGX5JX5&pd_rd_wg=VZsTV&pd_rd_w=c5Jxi&content-id=amzn1.sym.67d3dec9-3503-44a1-a945-e969d04cca69&pd_rd_r=fe256561-c1b9-405d-8487-bcf51ce4bfaa&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM"


headers= {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en-IN;q=0.9,en;q=0.8",
"Priority": "u=0, i",
"Sec-Ch-Ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Ch-Ua-Platform": '"Windows"',
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}
response = requests.get(url=URL , headers=headers)
response.raise_for_status()

soup = BeautifulSoup(markup=response.text,features="lxml")
price = str(soup.find(name="span",class_="a-price-whole").getText())
price=price.replace(",","")
print(price)
price= int(price)
print(type(price))

# Sending mail -----
    
my_mail= "siddiqui.maaz79@gmail.com"
mail_password ="gaaf bbkc haut xheb"
message = f"Subject: Assalamualaikum\n\nTIMEX Stainless Steel Men Green Round Automatic Dial Analog Watch- Tweg23502 now at ${price} https://www.amazon.in/dp/B0CQRQLJSR/ref=sspa_dk_detail_4?psc=1&pf_rd_p=67d3dec9-3503-44a1-a945-e969d04cca69&pf_rd_r=6SHTP9F1HED7NVGX5JX5&pd_rd_wg=VZsTV&pd_rd_w=c5Jxi&content-id=amzn1.sym.67d3dec9-3503-44a1-a945-e969d04cca69&pd_rd_r=fe256561-c1b9-405d-8487-bcf51ce4bfaa&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM"

to_mail = "maaz.irshad.siddiqui@gmail.com"

if price <=3599:
    with smtplib.SMTP_SSL("smtp.gmail.com",port=465) as connection:
        connection.login(user=my_mail,password=mail_password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=to_mail,
            msg=message) 
else:
    print("TO COSTLY")
    message = f"Subject: Assalamualaikum\n\nTO COSTLY\nPrice:{price}\n\nURL: https://www.amazon.in/dp/B0CQRQLJSR/ref=sspa_dk_detail_4?psc=1&pf_rd_p=67d3dec9-3503-44a1-a945-e969d04cca69&pf_rd_r=6SHTP9F1HED7NVGX5JX5&pd_rd_wg=VZsTV&pd_rd_w=c5Jxi&content-id=amzn1.sym.67d3dec9-3503-44a1-a945-e969d04cca69&pd_rd_r=fe256561-c1b9-405d-8487-bcf51ce4bfaa&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM"
    with smtplib.SMTP_SSL("smtp.gmail.com",port=465) as connection:
        connection.login(user=my_mail,password=mail_password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=to_mail,
            msg=message) 
