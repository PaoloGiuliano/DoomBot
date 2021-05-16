import time
from time import sleep
import json
import discord
from discord.ext import commands
from facebook_page_scraper import Facebook_scraper
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


image = ""
message = ""
video = ""
client = commands.Bot(command_prefix = '.')

page_name = "HeroicExpedition"
posts_count = 2
browser = "firefox"

@client.command()
async def fb(ctx):
    await ctx.send("============Facebook Post============")
    facebook_ai = Facebook_scraper(page_name,posts_count,browser)
    json_data = facebook_ai.scrap_to_json()
    loads = json.loads(json_data)
    for k in loads:
        video = loads[k]['video']
        message = loads[k]['content']
        image = loads[k]['image']
    await ctx.send(message)
    for img in image:
        await ctx.send(img)
    if video != "":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        url = "https://www.getfvid.com/"
        keys = video
        driver.get(url)

        videoInput = driver.find_element_by_name('url')
        videoInput.send_keys(keys)

        download = driver.find_element_by_id('btn_submit')
        download.click()

        count = 1
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        VIDEO = ""
        for vid in soup.find_all('a'):
            try:
                VIDEO = str(vid.get('href'))
            except TypeError:
                print('found nothing')
            else:
                if "scontent" in VIDEO:
                    if count == 1:
                        count += 1
                        await ctx.send(VIDEO)
        
        
    
    
    
client.run('ODQyMTMzODg2MzgxMzI2MzY3.YJw4TA.ZoJRd-Y0OCvDgtaKN2Cs2eiL9z0')
