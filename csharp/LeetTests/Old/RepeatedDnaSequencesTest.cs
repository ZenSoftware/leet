using Leet.RepeatedDnaSequences;

namespace LeetTests.Old
{
    internal class RepeatedDnaSequencesTest
    {
        [Test]
        public void TestsRepeatedDnaSequences()
        {
            var soltuion = new Solution();

            Assert.That(
                soltuion.FindRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"),
                Is.EqualTo(new[] { "AAAAACCCCC", "CCCCCAAAAA" })
            );

            Assert.That(
                soltuion.FindRepeatedDnaSequences("AAAAAAAAAAAAA"),
                Is.EqualTo(new[] { "AAAAAAAAAA" })
            );

            Assert.That(
                soltuion.FindRepeatedDnaSequences("AAAAAAAAAAA"),
                Is.EqualTo(new[] { "AAAAAAAAAA" })
            );
        }
    }
}
