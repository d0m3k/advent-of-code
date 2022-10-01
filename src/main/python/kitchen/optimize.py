import itertools

# prices of products
# 15495.02
products = [5589, 3567, 1799, 2899, 1299, 2899]
products = [1799, 1299, 443]
# 15435.099999999999
#products = [5589, 3799, 1799, 2899, 1299, 2899]

# 0% discount for 1st product, 20% discount for 2nd product etc.
promo_rule = [0, 0.25, 0.44, 0.77, 0.99]
#promo_rule = [0, 0.3, 0.5, 0.8, 0.9999999]
# //2 + 1
buckets = itertools.product(range(0,len(products)), repeat=len(products))

#print(str_comb(buckets))

options = []
for bucket in buckets:
    group = {}
    for i in range(0, len(bucket)):
        curr = group.get(bucket[i], [])
        curr.append(products[i])
        group[bucket[i]] = curr
    options.append(tuple(map(lambda v: tuple(sorted(v, reverse=True)) ,group.values())))

possible_prices = {}
min_sum = float("inf")
min_option = []
for option in options:
    sum = 0
    for group in option:
        for i in range(len(group)):
            if i == len(group) - 1:
                if i >= len(promo_rule):
                    sum += group[i] * (1-promo_rule[len(promo_rule) - 1])
                else:
                    sum += group[i] * (1-promo_rule[i])
            else:
                sum += group[i]
    possible_prices[option] = sum
    if sum < min_sum:
        min_sum = sum
        min_option = option

    # print(possible_prices)
print(min_sum)
print(min_option)