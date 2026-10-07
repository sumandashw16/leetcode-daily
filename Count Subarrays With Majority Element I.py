x = [1,2,2,3]

total_count = 0
for i in range(len(x)):
    for j in range(i, len(x)):
        two_counts = x[i:j+1].count(1)
        # print(two_counts, end=" ")
        # print(len(x[i:j]))
        # print(x[i:j+1])

        if two_counts/len(x[i:j+1]) >= 0.5:
            total_count += 1
print(total_count)
