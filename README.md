# New York Times Scraper

## Introduction

This project utilizes the New York Times API to crawl news articles with some keywords. The New York Times API provides access to a wealth of information, including articles, images, and more, allowing you to integrate up-to-date news content into your applications or projects.

## New York Times API

### Obtaining API Key

Before you begin, you'll need to obtain an API key from the New York Times Developer Network. Follow these steps:

1. **Create an Account:** If you don't have one, create an account on the [New York Times Developer Network](https://developer.nytimes.com/apis).

2. **Create a New App:** Once logged in, create a new app to generate an API key.

3. **Copy API Key:** After creating the app, you'll be provided with an API key. Copy this key; you'll need it to authenticate your requests.

## Usage

To use the New York Times API in this project, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/SindorimBear/NYTimes-Scraper.git
    cd SindorimBear
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set API Key:**
     Replace the `api_key` with the API key obtained from the New York Times Developer Network.

4. **Run the Project:**
    Execute the Python script to see the [specific functionality or purpose] in action.
    ```bash
    python nyscraper.py
    ```

## Python Code Explanation

In this section, you'll find a detailed explanation of the Python code provided in the repository. It covers the following methods:
- Call API-key for endpoint
- Setup keywords
- Defining the range of date
- Saving into csv file
- API rate limit handling
For a step-by-step guide and additional details, refer to the comments within the code itself.

Feel free to explore and modify the code to suit your needs!

1. **Get Your API Key:**
   - Go to the [New York Times Developer Portal](https://developer.nytimes.com/apis) and create an account.
   - Create a new app to get your API key.
   - Replace the placeholder `api_key` in the script with your actual API key.

2. **Set Your Keywords and Date Range:**
   - Adjust the `keywords` list to include terms you're interested in.
   - Set the `begin_date` and `end_date` to the desired date range.

3. **Run the Script:**
   - Execute the script in your Python environment.

4. **Check the Results:**
   - The script fetches articles containing the specified keywords and saves the data to a CSV file (`nyt_data.csv` by default).

### Notes

- Make sure to handle your API key securely.
- The script includes a delay between requests to comply with API rate limits. For more information, refer to the following: [New York Times Developer Portal](https://developer.nytimes.com/faq#:~:text=11.-,Is%20there%20an%20API%20call%20limit%3F,at%20code%40nytimes.com.)

### Running the Script

```bash
python nyscraper.py
```

