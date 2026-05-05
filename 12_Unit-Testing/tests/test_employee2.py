import unittest
from app import employee

class TestEmployee(unittest.TestCase):
    """Test the Employee class"""

    @classmethod
    def setUpClass(cls):
        print('setupClass')
    
    
    def setUp(self):
        """Create a test employee"""
        self.emp_1 = employee.Employee('John', 'Doe', 50000)  #employee is called by module & Employee is called by class
        self.emp_2 = employee.Employee('Jane', 'Smith', 60000)
        
    def tearDown(self):
        pass

    def test_email(self):
        """Test the email property"""
        self.assertEqual(self.emp_1.email, 'John.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')
        
        self.emp_1.first = 'Jim'
        self.emp_2.first = 'Johnny'
        
        self.assertEqual(self.emp_1.email, 'Jim.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Johnny.Smith@email.com')
        
    def test_fullname(self):
        """ Test the fullname property"""
        self.assertEqual(self.emp_1.fullname, 'John Doe')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')
        
        self.emp_1.first = 'Jim'
        self.emp_2.first = 'Johnny'
        
        self.assertEqual(self.emp_1.fullname, 'Jim Doe')
        self.assertEqual(self.emp_2.fullname, 'Johnny Smith')
        
    def test_apply_raise(self):
        """Test the Apply Raise Method"""
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
            
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
        
if __name__ == '__main__':
    unittest.main()
            
        