import sys
sys.path.append("../")

import os  # NOQA
import pytest  # NOQA -> para evitar que o autopep8 mova o import
from payments.pix import Pix  # NOQA


def test_pix_create_payment():
    pix_instance = Pix()

    # create a payment
    payment_info = pix_instance.create_payment(base_dir="../")

    assert "bank_payment_id" in payment_info
    assert "qr_code_path" in payment_info

    qr_code_path = payment_info["qr_code_path"]
    assert os.path.isfile(f"../static/img/{qr_code_path}.png")
