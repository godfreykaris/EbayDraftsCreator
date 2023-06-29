import json
import requests


class DraftItemCreater:

  def create_draft_item(self, access_token, BASE_URL, data):
    headers = {
      'Authorization': 'Bearer ' + access_token,
      'Content-Type': 'application/json'
    }
  

    response = requests.post(
      f'{BASE_URL}/sell/inventory/v1//bulk_create_or_replace_inventory_item',
      headers=headers,
      data=data)
    if response.status_code == 201:
      print('Draft item created successfully.')
      return response.json()['draft_id']
    else:
      print('Error creating draft item.')
      return response.content
