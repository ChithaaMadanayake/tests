import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        
        location = geocoder.description_for_number(parsed_number, "en")
        
        sim_carrier = carrier.name_for_number(parsed_number, "en")
        
        time_zones = timezone.time_zones_for_number(parsed_number)
        
        return {
            "Location": location,
            "Carrier": sim_carrier if sim_carrier else "Unknown",
            "Time Zones": time_zones
        }
    except phonenumbers.phonenumberutil.NumberParseException:
        return "Invalid phone number format."

phone_number = "+94702100515" 
info = get_phone_info(phone_number)
print(info)
