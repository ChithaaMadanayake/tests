import requests

def get_social_info_from_fullcontact(phone_number):
    api_key = 'your_api_key'  
    url = f'https://api.fullcontact.com/v3/person.enrich'
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    
    data = {
        "phone": phone_number
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return "Error: Unable to retrieve information."

phone_number = "+94702100515" 
info = get_social_info_from_fullcontact(phone_number)
print(info)
