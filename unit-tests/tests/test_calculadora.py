import calculadora

def test_soma_inteiros():
    resultado = calculadora.soma(1, 2)
    assert resultado == 3

def test_soma_invalido():
    resultado = calculadora.soma('1', 2)
    assert resultado == 3