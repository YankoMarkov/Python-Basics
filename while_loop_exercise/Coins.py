tips = float(input())
tips = int(tips * 100)
counter = 0

counter += tips // 200
tips %= 200
counter += tips // 100
tips %= 100
counter += tips // 50
tips %= 50
counter += tips // 20
tips %= 20
counter += tips // 10
tips %= 10
counter += tips // 5
tips %= 5
counter += tips // 2
tips %= 2
counter += tips // 1
tips %= 1

print(counter)
