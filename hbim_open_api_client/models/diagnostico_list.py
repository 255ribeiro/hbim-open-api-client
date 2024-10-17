from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.diagnostico_public import DiagnosticoPublic


T = TypeVar("T", bound="DiagnosticoList")


@_attrs_define
class DiagnosticoList:
    """
    Attributes:
        diagnosticos (List['DiagnosticoPublic']):
    """

    diagnosticos: List["DiagnosticoPublic"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        diagnosticos = []
        for diagnosticos_item_data in self.diagnosticos:
            diagnosticos_item = diagnosticos_item_data.to_dict()
            diagnosticos.append(diagnosticos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "diagnosticos": diagnosticos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.diagnostico_public import DiagnosticoPublic

        d = src_dict.copy()
        diagnosticos = []
        _diagnosticos = d.pop("diagnosticos")
        for diagnosticos_item_data in _diagnosticos:
            diagnosticos_item = DiagnosticoPublic.from_dict(diagnosticos_item_data)

            diagnosticos.append(diagnosticos_item)

        diagnostico_list = cls(
            diagnosticos=diagnosticos,
        )

        diagnostico_list.additional_properties = d
        return diagnostico_list

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
