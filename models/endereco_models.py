from db import db

class Endereco(db.Model):
    __tablename__ = 'enderecos'

    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(9), nullable=False)
    logradouro = db.Column(db.String(100), nullable=False)
    complemento = db.Column(db.String(100))
    unidade = db.Column(db.String(20))
    bairro = db.Column(db.String(100), nullable=False)
    localidade = db.Column(db.String(100), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    regiao = db.Column(db.String(50), nullable=False)
    ibge = db.Column(db.String(10), nullable=False)
    gia = db.Column(db.String(10))
    ddd = db.Column(db.String(3), nullable=False)
    siafi = db.Column(db.String(10))

    def json(self):
        return {
            'id': self.id,           
            'cep': self.cep,
            'logradouro': self.logradouro,
            'complemento': self.complemento,
            'unidade': self.unidade,
            'bairro': self.bairro,
            'localidade': self.localidade,
            'uf': self.uf,
            'estado': self.estado,
            'regiao': self.regiao,
            'ibge': self.ibge,
            'gia': self.gia,
            'ddd': self.ddd,
            'siafi': self.siafi
}

