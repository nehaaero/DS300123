import json

dict = {
  "Uttarakhand": "Dehradun",
  "Karnataka": "Bengaluru",
  "Tamil Nadu": "Chennai",
  "Orrisa": "Bhubaneswar",
  "Telangana": "Hyderabad",
  "Kerala": "Thiruvananthapuram",
  "Rajasthan": "Jaipur"
}

with open("indian_states.json", 'w') as file:
   json_object = json.dumps(dict, indent = 7)
   file.write(json_object)