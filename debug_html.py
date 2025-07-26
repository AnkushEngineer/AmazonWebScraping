from bs4 import BeautifulSoup

file_path = r"D:\Software Tester\Laptop_data\amazon_laptop_page_1.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

    # Find all product blocks
    products = soup.find_all("div", attrs={"data-component-type": "s-search-result"})

    print(f"Found {len(products)} products on the page.")

    for i, product in enumerate(products[:10], 1):  # first 10 products
        # Try first selector for title
        title_tag = product.find("span", class_="a-size-medium a-color-base a-text-normal")
        
        if not title_tag:
            # Fallback selector for title in <h2><a> structure
            h2_tag = product.find("h2")
            title_tag = h2_tag.find("a") if h2_tag else None
        
        title = title_tag.text.strip() if title_tag else "N/A"
        print(f"{i}. {title}")
