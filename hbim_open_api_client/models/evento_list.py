from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.evento_public import EventoPublic


T = TypeVar("T", bound="EventoList")


@_attrs_define
class EventoList:
    """
    Attributes:
        eventos (List['EventoPublic']):
    """

    eventos: List["EventoPublic"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eventos = []
        for eventos_item_data in self.eventos:
            eventos_item = eventos_item_data.to_dict()
            eventos.append(eventos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventos": eventos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.evento_public import EventoPublic

        d = src_dict.copy()
        eventos = []
        _eventos = d.pop("eventos")
        for eventos_item_data in _eventos:
            eventos_item = EventoPublic.from_dict(eventos_item_data)

            eventos.append(eventos_item)

        evento_list = cls(
            eventos=eventos,
        )

        evento_list.additional_properties = d
        return evento_list

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
