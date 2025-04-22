using Old.IntersectionOfTwoLinkedLists;

namespace LeetTests.Old
{
    internal class IntersectionOfTwoLinkedListsTest
    {
        [Test]
        public void TestsIntersectionOfTwoLinkedLists()
        {
            var rootA = new ListNode(4);
            var nodeA2 = new ListNode(1);

            var rootB = new ListNode(5);
            var nodeB2 = new ListNode(6);
            var nodeB3 = new ListNode(1);

            var shared1 = new ListNode(8);
            var shared2 = new ListNode(4);
            var shared3 = new ListNode(5);

            rootA.next = nodeA2;
            rootB.next = nodeB2;
            nodeB2.next = nodeB3;
            nodeA2.next = shared1;
            nodeB3.next = shared1;
            shared1.next = shared2;
            shared2.next = shared3;

            var solution = new Solution();
            var result = solution.GetIntersectionNode(rootA, rootB);
            Assert.That(result, Is.EqualTo(shared1));
        }
    }
}
