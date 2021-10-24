def ShopOLAP(n, items):
    new_items = dict()
    for each in items:
        item, total = each.split()
        if item not in new_items.keys():
            new_items[item] = int(total)
        else:
            new_items[item] += int(total)

    results = ['']*len(new_items)
    items = sorted(new_items.values(), reverse=True)

    for key,value in new_items.items():
        results[items.index(value)] = key + ' ' + str(value)

    return results
