from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RelacaoDanosPublic")


@_attrs_define
class RelacaoDanosPublic:
    """
    Attributes:
        id (int):
        causa_id_diagnostico (int):
        consequencia_id_diagnostico (int):
        descricao (str):
    """

    id: int
    causa_id_diagnostico: int
    consequencia_id_diagnostico: int
    descricao: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        causa_id_diagnostico = self.causa_id_diagnostico

        consequencia_id_diagnostico = self.consequencia_id_diagnostico

        descricao = self.descricao

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "causa_id_diagnostico": causa_id_diagnostico,
                "consequencia_id_diagnostico": consequencia_id_diagnostico,
                "descricao": descricao,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        causa_id_diagnostico = d.pop("causa_id_diagnostico")

        consequencia_id_diagnostico = d.pop("consequencia_id_diagnostico")

        descricao = d.pop("descricao")

        relacao_danos_public = cls(
            id=id,
            causa_id_diagnostico=causa_id_diagnostico,
            consequencia_id_diagnostico=consequencia_id_diagnostico,
            descricao=descricao,
        )

        relacao_danos_public.additional_properties = d
        return relacao_danos_public

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
