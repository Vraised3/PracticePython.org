num = int(input('How many numbers of the fibonacci sequence do you want: '))
sum = [0, 1]
# sum.append([(sum[a] + sum[a - 1]) for a in range(1, num)])
for a in range(1, num + 1):
    sum.append(sum[a] + sum[a - 1])

print(sum)
# sum.append([(sum[a] + sum[a - 1]) for a in range(1, num)])
