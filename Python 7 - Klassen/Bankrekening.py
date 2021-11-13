class BankRekening:
    def __init__(self, naam, rekeningnummer, bedrag=0):
        self.naam = naam
        self.rekeningnummer = rekeningnummer
        self.bedrag = bedrag

    def __str__(self):
        return f"{self.naam}, {self.rekeningnummer}, bedrag: {self.bedrag}"

    def __repr__(self):
        return f"BankRekening('{self.naam}', '{self.rekeningnummer}', {self.bedrag})"

    def storten(self, n):
        self.bedrag += n

    def afhalen(self, n):
        self.bedrag -= n
