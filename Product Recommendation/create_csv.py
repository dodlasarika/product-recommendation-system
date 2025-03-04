import pandas as pd

# Creating a simple dataset
data = {
    'Product_ID': [1, 2, 3, 4, 5],
    'Product_Name': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Wearables'],
    'Description': [
        'A powerful laptop with 16GB RAM and SSD storage.',
        'A smartphone with an amazing camera and battery life.',
        'A lightweight tablet with a large display for work and entertainment.',
        'Wireless headphones with noise cancellation and deep bass.',
        'A smartwatch with fitness tracking and long battery life.'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('products.csv', index=False)

print("✅ Dataset Created: 'products.csv'")

import pandas as pd

# Expanded dataset with more real-world products
data = {
    'Product_ID': list(range(1, 16)),  # Assigning unique IDs
    'Product_Name': [
        'iPhone 15 Pro', 'Samsung Galaxy S23', 'MacBook Air M2', 'Dell XPS 13', 'Sony WH-1000XM5 Headphones',
        'Boat Rockerz 450', 'Apple iPad Pro', 'Samsung 55-inch Smart TV', 'Nike Air Max Shoes', 'Adidas Running Shoes',
        'Rolex Watch', 'Fossil Smartwatch', 'Dyson Vacuum Cleaner', 'LG 1.5 Ton AC', 'Amazon Echo Dot'
    ],
    'Category': [
        'Smartphones', 'Smartphones', 'Laptops', 'Laptops', 'Headphones',
        'Headphones', 'Tablets', 'Televisions', 'Footwear', 'Footwear',
        'Watches', 'Watches', 'Home Appliances', 'Home Appliances', 'Smart Devices'
    ],
    'Description': [
        'Latest Apple iPhone 15 Pro with A17 Bionic chip and 48MP camera.',
        'Samsung Galaxy S23 with Snapdragon 8 Gen 2 and Dynamic AMOLED display.',
        'MacBook Air M2 with 13.6-inch Retina display, 8GB RAM, and 256GB SSD.',
        'Dell XPS 13 with Intel Core i7, 16GB RAM, and 512GB SSD for high performance.',
        'Sony WH-1000XM5 Wireless Noise-Canceling Headphones with 30-hour battery life.',
        'Boat Rockerz 450 wireless Bluetooth headphones with deep bass and long battery life.',
        'Apple iPad Pro with M2 chip, 12.9-inch Liquid Retina display, and Apple Pencil support.',
        'Samsung 55-inch Crystal 4K UHD Smart TV with HDR10+ and voice control support.',
        'Nike Air Max running shoes with breathable mesh and comfortable cushioning.',
        'Adidas lightweight running shoes with excellent grip and stylish design.',
        'Rolex luxury watch with automatic movement and water resistance.',
        'Fossil Gen 6 Smartwatch with heart rate monitor, Alexa built-in, and fitness tracking.',
        'Dyson cordless vacuum cleaner with powerful suction and long battery life.',
        'LG 1.5 Ton 5 Star Inverter AC with dual inverter compressor and energy saving mode.',
        'Amazon Echo Dot (5th Gen) smart speaker with Alexa and improved bass response.'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('products.csv', index=False)

print("✅ Updated Dataset Created: 'products.csv'")
