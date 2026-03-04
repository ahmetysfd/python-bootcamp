from bs4 import BeautifulSoup
import requests
import smtplib


url = ("https://www.amazon.pl/Marshall-Emberton-1006234-Glo%C5%9Bnik-Bluetooth/dp/B09XXW54QG/"
       "ref=pd_day0fbt_thbs_d_sccl_2/260-4921051-4986414?pd_rd_w=SpvJA&content-id=amzn1.sym.39b0074d-e537-4ca2-8058-"
       "57721612ac6e&pf_rd_p=39b0074d-e537-4ca2-8058-57721612ac6e&pf_rd_r=C77ER1P8G8GFAG67Z913&pd_rd_wg=1OQgf&pd_rd_r="
       "a23f6323-9a36-4a29-8429-d41f8df15c20&pd_rd_i=B09XXW54QG&th=1")

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(name="span", class_="a-price-whole")
item_name = soup.find(name="span", class_="a-size-large product-title-word-break")
price_text = price.getText()
clean_price = price_text.replace(",", "").strip()
price_float = float(clean_price)



item_name_string = item_name.getText()
item_name_string = item_name_string.encode("utf-8")


target_price = 300

my_email = "saddad0618@gmail.com"
password = "foqs qgdz fcjd mvul"

if price_float < target_price:

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=item_name_string
        )

