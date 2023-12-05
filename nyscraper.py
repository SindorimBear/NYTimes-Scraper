import requests
import csv
import time
#Manually get Api-Key from the New York Times Developer Portal
api_key = ''#Replace with your own API Key
base_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
#Set Keywords
keywords = ['online'] #Can add multiple keywords
# Date range 2022~2023
begin_date = '20220101'
end_date = '20231127'
# Save file name 
csv_file = 'data.csv'
#Requsting New York Times api for data
def make_api_request(keyword):
    query = keyword
    params = {
        'api-key': api_key,
        'q': query,
        'begin_date': begin_date,
        'end_date': end_date
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        articles = response.json()['response']['docs']
        data = []
        for article in articles:
            url = article['web_url']
            headline = article['headline']['main'] if 'headline' in article and 'main' in article['headline'] else ''
            article_content = article['lead_paragraph'] if 'lead_paragraph' in article else ''
            article_content = article_content.replace('\n', ' ')

            # Make the comparison case-insensitive to get relative results
            if any(keyword_part.lower() in field.lower() for keyword_part in keyword.split() for field in [url, headline, article_content]):
                data.append([url, headline, article_content])

        return data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return []
#Print the data into csv file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['URL', 'Headline', 'Article Content'])

    for keyword in keywords:
        urls_and_headlines = make_api_request(keyword)
        writer.writerows(urls_and_headlines)
        time.sleep(12)
#Sleeping for 12 seconds due to api rate-limit
print(f"Scraping completed. Data has been saved to {csv_file}") # Return log
