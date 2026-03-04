# test_gascore.py
"""
Tests for GasCore module.
"""

import unittest
from gascore import GasCore

class TestGasCore(unittest.TestCase):
    """Test cases for GasCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GasCore()
        self.assertIsInstance(instance, GasCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GasCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
