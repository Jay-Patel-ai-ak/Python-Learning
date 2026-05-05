import pytest 

@pytest.fixture
def setup_database():
    print("Setup Database")
    yield
    print("TearDown Database")
    
@pytest.fixture
def setup_config():
    print("Setup Configuration")
    yield
    print("Teardown Configuration")
    
class TestExample:
    def setup_method(self, method):
        print("Stup before each test method")
        
    def teardown_method (self, method):
        print("TearDown after each test method")
        
    def test_addition(self, setup_database, setup_config):
        assert 1 + 1 == 2
        
    def test_subtraction(self, setup_database, setup_config):
        assert 3 - 1 == 2
    
    
# Function Level 
@pytest.fixture (scope = "function")
def my_rectangle():
    return shape.Rectangle (10,20)

@pytest.fixture (scope = "package")
def wierd_rectangle():
    return shape.Rectangle (10,20)

@pytest.fixture (scope = "class")
def my_rectangle():
    return shape.Rectangle (10,20)

@pytest.fixture (scope = "module")
def wierd_rectangle():
    return shape.Rectangle (5,7)

@pytest.fixture (scope = "session")
def wierd_rectangle():
    return shape.Rectangle (5,7)