from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tipo_dano_public import TipoDanoPublic


T = TypeVar("T", bound="TipoDanoList")


@_attrs_define
class TipoDanoList:
    """
    Attributes:
        tipos_danos (List['TipoDanoPublic']):
    """

    tipos_danos: List["TipoDanoPublic"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tipos_danos = []
        for tipos_danos_item_data in self.tipos_danos:
            tipos_danos_item = tipos_danos_item_data.to_dict()
            tipos_danos.append(tipos_danos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tipos_danos": tipos_danos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tipo_dano_public import TipoDanoPublic

        d = src_dict.copy()
        tipos_danos = []
        _tipos_danos = d.pop("tipos_danos")
        for tipos_danos_item_data in _tipos_danos:
            tipos_danos_item = TipoDanoPublic.from_dict(tipos_danos_item_data)

            tipos_danos.append(tipos_danos_item)

        tipo_dano_list = cls(
            tipos_danos=tipos_danos,
        )

        tipo_dano_list.additional_properties = d
        return tipo_dano_list

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
