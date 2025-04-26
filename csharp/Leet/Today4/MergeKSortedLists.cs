// https://leetcode.com/problems/merge-k-sorted-lists/description/
using Leet.List;
namespace Today4.MergeKSortedLists;

public class Solution
{
    public ListNode MergeKLists(ListNode[] lists)
    {
        var priorityQ = new PriorityQueue<ListNode, int>();
        foreach (var head in lists)
        {
            if (head is not null)
                priorityQ.Enqueue(head, head.val);
        }

        var dummy = new ListNode(-1);
        var pointer = dummy;
        while (priorityQ.Count > 0)
        {
            var cur = priorityQ.Dequeue();
            if (cur.next is not null)
                priorityQ.Enqueue(cur.next, cur.next.val);
            pointer.next = cur;
            pointer = pointer.next;
        }

        return dummy.next;
    }
}