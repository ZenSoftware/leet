// https://leetcode.com/problems/intersection-of-two-linked-lists/description/
using Leet.List;

namespace Old.IntersectionOfTwoLinkedLists
{
    public class Solution
    {
        public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
        {
            if (headA == null || headB == null) return null;

            var a = headA;
            var b = headB;

            while (a != b)
            {
                a = a == null ? headB : a.next;
                b = b == null ? headA : b.next;
            }

            return a;
        }
    }
}
