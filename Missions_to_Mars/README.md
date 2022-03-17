# Web Scraping Homework - Mission to Mars

Scrape a series of webpages to gather details and images regarding Mars

### NASA Mars News

- Scrape the webpage https://redplanetscience.com/ to collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
- Setup Splinter to allow browser visitation
- Use sleep function to allow page time to load
- Use html parser to scrape through page to gather headlines, date of headline and paragraph
- Use pandas to sort values by headline date, choosing the most recent and save variables

### Scrape through Mars Space Images to grab the Featured Image

- Scrape the webpage https://spaceimages-mars.com to collect the featured image
- Setup Splinter to allow browser visitation
- Use sleep function to allow page time to grab href for image
- Use button and click function to image page
- Leverage html parser to grab the image path and append to the url for the full url
- Save as variable to reference later

### Mars Facts

- Scrape the webpage https://galaxyfacts-mars.com to collect mars statistics
- Use Pandas to scrape
- Create list using read_html and transform to dataframe

*Approach changes when transitioning to VS Code
- Use similar steps noted above to scrape through featured image and latest headline


### Mars Hemispheres

- Scrape the webpage https://marshemispheres.com to collect mars hemisphere images and titles
- Setup Splinter to allow browser visitation
- Use sleep function to allow page time to grab href for each hemisphere to get to the full image
- Leverage html parser to grab the image path and append to the url for the full url
- Use Splinter to parse through each page found with the image path and gather the full image url
- Save title and full image url as variables to reference later


## Step 2 - MongoDB and Flask Application

- Use MongoDB with Flask to create a page, showcasing the information and images scraped from prior pages
- Convert all script from Jupyter Notebook to VS Code
- Create series of functions for each scraping effort, returning all data elements in form of dictionary
- Combine all data elements into one dictionary in a summarizing scrape function
- Use Flask to connect dictionary created and render onto webpage
- Create index.html, saving to Templates folder
- Introduce formatting to display information and images collected