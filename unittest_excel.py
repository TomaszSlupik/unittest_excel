import unittest
import pandas as pd

def load_excel(file_path):
    return pd.read_excel(file_path)

my_excel = 'C:/Users/Tomek/Desktop/unittest.xlsx'

df = load_excel(my_excel)

print(df)

print ('----')

print ('Testy:')
class TestExcelData(unittest.TestCase):

    # Dekorator  @classmethod sprawia, że metoda setUpClass jest metodą klasy, a nie instancji.
    # dzięki temu metoda ta otrzymuje jako pierwszy argument klasę (cls)
    @classmethod
    def setUpClass(cls):
        cls.df = df

    # Sprawdzenie nagłówków
    def test_column_headers(self):
        headers = ['id', 'name', 'age', 'position', 'practice']
        actual_headers = list(self.df.columns)
        self.assertEqual(headers, actual_headers, "Kolumny nie zgadzają się")

    def test_id_is_numeric(self):
        # Sprawdza, czy kolumna 'id' jest numeryczna
        self.assertTrue(pd.api.types.is_numeric_dtype(self.df['id']), "Kolumna 'id' powinna być numeryczna")

    def test_name_is_str(self):
        # Sprawdza, czy kolumna 'name' jest stringiem
        self.assertTrue(pd.api.types.is_string_dtype(self.df['name']), "Kolumna 'name' powinna być stringiem")

    def test_row_count(self):
        # Sprawdza, czy DataFrame zawiera dokładnie 3 wiersze
        row_count = self.df.shape[0]
        self.assertEqual(row_count, 3, "DataFrame powinien zawierać 3 wiersze")

    def test_column_count(self):
        # Sprawdza, czy DataFrame zawiera dokładnie 5 kolumn
        column_count = self.df.shape[1]
        self.assertEqual(column_count, 5, "DataFrame powinien zawierać 5 kolumn")

if __name__ == '__main__':
    unittest.main(verbosity=2)