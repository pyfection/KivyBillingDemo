"""
A simple App in Kivy to demonstrate billing for Google Play

Billing library:
https://github.com/shashi278/android-iab-v3-kivy
"""

from kivy.core.window import Window
Window.size = (1280, 720)
import os

from kivy.app import App
from kivy.properties import ObjectProperty

# from iabwrapper import PythonBillingProcessor


PRODUCTS = {
    1: 'kivybillingdemo.prod.donate',
    5: 'kivybillingdemo.prod.donate5',
    10: 'kivybillingdemo.prod.donate10',
    100: 'kivybillingdemo.prod.donate100',
}


class KivyBillingDemo(App):
    billing = ObjectProperty()

    def on_start(self):
        license_key = os.getenv("KBD_LICENSE")
        # self.billing = PythonBillingProcessor(
        #     license_key
        # )

    def donate(self, amount):
        print('wants to donate', amount, 'EUR')
        # self.billing.purchase(PRODUCTS[amount])
        print("Donated!")


app = KivyBillingDemo()
app.run()
