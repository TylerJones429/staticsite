import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "www.test.com")
        node2 = TextNode("This is a text node", "bold", "www.test.com")
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", "italic", "www.test.com")
        node2 = TextNode("This is a text node", "bold", "www.test.com")
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", "bold", "www.test.com")
        node2 = TextNode("This is not a text node", "bold", "www.test.com")
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", "bold", "www.test.com")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
