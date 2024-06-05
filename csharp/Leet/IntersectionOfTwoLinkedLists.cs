using Leet.List;

namespace Leet.IntersectionOfTwoLinkedLists
{
    public class Solution
    {
        public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
        {
            var nodesA = new HashSet<ListNode>();

            var pointer = headA;
            while (pointer != null)
            {
                nodesA.Add(pointer);
                pointer = pointer.next;
            }

            pointer = headB;
            while (pointer != null)
            {
                if (nodesA.Contains(pointer)) break;
                pointer = pointer.next;
            }

            return pointer;
        }
    }
}
