from bs4 import BeautifulSoup
import pandas
import os


class AmazonScraper:
    def __init__(self, folder_path,filename):
        self.folder_path = folder_path
        self.data = {
            'title': [],
            'link': [],
            'rating': [],
            'price': []
        }
        self.read_files()
        self.save_to_csv(filename=filename)

    def read_files(self):
        for file_name in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                html_doc = f.read()
            self.extract_data(html_doc)

    def extract_data(self, html_doc):
        soup = BeautifulSoup(html_doc, "html.parser")

        try:
            # Title
            heading = soup.find("h2")
            if heading:
                self.data['title'].append(heading.getText())
            else:
                self.data['title'].append("N/A")

            # Link
            link_tag = heading.find_previous('a') if heading else None
            if link_tag and link_tag.has_attr('href'):
                link = "https://amazon.in" + link_tag['href']
                self.data['link'].append(link)
            else:
                self.data['link'].append("N/A")

            # Rating
            rating_tag = soup.find('span', class_="a-icon-alt")
            if rating_tag:
                self.data['rating'].append(rating_tag.getText())
            else:
                self.data['rating'].append("N/A")

            # Price
            price_tag = soup.find('span', class_="a-price-whole")
            if price_tag:
                self.data['price'].append(price_tag.getText())
            else:
                self.data['price'].append("N/A")

        except UnicodeDecodeError as e:
            print("Unicode Error:", e)
        except Exception as e:
            print("Didn't get:", e)

    def save_to_csv(self, filename):
        df = pandas.DataFrame(self.data)
        df = df.sort_values(by="price",ascending=False)
        print(df)
        df.to_csv(filename, index=False)
        
        
# a = AmazonScraper("data-base")
# a.save_to_csv("Exported_Data.csv")


