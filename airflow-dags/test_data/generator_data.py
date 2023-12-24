import csv
from faker import Faker
import pandas as pd

fake = Faker('zh_TW')  # 用台灣的資料格式

def generate_shopping_data(rows=100):
    with open('shopping_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['product_id', 'category', 'price', 'quantity', 'purchase_date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for _ in range(rows):
            writer.writerow({
                'product_id': fake.random_int(min=1, max=1000),
                'category': fake.random_element(['電子產品', '書籍', '服飾', '食品']),
                'price': round(fake.random_number(digits=4) / 100, 2),
                'quantity': fake.random_int(min=1, max=10),
                'purchase_date': fake.date_this_decade()
            })

def generate_product_mapping(rows=100):
    with open('product_mapping.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['product_id', 'product_name', 'brand', 'supplier']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for _ in range(rows):
            writer.writerow({
                'product_id': fake.random_int(min=1, max=1000),
                'product_name': fake.bs(),
                'brand': fake.company(),
                'supplier': fake.company()
            })

if __name__ == "__main__":
    # 透過參數來設定生成多少行資料，例如這裡生成了100行資料。
    generate_shopping_data(rows=1000)
    generate_product_mapping(rows=1000)
