
def printing_items(items):
    for (k, v) in items.items():
        print(f"{k}: {v}")


data = input().split(" ")

key_materials = {
    "shards": 0,
    "motes": 0,
    "fragments": 0
}
end = False
while True:
    for idx in range(0,len(data),2):
        key = data[idx +1].lower()
        value = int(data[idx])
        if key in key_materials:
            key_materials[key] += value
        else:
            key_materials[key] = value
        if key_materials["fragments"] >= 250:
            key_materials["fragments"] -= 250
            print("Valanyr obtained!")
            end = True
            break
        elif key_materials["shards"] >= 250:
            key_materials["shards"] -= 250
            print("Shadowmourne obtained!")
            end = True
            break
        elif key_materials["motes"] >= 250:
            key_materials["motes"] -= 250
            print("Dragonwrath obtained!")
            end = True
            break
    if end: break
    data = input().split(" ")

legendary_item = {key: value for (key,value) in key_materials.items() if key in ['fragments','shards','motes']}
junk_items = {key: value for (key,value) in key_materials.items() if key not in ['fragments','shards','motes']}

legendary_item_sorted = dict(sorted(legendary_item.items(), key = lambda x: (-x[1],x[0])))
junk_item_sorted = dict(sorted(junk_items.items(), key = lambda x: (x[0],x[0])))

printing_items(legendary_item_sorted)
printing_items(junk_item_sorted)
