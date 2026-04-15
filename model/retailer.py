from dataclasses import dataclass

@dataclass
class Retailer:
    Retailer_name: str
    Retailer_code: int
    Type: str
    Country: str

    def __eq__(self, other):
        return self.Retailer_code == other.Retailer_code

    def __hash__(self):
        return hash(self.Retailer_name)

    def __str__(self):
        return f"Nome retailer: {self.Retailer_name} - ({self.Retailer_code}); Country : {self.Country}; Tipologia: {self.Type}"  # più comodo e già pronto per dopo