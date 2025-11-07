from src.conta import Conta

def test_conta_inicia_com_saldo_zero():
    c = Conta()
    assert c.saldo() == 0