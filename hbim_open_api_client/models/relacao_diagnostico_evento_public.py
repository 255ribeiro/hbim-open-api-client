from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RelacaoDiagnosticoEventoPublic")


@_attrs_define
class RelacaoDiagnosticoEventoPublic:
    """
    Attributes:
        id (int):
        id_evento (int):
        id_diagnostico (int):
        descricao (str):
    """

    id: int
    id_evento: int
    id_diagnostico: int
    descricao: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        id_evento = self.id_evento

        id_diagnostico = self.id_diagnostico

        descricao = self.descricao

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "id_evento": id_evento,
                "id_diagnostico": id_diagnostico,
                "descricao": descricao,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        id_evento = d.pop("id_evento")

        id_diagnostico = d.pop("id_diagnostico")

        descricao = d.pop("descricao")

        relacao_diagnostico_evento_public = cls(
            id=id,
            id_evento=id_evento,
            id_diagnostico=id_diagnostico,
            descricao=descricao,
        )

        relacao_diagnostico_evento_public.additional_properties = d
        return relacao_diagnostico_evento_public

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
