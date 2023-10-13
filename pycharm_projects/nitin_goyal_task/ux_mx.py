import json

def get_provision_ids_with_null_phone_numbers(json_file_path):
    try:
        # Load the JSON data from the local system
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        provision_ids = []

        # Iterate through the accountServices array
        for entry in data.get("accountServices", []):
            display_properties = entry.get("displayProperties", [])

            # Check if "PhoneNumber" is in the names list and "value" is null
            phone_number_entry = next((d for d in display_properties if d["name"] == "PhoneNumber"), None)
            if phone_number_entry is not None and not phone_number_entry["value"]:
                provision_id = entry.get("ProvisionId")
                if provision_id:
                    provision_ids.append(provision_id)

        return provision_ids

    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return []


# your file_path:
file_path_ux = '/home/afzhal-ahmed-s/Downloads/UX.json'
file_path_mx = '/home/afzhal-ahmed-s/Downloads/MX.json'

provision_ids_1 = get_provision_ids_with_null_phone_numbers(file_path_ux)
provision_ids_2 = get_provision_ids_with_null_phone_numbers(file_path_mx)

print("Provision IDs from UX.json:", provision_ids_1)
print("Provision IDs from MX.json:", provision_ids_2)

