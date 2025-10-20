# test_mangatracker.py
"""
Tests for MangaTracker module.
"""

import unittest
from mangatracker import MangaTracker

class TestMangaTracker(unittest.TestCase):
    """Test cases for MangaTracker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaTracker()
        self.assertIsInstance(instance, MangaTracker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaTracker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
