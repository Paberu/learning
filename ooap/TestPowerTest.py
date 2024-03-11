import unittest
from PowerSet import PowerSet


class TestPowerSet(unittest.TestCase):

    def setUp(self):
        self.set1 = PowerSet()
        self.set2 = PowerSet()
        self.set3 = PowerSet()
        self.str1 = '''
                    Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
                    Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.
                '''

        self.str2 = '''
                    Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
                '''

        self.str3 = '''A design is a plan or specification for the construction of an object or system or for the implementation of an activity or process, or the result of that plan or specification in the form of a prototype, product or process. The verb to design expresses the process of developing a design. In some cases, the direct construction of an object without an explicit prior plan (such as in craftwork, some engineering, coding, and graphic design) may also be considered to be a design activity. The design usually has to satisfy certain goals and constraints, may take into account aesthetic, functional, economic, or socio-political considerations, and is expected to interact with a certain environment. Major examples of designs include architectural blueprints, engineering drawings, business processes, circuit diagrams, and sewing patterns'''

        strings = self.str1.split()
        for string in strings:
            self.set1.put(string)

        strings = self.str2.split()
        for string in strings:
            self.set2.put(string)

        strings = self.str3.split()
        for string in strings:
            self.set3.put(string)

    def test_put0(self):
        set0 = PowerSet()
        self.assertEqual(set0.size(), 0)
        set0.put('Python')
        self.assertEqual(set0.size(), 1)

    def test_put1(self):
        self.assertEqual(self.set1.size(), 59)
        self.assertFalse(self.set1.get('Ruby'))
        self.set1.put('Ruby')
        self.assertTrue(self.set1.get('Ruby'))
        self.assertEqual(self.set1.size(), 60)

    def test_put2(self):
        self.assertEqual(self.set1.size(), 59)
        self.assertTrue(self.set1.get('Python'))
        self.set1.put('Python')
        self.assertTrue(self.set1.get('Python'))
        self.assertEqual(self.set1.size(), 59)

    def test_remove(self):
        self.assertEqual(self.set1.size(), 59)
        self.assertTrue(self.set1.get('Python'))
        self.set1.remove('Python')
        self.assertFalse(self.set1.get('Python'))
        self.assertEqual(self.set1.size(), 58)

    def test_intersection1(self):
        test_set = self.set1.intersection(self.set3)
        self.assertEqual(test_set.size(), 10)

    def test_intersection2(self):
        for word in ['an','for','with','as','of','a','is','and','to','design']:
            self.set3.remove(word)
        test_set = self.set1.intersection(self.set3)
        self.assertEqual(test_set.size(), 0)

    def test_union1(self):
        temp_set1 = PowerSet()
        temp_set2 = PowerSet()
        temp_set1.put('size')
        temp_set1.put('two')
        test_set = temp_set1.union(temp_set2)
        self.assertEqual(test_set.size(), 2)
        self.assertTrue(test_set.get('size'))
        self.assertTrue(test_set.get('two'))

    def test_union2(self):
        test_set = self.set1.union(self.set3)
        self.assertEqual(test_set.size(), self.set1.size()+self.set3.size()-10)

    def test_difference1(self):
        test_set = self.set1.difference(PowerSet())
        self.assertEqual(test_set.size(), self.set1.size())

    def test_difference2(self):
        temp_set = PowerSet()
        strings = self.str1.split()
        for string in strings:
            temp_set.put(string)
        test_set = self.set1.difference(temp_set)
        self.assertEqual(test_set.size(), 0)

    def test_difference3(self):
        test_set = self.set1.difference(self.set3)
        self.assertEqual(test_set.size(), self.set1.size() - 10)

    def test_issubset1(self):
        self.assertTrue(self.set1.issubset(self.set2))

    def test_issubset2(self):
        self.assertFalse(self.set2.issubset(self.set1))

    def test_issubset3(self):
        self.set2.put('Ruby')
        self.assertFalse(self.set1.issubset(self.set2))


unittest.main()
