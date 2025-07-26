import os
from bs4 import BeautifulSoup
import pandas as pd

# Folder containing HTML files
folder_path = r"D:\Software Tester\Laptop_data"

# List to store extracted data
laptop_data = []

# Loop through all HTML files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".html"):
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

            # Extract all product containers
            containers = soup.find_all("div", {"data-component-type": "s-search-result"})

            for container in containers:
                # Title (keep your original way)
                title_tag = container.find("h2")
                title = title_tag.get_text(strip=True) if title_tag else "N/A"

                # Price (keep your original way)
                price_tag = container.select_one("span.a-price span.a-offscreen")
                price = price_tag.get_text(strip=True) if price_tag else "N/A"

                # LINK (updated as per your working snippet)
                link_tag = container.find('a', class_='a-link-normal')
                if link_tag and 'href' in link_tag.attrs:
                    link = "https://www.amazon.in" + link_tag['href']
                else:
                    link = "N/A"

                # Append data
                laptop_data.append({
                    "Title": title,
                    "Price": price,
                    "Link": link
                })

# Save data to Excel
output_path = os.path.join(folder_path, "laptops_data.xlsx")
df = pd.DataFrame(laptop_data)
df.to_excel(output_path, index=False)

print("Data saved to Excel:", output_path)
