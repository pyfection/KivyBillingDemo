"""
A simple App in Kivy to demonstrate billing for Google Play

Billing library is a modified and updated version of:
https://github.com/knappador/billing-example
"""
import os


from kivy.app import App
from kivy.properties import ObjectProperty

from billing import Billing


PROD_DONATE = 'kivybillingdemo.prod.donate'


class KivyBillingDemo(App):
    skus = [
        PROD_DONATE,
        'android.test.purchased',
    ]
    billing = ObjectProperty()

    def on_start(self):
        pub_key = os.getenv('GPAY_PUB_KEY')
        self.billing = Billing(pub_key, self.skus)
        # self.billing.set_retry_prompt(modal_ctl.ask_retry_purchase)

    def donate(self, amount):
        print('wants to donate', amount, '$')
        self.billing.purchase(PROD_DONATE)
        print("Donated!")


app = KivyBillingDemo()
app.run()
