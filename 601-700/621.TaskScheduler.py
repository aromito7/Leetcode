class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = len(tasks)
        tasks = [task.encode('ascii') for task in tasks]

        dic = defaultdict(lambda: 0)

        for task in tasks:
            dic[task] += 1

        tasks = sorted([[task, dic[task]] for task in dic], key = lambda x: -x[1])

        max_count = [len([task for task in tasks if task[1] == tasks[0][1]]), tasks[0][1]]
        
        output = (max_count[1] - 1) * (n + 1) + max_count[0]

        output = max(output, count)


        return output
