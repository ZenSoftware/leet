// https://leetcode.com/problems/course-schedule/description/
namespace Today4.CourseSchedule;

public class Solution
{
    public bool CanFinish(int numCourses, int[][] prerequisites)
    {
        var graph = new Dictionary<int, List<int>>();
        var indegree = new Dictionary<int, int>();
        foreach (var prereq in prerequisites)
        {
            if (!graph.ContainsKey(prereq[1]))
                graph[prereq[1]] = new List<int>();
            graph[prereq[1]].Add(prereq[0]);

            if (!indegree.ContainsKey(prereq[0]))
                indegree[prereq[0]] = 0;
            indegree[prereq[0]] += 1;
        }

        var queue = new Queue<int>();
        for (int course = 0; course < numCourses; course++)
        {
            if (!indegree.ContainsKey(course))
                queue.Enqueue(course);
        }

        var count = 0;
        while (queue.Count > 0)
        {
            var course = queue.Dequeue();
            count++;
            if (graph.ContainsKey(course))
            {
                foreach (var adj in graph[course])
                {
                    indegree[adj] -= 1;
                    if (indegree[adj] == 0)
                        queue.Enqueue(adj);
                }
            }
        }

        return count == numCourses;
    }
}