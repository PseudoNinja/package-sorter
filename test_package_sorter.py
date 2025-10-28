import unittest
from package_sorter import sort


class TestPackageSorter(unittest.TestCase):
    
    def test_standard_package(self):
        """Test standard package (not bulky, not heavy)"""
        result = sort(10, 10, 10, 5)
        self.assertEqual(result, "STANDARD")
    
    def test_standard_package_just_below_thresholds(self):
        """Test package just below all thresholds"""
        result = sort(149, 149, 44, 19.9)
        self.assertEqual(result, "STANDARD")
    
    def test_bulky_by_volume(self):
        """Test bulky package due to volume >= 1,000,000 cm³"""
        result = sort(100, 100, 100, 10)
        self.assertEqual(result, "SPECIAL")
    
    def test_bulky_by_volume_exactly_at_threshold(self):
        """Test bulky package with volume exactly 1,000,000 cm³"""
        result = sort(100, 100, 100, 15)
        self.assertEqual(result, "SPECIAL")
    
    def test_bulky_by_width_dimension(self):
        """Test bulky package with width >= 150 cm"""
        result = sort(150, 50, 50, 10)
        self.assertEqual(result, "SPECIAL")
    
    def test_bulky_by_height_dimension(self):
        """Test bulky package with height >= 150 cm"""
        result = sort(50, 150, 50, 10)
        self.assertEqual(result, "SPECIAL")
    
    def test_bulky_by_length_dimension(self):
        """Test bulky package with length >= 150 cm"""
        result = sort(50, 50, 150, 10)
        self.assertEqual(result, "SPECIAL")
    
    def test_heavy_package(self):
        """Test heavy package (mass >= 20 kg)"""
        result = sort(10, 10, 10, 20)
        self.assertEqual(result, "SPECIAL")
    
    def test_heavy_package_above_threshold(self):
        """Test heavy package well above threshold"""
        result = sort(50, 50, 50, 25)
        self.assertEqual(result, "SPECIAL")
    
    def test_rejected_bulky_and_heavy_by_volume(self):
        """Test rejected package (bulky by volume and heavy)"""
        result = sort(100, 100, 100, 20)
        self.assertEqual(result, "REJECTED")
    
    def test_rejected_bulky_and_heavy_by_dimension(self):
        """Test rejected package (bulky by dimension and heavy)"""
        result = sort(150, 50, 50, 20)
        self.assertEqual(result, "REJECTED")
    
    def test_rejected_all_thresholds_exceeded(self):
        """Test rejected package with all criteria exceeded"""
        result = sort(200, 200, 200, 50)
        self.assertEqual(result, "REJECTED")
    
    def test_edge_case_tiny_package(self):
        """Test very small package"""
        result = sort(1, 1, 1, 0.1)
        self.assertEqual(result, "STANDARD")
    
    def test_edge_case_large_volume_light(self):
        """Test large volume but light package"""
        result = sort(101, 101, 99, 5)
        self.assertEqual(result, "SPECIAL")
    
    def test_edge_case_small_volume_heavy(self):
        """Test small volume but heavy package"""
        result = sort(10, 10, 10, 100)
        self.assertEqual(result, "SPECIAL")


if __name__ == '__main__':
    unittest.main(verbosity=2)