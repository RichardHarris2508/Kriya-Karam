import requests, re , colorama
colorama.init()

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

city = input("Enter city name....\t")
city = city.replace(" ", "%20")

try:
    url = f"http://www.insecam.org/en/bycity/{city}/?page=3"

    res = requests.get(url, headers=headers)
    find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
    for ip in find_ip:
        print("\033[1;31m", ip)

except Exception as e:
    print(e)