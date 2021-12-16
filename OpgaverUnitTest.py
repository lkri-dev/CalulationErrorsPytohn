import unittest
import Opgave1_main
import Opgave2_main


class TestMethod(unittest.TestCase):

	def test_opgave1_bmi(self):
		vaegt = 60.0
		hoejde = 1.8
		self.assertEqual(Opgave1_main.bmi_udregner(vaegt, hoejde), 18.51851851851852)

	def test_opgave2(self):
		i = 2.0
		r = 2.5
		u = 5.0
		self.assertEqual(Opgave2_main.ohms_lov(i_amp=i, u_volt=u), r)
		self.assertEqual(Opgave2_main.ohms_lov(i_amp=i, r_ohms=r), u)
		self.assertEqual(Opgave2_main.ohms_lov(r_ohms=r, u_volt=u), i)


if __name__ == '__main__':
	unittest.main()
