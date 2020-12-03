def greedy_sheduling(jobs, criteria):
    j = []
    for job in jobs:
        w, l = job 
        s = criteria(w, l)
        j.append((w, l, s))

    jobs_sorted = sorted(j, key=lambda job: (job[2], job[0]), reverse=True)
    C = 0 #completion time
    weighted_sum = 0
    for job in jobs_sorted:
        w, l, s = job
        C += l
        weighted_sum  += C * w
    
    return weighted_sum

def ratio(a, b):
    return a / b

def diff(a, b):
    return a - b


def alg(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        jobs = []
        for i in range(n):
            w, l = f.readline().strip().split()
            jobs.append((int(w), int(l)))

        return [greedy_sheduling(jobs, diff), greedy_sheduling(jobs, ratio)]


if __name__ == '__main__':
    with open('tests/problem13.4test.txt', 'r') as f:
        n = int(f.readline())
        jobs = []
        for i in range(n):
            w, l = f.readline().strip().split()
            jobs.append((int(w), int(l)))

        print(greedy_sheduling(jobs, diff))
        print(greedy_sheduling(jobs, ratio))