from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.relacao_diagnostico_evento_public import RelacaoDiagnosticoEventoPublic


T = TypeVar("T", bound="RelacaoDiagnosticoEventoList")


@_attrs_define
class RelacaoDiagnosticoEventoList:
    """
    Attributes:
        relacoes_diag_eventos (List['RelacaoDiagnosticoEventoPublic']):
    """

    relacoes_diag_eventos: List["RelacaoDiagnosticoEventoPublic"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        relacoes_diag_eventos = []
        for relacoes_diag_eventos_item_data in self.relacoes_diag_eventos:
            relacoes_diag_eventos_item = relacoes_diag_eventos_item_data.to_dict()
            relacoes_diag_eventos.append(relacoes_diag_eventos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relacoes_diag_eventos": relacoes_diag_eventos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.relacao_diagnostico_evento_public import RelacaoDiagnosticoEventoPublic

        d = src_dict.copy()
        relacoes_diag_eventos = []
        _relacoes_diag_eventos = d.pop("relacoes_diag_eventos")
        for relacoes_diag_eventos_item_data in _relacoes_diag_eventos:
            relacoes_diag_eventos_item = RelacaoDiagnosticoEventoPublic.from_dict(relacoes_diag_eventos_item_data)

            relacoes_diag_eventos.append(relacoes_diag_eventos_item)

        relacao_diagnostico_evento_list = cls(
            relacoes_diag_eventos=relacoes_diag_eventos,
        )

        relacao_diagnostico_evento_list.additional_properties = d
        return relacao_diagnostico_evento_list

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
