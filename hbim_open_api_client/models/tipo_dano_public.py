from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TipoDanoPublic")


@_attrs_define
class TipoDanoPublic:
    """
    Attributes:
        id (int):
        nome (str):
        descricao (str):
    """

    id: int
    nome: str
    descricao: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        nome = self.nome

        descricao = self.descricao

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nome": nome,
                "descricao": descricao,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        nome = d.pop("nome")

        descricao = d.pop("descricao")

        tipo_dano_public = cls(
            id=id,
            nome=nome,
            descricao=descricao,
        )

        tipo_dano_public.additional_properties = d
        return tipo_dano_public

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
