import phonenumbers
from phonenumbers import geocoder, carrier, timezone, PhoneNumberFormat, number_type
from phonenumbers.phonenumberutil import region_code_for_number

def deep_lookup(phone_number: str):
    parsed = phonenumbers.parse(phone_number)

    if not phonenumbers.is_valid_number(parsed):
        return {"Error": "Invalid number"}

    info = {
        "E.164": phonenumbers.format_number(parsed, PhoneNumberFormat.E164),
        "International": phonenumbers.format_number(parsed, PhoneNumberFormat.INTERNATIONAL),
        "National": phonenumbers.format_number(parsed, PhoneNumberFormat.NATIONAL),
        "Country Code": parsed.country_code,
        "Region": region_code_for_number(parsed),
        "Location": geocoder.description_for_number(parsed, "en"),
        "Carrier": carrier.name_for_number(parsed, "en"),
        "Time Zones": timezone.time_zones_for_number(parsed),
        "Number Type": number_type(parsed),
        "Is Valid?": phonenumbers.is_valid_number(parsed),
        "Is Possible?": phonenumbers.is_possible_number(parsed)
    }

    return info

# Use it
if __name__ == "__main__":
    number = "+94713703131"  # Your number
    result = deep_lookup(number)

    print("\n🔍 Phone Number Metadata:")
    for k, v in result.items():
        print(f"{k}: {v}")
