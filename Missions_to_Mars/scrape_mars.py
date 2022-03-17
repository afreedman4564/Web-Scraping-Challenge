from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

from pprint import pprint
import pandas as pd
import datetime as dt

def scrape_all():

    # setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # return JSON data to load into mongodb
    headline, paragraph = scrape_news(browser)

    # build a dictionary using the scrapes
    mars_data = {
        "news_title": headline,
        "news_paragraph": paragraph,
        "featured_image": scrape_image(browser),
        "mars_facts": scrape_mars_facts(browser),
        "full_image_dict": scrape_hemispheres(browser),
        "as_of_date": dt.datetime.now()
    }


    # stop the browser
    browser.quit()

    # show data
    return mars_data

# scrape news page
def scrape_news(browser):

    url = "https://redplanetscience.com/"
    browser.visit(url)

    # time.sleep(5)
    
    # convert to soup object that can be parsed
    html = browser.html
    soup = bs(html,'html.parser')

    results_headline = soup.find_all('div', "content_title")
    number = len(results_headline)

    articles = []

    for article in range(number):
        headline = soup.find_all('div', "content_title")[article].get_text()
        paragraph = soup.find_all('div', "article_teaser_body")[article].get_text()
        date = soup.find_all('div', "list_date")[article].get_text()
        articles.append({"headline": headline, "paragraph": paragraph, "date": date})


    # convert dictionary into df
    latest_article_df = pd.DataFrame(articles)

    # convert date into datetime data element to enable sorting
    latest_article_df["date"] = latest_article_df["date"].astype(str)
    latest_article_df["date"] = pd.to_datetime(latest_article_df["date"]).dt.date
    latest_article_df.sort_values(by="date", inplace=True, ascending = False)

    # pull 1st value for 1st record and assign to variables that can be leveraged later
    most_recent_headline = latest_article_df.iloc[0, 0]
    most_recent_paragraph = latest_article_df.iloc[0, 1]
    
    return most_recent_headline, most_recent_paragraph

def scrape_image(browser):

    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    # capture the complete url string for this image featured
    image_path = browser.find_by_tag('button')[1]
    image_path.click()

    html = browser.html
    soup_image = bs(html,'html.parser')

    image_url_path = soup_image.find('img', 'fancybox-image')['src']

    image_url = url + image_url_path
    
    return image_url


def scrape_mars_facts(browser):

    url = "https://galaxyfacts-mars.com"
    browser.visit(url)

    html = browser.html
    soup_facts = bs(html,'html.parser')

    facts_section = soup_facts.find("div", "diagram mt-4")
    facts_table = facts_section.find("table")

    facts = ''
    
    facts += str(facts_table)

    return facts

def scrape_hemispheres(browser):
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit https://marshemispheres.com
    url = "https://marshemispheres.com/"
    browser.visit(url)

    time.sleep(5)

    html = browser.html
    hemisphere_soup = bs(html,'html.parser')

    results_links = hemisphere_soup.find_all('div', 'item')
    # pprint(results_links)
    image_list = []

    for result in results_links:
        image_link = ''
        url = "https://marshemispheres.com/"
        title=''
        title = result.find('h3').text
        image_link = result.find('a', class_="itemLink product-item")["href"]
        image_name = image_link.replace(".html", "")
        url = url + image_link
        image_list.append(url)

    full_image_dict = []
        
    for link in image_list:
        url = "https://marshemispheres.com/"
        browser.visit(link)
        hemisphere_html = browser.html
        hemisphere_soup = bs(hemisphere_html, "html.parser")
        title = hemisphere_soup.find('div', 'cover').find('h2', 'title').text
        full_image_link = hemisphere_soup.find('img', 'wide-image')['src']
        url = url + full_image_link
        full_image_dict.append({"title": title, "full_image_url": url})

    return full_image_dict


if __name__ == "__main__":
    print(scrape_all())

