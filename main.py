import os
import pandas as pd

from modules.create_draft_item import DraftItemCreater

PHOTOS_FOLDER_PATH = os.getcwd() + "\photos"

BASE_URL = 'https://api.ebay.com'

# Your access token
access_token = 'YOUR ACCESS TOKEN'

draft_creater = DraftItemCreater()


# Create DataFrame
df = pd.DataFrame(columns=[
    "Title", "SKU", "Description", "Pricing Format", "Price", "Quantity", 
    "Allow Offers", "Shipping Method", "Package Weight", "Package Dimensions", 
    "Domestic Shipping Cost Type", "Domestic Shipping Service", "Rate Table", 
    "Flat Shipping Rule", "Promotional Shipping Rule", "Excluded Locations", 
    "Payment Preferences", "Photo"
])

# Sample data in a list
data = [
    "Item Title", "Item SKU", "Item Description", "FIXED_PRICE", 100.00, 1, 
    True, "USPS_FIRST_CLASS", 10.0, {"Length": 10.0, "Width": 8.0, "Height": 6.0},
    "FLAT_RATE", "USPS_FIRST_CLASS", "RATE_TABLE_ID", "FLAT_RATE", 
    "PROMOTIONAL_SHIPPING_RULE_ID", ["EXCLUDED_LOCATION"], ["PAYPAL"], ""
]


photo_urls = [
  os.path.join(PHOTOS_FOLDER_PATH, photo)
  for photo in os.listdir(PHOTOS_FOLDER_PATH)
]

counter = 0
for photo_url in photo_urls:
    # Add the data to the DataFrame
    df.loc[len(df)] = data
    # Set the photo
    df.at[counter, "Photo"] = photo_url
    
    # Create the draft item
    response = draft_creater.create_draft_item(access_token=access_token, BASE_URL=BASE_URL, data=df.iloc[counter].to_json())
    print(response)
    counter = counter + 1
    







