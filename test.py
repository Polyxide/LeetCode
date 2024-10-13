def knap_sack(dictionary, kg):

    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1][0], reverse=True))

    amount = 0
    for i in dictionary.items():
        amount += 1

    dp = [[0]*(kg+1) for _ in range(amount+1)]

    for i in range(1, amount+1):
        weight, cost = list(dictionary.values())[i-1]
        for j in range(1, kg+1):

            if weight > j:
                dp[i][j] = dp[i - 1][j]
            elif weight == j and dp[i-1][j] < cost:
                dp[i][j] = cost
            elif weight == j and dp[i - 1][j] > cost:
                dp[i][j] = dp[i - 1][j]
            elif j > weight:
                x = j - weight
                y = dp[i-1][x] + cost
                dp[i][j] = (y if y > dp[i-1][j] else dp[i-1][j])


    return print(dp[amount][kg])


items = dict()
items['phone'] = [1, 2000]
items['pods'] = [2, 2000]
items['stereo'] = [4, 3000]
items['laptop'] = [2, 2000]
items['guitar'] = [1, 1500]

max_weight = 6

knap_sack(items, max_weight)




