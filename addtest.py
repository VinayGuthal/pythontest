import unittest
import add
class firsttest(unittest.TestCase):
    values=( (1,1,2),(1,2,3),(1,9,10),(9,2,11),(19,1,20),(99,1,100),(99,2,101))
    def testno(self):
        for num1,num2,num3 in self.values:
            num4=add.add(num1,num2);
            self.assertEqual(num3,num4);
class errortest(unittest.TestCase):
    def testzero(self):
        self.assertRaises(add.wrong,add.add,0,2);
    def testnegative(self):
        self.assertRaises(add.wrong,add.add,-1,3);
    def testdecimal(self):
        self.assertRaises(add.wrong,add.add,0.5,4);
if __name__ == "__main__":
    unittest.main()  
