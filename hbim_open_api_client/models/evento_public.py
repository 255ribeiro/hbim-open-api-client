from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

T = TypeVar("T", bound="EventoPublic")


@_attrs_define
class EventoPublic:
    """
    Attributes:
        id (int):
        nome (str):
        descricao (str):
        data (str):
        documento_referencia (File):
    """

    id: int
    nome: str
    descricao: str
    data: str
    documento_referencia: File
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        nome = self.nome

        descricao = self.descricao

        data = self.data

        documento_referencia = self.documento_referencia.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nome": nome,
                "descricao": descricao,
                "data": data,
                "documento_referencia": documento_referencia,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        nome = d.pop("nome")

        descricao = d.pop("descricao")

        data = d.pop("data")

        documento_referencia = File(payload=BytesIO(d.pop("documento_referencia")))

        evento_public = cls(
            id=id,
            nome=nome,
            descricao=descricao,
            data=data,
            documento_referencia=documento_referencia,
        )

        evento_public.additional_properties = d
        return evento_public

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
