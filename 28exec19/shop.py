def ShopOLAP(n, items):
    new_items = dict()
    for each in items:
        item, total = each.split()
        if item not in new_items.keys():
            new_items[item] = int(total)
        else:
            new_items[item] += int(total)

    results = []
    for key in new_items.keys():
        results.append(key+' '+str(new_items[key]))

    return sorted(results)
