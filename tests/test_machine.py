import unittest
from machine import Machine


class MachineTest(unittest.TestCase):
    def test_init_machine(self):
        machine = Machine()
        self.assertIsInstance(machine.products,dict)
        self.assertIsNotNone(machine.products.get("A"))
        self.assertIsNotNone(machine.products.get("A").get("description"))
        self.assertEqual(machine.products["A"]["description"],"Chocolate biscuits")
        self.assertEqual(machine.products["A"]["price"],100)
        self.assertEqual(machine.products["A"]["stock"],10)

        self.assertIsInstance(machine.inserted_money,int)
        self.assertEqual(machine.inserted_money,0)

    def test_insert_coins(self):
        machine = Machine()
        machine.insert_money({100: 1})
        self.assertEqual(machine.inserted_money, 100)
        machine.insert_money({50: 1})
        self.assertEqual(machine.inserted_money, 150)

    def test_buy_item_A(self):
        machine = Machine()
        self.assertIsInstance(machine.press_button("A"),tuple)
        self.assertEqual(machine.press_button("A"),(None,None))
        machine.insert_money({100: 1})
        self.assertEqual(machine.press_button("A"),("A",0))
        self.assertEqual(machine.products["A"]["stock"],9)
        machine.insert_money({100: 2})
        self.assertEqual(machine.press_button("A"),("A",100))
        self.assertEqual(machine.products["A"]["stock"],8)

    def test_cancel_button(self):
        machine = Machine()
        self.assertEqual(machine.press_cancel(),0)
        machine.insert_money({100: 1})
        self.assertEqual(machine.press_cancel(),100)
        machine.insert_money({100: 1})
        machine.products["A"]["stock"] = 0
        self.assertEqual(machine.press_button("A"),(None,None))
        self.assertEqual(machine.press_cancel(),100)

        self.assertEqual(machine.inserted_money,0)


