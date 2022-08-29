#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[2]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[3]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[4]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[5]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[6]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[7]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[8]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[9]:


df.to_html()


# # Hemispheres

# In[ ]:


url = 'https://marshemispheres.com/'
browser.visit(url)
browser.is_element_present_by_css('div.list_text', wait_time=1)
    
# Empty list to contain urls
hemisphere_image_urls = []

full_image_elem = browser.find_by_tag('h3')

for hemi in range(0,4):
    full_image_elem = browser.find_by_tag('h3')[hemi]
    full_image_elem.click()
    html = browser.html
        
        # Find the relative image url
    img_soup = soup(html, 'html.parser')
    img_url_rel = img_soup.find('img', class_='wide-image').get('src')
        
        # Use the base URL to create an absolute URL
    image_url = f'{url}+{img_url_rel}'
    
    title_txt = browser.find_by_tag('h2').value
    
    hemisphere = {'img_url': image_url, 'title': title_txt}
    hemisphere_image_urls.append(hemisphere)
    
    time.sleep(2)

    browser.back()
# hemispheres = zip(hemisphere_image_urls,hemisphere_titles)
# hemispheres = list(zip(hemisphere_titles, hemisphere_image_urls))


# In[12]:


# 4. Print the list that holds the dictionary of each image url and title.
# for x in range(len(hemi_titles)):
#     print(hemi_titles[x])

hemisphere_image_urls

# hemi_titles


# In[ ]:


# 5. Quit the browser
browser.quit()


# In[ ]:




