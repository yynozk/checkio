def best_stock(data):
    return max(data.items(), key=lambda x: x[1])[0]
