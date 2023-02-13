def maxEarnings(n, jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    start = [0] * 2400
    end = [0] * 2400
    total = 0
    count = 0
    for i in range(n):
        if start[jobs[i][0]] == 0 and end[jobs[i][1]] == 0:
            start[jobs[i][0]] = 1
            end[jobs[i][1]] = 1
            total += jobs[i][2]
            count += 1
    return [n-count, total]

n = int(input("Enter the number of Jobs: "))
jobs = []
print("Enter job start time, end time, and earnings")
for i in range(n):
    start = int(input().strip())
    end = int(input().strip())
    earnings = int(input().strip())
    jobs.append([start, end, earnings])
result = maxEarnings(n, jobs)
print("The number of tasks and earnings available for others")
print("Task:", result[0])
print("Earnings:", result[1])
