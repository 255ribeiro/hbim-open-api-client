import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="EdificacaoPublic")


@_attrs_define
class EdificacaoPublic:
    """
    Attributes:
        id (int):
        nome (str):
        descricao_historica (str):
        data_construcao (datetime.date):
        valor_patrimonial (str):
    """

    id: int
    nome: str
    descricao_historica: str
    data_construcao: datetime.date
    valor_patrimonial: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        nome = self.nome

        descricao_historica = self.descricao_historica

        data_construcao = self.data_construcao.isoformat()

        valor_patrimonial = self.valor_patrimonial

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nome": nome,
                "descricao_historica": descricao_historica,
                "data_construcao": data_construcao,
                "valor_patrimonial": valor_patrimonial,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        nome = d.pop("nome")

        descricao_historica = d.pop("descricao_historica")

        data_construcao = isoparse(d.pop("data_construcao")).date()

        valor_patrimonial = d.pop("valor_patrimonial")

        edificacao_public = cls(
            id=id,
            nome=nome,
            descricao_historica=descricao_historica,
            data_construcao=data_construcao,
            valor_patrimonial=valor_patrimonial,
        )

        edificacao_public.additional_properties = d
        return edificacao_public

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
