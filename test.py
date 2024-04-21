import json
import hid

for x in hid.enumerate(0x046D):
    if x["product_id"] == 0xc52b and x['usage'] == 0x0001 and x['usage_page'] == 0xFF00:
        print("Bolt")
    if x['usage'] == 0x0202 and x['usage_page'] == 0xff43:
    	print(
			"Bluetooth {} ({:04x}) = {}".format(
				x["product_string"] or "(None)",
				x["product_id"],
				# x['usage'],
				# x['usage_page'],
				x["path"],
			)
    )

# for d in hid.enumerate():
# 	print(d)
# json_str = json.dumps(hid.enumerate(), indent=4)
# print(json_str)
