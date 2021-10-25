def ShopOLAP(n, items):
    new_items = dict()
    for each in items:
        item, total = each.split()
        if item not in new_items.keys():
            new_items[item] = int(total)
        else:
            new_items[item] += int(total)

    sorted_items = [item[0]+' '+str(item[1]) for item in sorted(new_items.items(), key=lambda item: (-item[1], item[0]), reverse = True)]
    sorted_items.reverse()

    return sorted_items
    
    bought_comp = dict()
    for value in new_items.values():
        if value not in bought_comp:
            bought_comp[value] = True
        else:
            bought_comp[value] = False
    
    results = ['']*len(new_items)
    for key, value in new_items.items():
        if bought_comp[value]:
            results[items.index(value)] = key + ' ' + str(value)
    

    return results
