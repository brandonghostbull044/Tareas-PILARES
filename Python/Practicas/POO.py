class CuentaBancaria:
    def __init__(self, num_cuenta, nopmbre_titular, balance):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nopmbre_titular
        self.balance = balance
    def generar_balance(self):
        print(self.balance)
    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
        else:
            self.balance = monto
mi_cuenta = CuentaBancaria('`05-356-643', 'Brandon Leon', 7000)
alberto = CuentaBancaria('2342342', 'Alberto Parra', 10000)

alberto.generar_balance()






