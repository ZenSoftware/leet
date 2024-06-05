namespace Leet.List
{
    public static class LeetList
    {
        public static ListNode ToList(int[] elements)
        {
            ListNode pointer = null;

            for (int i = elements.Length - 1; i >= 0; i--)
            {
                var node = new ListNode(elements[i]);
                node.next = pointer;
                pointer = node;
            }

            return pointer;
        }

        public static int[] ToArray(ListNode root)
        {
            if (root == null) return Array.Empty<int>();

            var result = new List<int>();
            var pointer = root;

            while(pointer != null)
            {
                result.Add(pointer.val);
                pointer = pointer.next;
            }

            return result.ToArray();
        }
    }

    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int x) { val = x; }
    }
}
