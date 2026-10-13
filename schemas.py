from pydantic import BaseModel, Field
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str = Field(..., min_length=2, example="João Silva")
    email: str = Field(..., min_length=5, example="joao@email.com")
    senha: str = Field(..., min_length=4, example="senha123")
    ativo: Optional[bool] = True
    admin: Optional[bool] = False

    class Config:
        from_attributes = True

class PedidoSchema(BaseModel):
    id_usuario: Optional[int] = None

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True

class ItemPedidoSchema(BaseModel):
    quantidade: int = Field(..., gt=0, description="Quantidade deve ser maior que 0", example=2)
    sabor: str = Field(..., min_length=2, example="Calabresa")
    tamanho: str = Field(..., example="Grande")
    preco_unitario: float = Field(..., gt=0, description="Preço deve ser positivo", example=45.50)

    class Config:
        from_attributes = True
