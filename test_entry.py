import pandas as pd
import unittest
from add_new_entry import add_new_entry

class TestAddNewEntry(unittest.TestCase):
    def test_add_new_entry(self):
        # Create a test DataFrame
        revenue = pd.DataFrame(columns=["Year", "Studio_Entertainment", "Disney_Products", "Disney_Parks_Resorts", "Disney_Media_Networks", "Total"])
        
        # Define test values
        year = 2059
        studio_entertainment = 205400.0
        disney_products = 1212100.0
        disney_parks_resorts = 3555000.0
        disney_media_networks = 5002440.0
        
        # Call the add_new_entry function with test values
        result = add_new_entry(revenue, year, studio_entertainment, disney_products, disney_parks_resorts, disney_media_networks)

        # Perform assertions here based on the expected changes to the 'revenue' DataFrame
        self.assertEqual(len(result), 1)  # Check if one entry was added
        added_entry = result.iloc[0]
        self.assertEqual(added_entry["Year"], year)
if __name__ == '__main__':
    unittest.main()

