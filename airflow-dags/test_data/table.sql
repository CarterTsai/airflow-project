欄位名稱	資料型別	描述
product_id	INT	商品ID
category	VARCHAR	商品類別
price	DECIMAL	商品價格
quantity	INT	購買數量
purchase_date	DATE	購買日期

CREATE TABLE shopping_data (
    product_id INT,
    category VARCHAR(255),
    price DECIMAL(10, 2),
    quantity INT,
    purchase_date DATE
);

欄位名稱	資料型別	描述
product_id	INT	商品ID
product_name	VARCHAR	商品名稱
brand	VARCHAR	品牌名稱
supplier	VARCHAR	供應商名稱

CREATE TABLE product_mapping (
    product_id INT,
    product_name VARCHAR(255),
    brand VARCHAR(255),
    supplier VARCHAR(255)
);