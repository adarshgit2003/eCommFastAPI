# Purpose: To define the schema for address

def address_serial(address) -> dict:
    return {
        "city": address["city"],
        "state": address["state"],
        "country": address["country"],
        "pincode": address["pincode"]
    }