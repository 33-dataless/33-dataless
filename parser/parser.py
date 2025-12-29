
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def return_readme(readme_data: list) -> str:
    return f"""
<div align="center"><img src="source\lelouch.gif" alt="gif not loaded" width="500" height="100"></div>

<h1 align="center"> Roman Nervousness | 33-dataless </h1>
<h3 align="center"> 17yo software developer, future data science ml engineer <h3>

<div align="center">[![My Skills](https://skillicons.dev/icons?i=python,rust,java,postgres,)](https://skillicons.dev)</div>
<div align="center">[![My Skills](https://skillicons.dev/icons?i=redis,docker,git,linux,)](https://skillicons.dev)</div>

<h1 align="center">my best hero in dota 2</h1>

<table border="1" width="100%" align="center">
  <tr align="center">
    <td><div align="center"><img src="source\Beastmaster_minimap_icon.webp" width="55"></td>
    <td><div align="center"><img src="source\Lone_Druid_minimap_icon.webp " width="55"></td>
    <td><div align="center"><img src="source\Doom_minimap_icon.webp       " width="55"></td>
  </tr>
  <tr align="center">
    <td>winrate: <div style="color: green">{readme_data[0][2]}</div></td>
    <td>winrate: <div style="color: green">{readme_data[1][2]}</div></td>
    <td>winrate: <div style="color: green">{readme_data[2][2]}</div></td>
  </tr>
  <tr align="center">
    <td>matches: <div style="color: yellow">{readme_data[0][1]}</div></td>
    <td>matches: <div style="color: yellow">{readme_data[1][1]}</div></td>
    <td>matches: <div style="color: yellow">{readme_data[2][1]}</div></td>
  </tr>
</table>

### other skils 
- html/css
- aiogram 
- parsing ( bs4, немного selenium )
- little english ( can read documentation )

### my project
- telegram bot, anonymous message ( full clone famous bot )
- parsing data using hidden API ( d2pt parsing )
"""
    

def get_data_by_hero_name(hero_name: str, soup: BeautifulSoup) -> list:
    hero = hero_name
    amount_match = None
    winrate = None

    tr = soup.select_one(f'td.cell-icon[data-value="{hero_name}"]').find_parent('tr')
    amount_match = tr.select_one('div.segment.segment-match').find_parent('td').contents[0].strip()
    winrate = tr.select_one('div.segment.segment-win').find_parent('td').contents[0].strip()

    return [hero, amount_match, winrate]

def build_readme() -> None:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.binary_location = r"C:\Users\roman\AppData\Local\Mozilla Firefox\firefox.exe"
    options.set_preference(
        "general.useragent.override", 
        "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/120.0"
    )

    service = Service(r"D:\geckodriver\geckodriver.exe")

    driver = webdriver.Firefox(service=service, options=options)
    
    try:
        driver.get("https://ru.dotabuff.com/players/1485404803/heroes")
        time.sleep(5)
        element = driver.find_element(By.CLASS_NAME, "sortable")

        with open(r'parser\answer.html', 'w', encoding="utf-8") as file:
            file.write(str(element.get_attribute("outerHTML")))

        with open(r'parser\answer.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, 'lxml')

            heroes = ['Beastmaster', 'Lone Druid', 'Doom']
            readme_data = []
            for hero in heroes:
                readme_data.append(get_data_by_hero_name(hero, soup=soup))
            else:
                readme = return_readme(readme_data)
        
    finally:
        driver.quit()
        return readme


