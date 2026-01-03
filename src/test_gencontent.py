import unittest
from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_success(self):
        markdown = "# hello"
        title = extract_title(markdown)
        self.assertEqual(title, "hello")

    def test_extract_title_no_title(self):
        markdown = "no title."
        with self.assertRaises(ValueError) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "no title found")

if __name__ == "__main__":
    unittest.main()