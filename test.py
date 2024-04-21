import json
import hid

for x in hid.enumerate(0x046D):
    print(
        "{:04x}  {}  at: {} {}".format(
            x["product_id"],
            x["product_string"] or "(None)",
            x['usage'],
            x['usage_page'],
            # x["path"],
        )
    )

# for d in hid.enumerate():
# 	print(d)
# json_str = json.dumps(hid.enumerate(), indent=4)
# print(json_str)
