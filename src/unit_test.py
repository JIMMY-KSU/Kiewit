import unittest
#from structure_of_scripts import do_something

class Test_dosomething_fn(unittest.TestCase):
    
    def test_dosomething(self):# We will talk about this self object later when you revise classes
        """
        Write your discription for the unit test
        """
        
        
        x = 234
        expected = 2*234
        got = do_something(x)
        self.assertAlmostEqual(expected, got, places=7,
                               msg='expected {:.8f} but got {:.8f}')
        
      
        
if __name__ == '__main__':
    
    unittest.main()