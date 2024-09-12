import unittest
from my_python_logic import my_task

class TestMyTask(unittest.TestCase):
    
    def test_my_task(self):
        my_task()

if __name__ == "__main__":
    unittest.main()
