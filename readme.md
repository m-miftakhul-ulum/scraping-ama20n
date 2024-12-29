### README  

# Ama20n Product Scraper  

This Python script scrapes product data from Ama20n, such as titles, prices, and links, based on a search keyword. The data is saved in JSON format and converted to CSV for easier analysis.  

---

## Features  

- Scrape product titles, prices, and links for a specified number of items.  
- Uses Selenium with Chrome WebDriver to interact with Ama20n's search functionality.  
- Stores cookies for persistent sessions to avoid frequent login prompts.  
- Saves scraped data into `dataset.json` and converts it to a timestamped CSV file.  
- Configurable to run in headless mode for seamless background execution.  

---

## Prerequisites  

Ensure the following tools and libraries are installed before running the script:  

### Python Libraries  
Install the required libraries using `pip`:  
```bash  
pip install curl-cffi beautifulsoup4 selenium  
```  

### WebDriver  
Download and install the Chrome WebDriver that matches your installed Chrome browser version. [Download here](https://chromedriver.chromium.org/downloads).  

---

## How to Use  

1. **Load Cookies**  
   Place a valid `cookies.json` file in the working directory to avoid frequent logins. This file should contain cookies in JSON format.  

2. **Run the Script**  
   Execute the script by running:  
   ```bash  
   python script_name.py  
   ```  

3. **Set Search Query and Data Count**  
   Modify the search query and data count by editing the following lines in the script:  
   ```python  
   inputElement.send_keys('controller for pc wireless')  
   get_data(50)  # Number of items to scrape  
   ```  

4. **Output**  
   - The scraped data will be saved in `dataset.json`.  
   - A timestamped CSV file will also be generated in the same directory, e.g., `2024-12-29-12-00-00.csv`.  

---

## Key Functions  

### `get_data(request)`  
Scrapes product data from Ama20n.  

- **Arguments:**  
  `request`: The number of products to scrape.  

- **Process:**  
  - Loads cookies and initializes the Chrome WebDriver.  
  - Searches for the specified keyword on Ama20n.  
  - Iteratively extracts product data (title, price, link).  
  - Saves the data to a JSON file and calls `save_document()` to generate a CSV.  

### `save_document()`  
Converts the JSON data to a CSV file with a timestamped filename.  

---

## Notes  

- Ensure the `cookies.json` file does not include unsupported attributes (e.g., `"sameSite"`).  
- This script is configured for `ama20n.com`. Update the domain if you're targeting a different Ama20n region.  
- Modify the CSS selectors (`.s-result-item`, `.a-size-medium`, etc.) if Ama20n's layout changes.  

---

## Disclaimer  

This script is intended for educational purposes only. Scraping Ama20n or similar websites may violate their terms of service. Use responsibly and adhere to local regulations.