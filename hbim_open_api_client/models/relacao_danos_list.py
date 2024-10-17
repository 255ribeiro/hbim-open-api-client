from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.relacao_danos_public import RelacaoDanosPublic


T = TypeVar("T", bound="RelacaoDanosList")


@_attrs_define
class RelacaoDanosList:
    """
    Attributes:
        relacao_danos (List['RelacaoDanosPublic']):
    """

    relacao_danos: List["RelacaoDanosPublic"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        relacao_danos = []
        for relacao_danos_item_data in self.relacao_danos:
            relacao_danos_item = relacao_danos_item_data.to_dict()
            relacao_danos.append(relacao_danos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relacao_danos": relacao_danos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.relacao_danos_public import RelacaoDanosPublic

        d = src_dict.copy()
        relacao_danos = []
        _relacao_danos = d.pop("relacao_danos")
        for relacao_danos_item_data in _relacao_danos:
            relacao_danos_item = RelacaoDanosPublic.from_dict(relacao_danos_item_data)

            relacao_danos.append(relacao_danos_item)

        relacao_danos_list = cls(
            relacao_danos=relacao_danos,
        )

        relacao_danos_list.additional_properties = d
        return relacao_danos_list

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
