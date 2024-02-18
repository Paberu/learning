def ShopOLAP(n, items):
    new_items = dict()
    for each in items:
        item, total = each.split()
        if item not in new_items.keys():
            new_items[item] = int(total)
        else:
            new_items[item] += int(total)

    items = [item[0]+' '+str(item[1])
             for item in sorted(new_items.items(), key=lambda item: (-item[1], item[0]), reverse=True)]
    items.reverse()

    return items

