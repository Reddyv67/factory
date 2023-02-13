def job_scheduling(n, jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    task = 0
    earnings = 0
    end = 0
    for i in range(n):
        if jobs[i][0] >= end:
            task += 1
            end = jobs[i][1]
            earnings += jobs[i][2]
    return [n - task, sum([j[2] for j in jobs]) - earnings]

if __name__ == '__main__':
    n = int(input('Enter the number of Jobs: '))
    jobs = []
    for i in range(n):
        start = int(input('Enter job start time: '))
        end = int(input('Enter job end time: '))
        profit = int(input('Enter job earnings: '))
        jobs.append([start, end, profit])
    result = job_scheduling(n, jobs)
    print('The number of tasks and earnings available for others')
    print('Task:', result[0])
    print('Earnings:', result[1])
