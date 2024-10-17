from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.geometria_public import GeometriaPublic


T = TypeVar("T", bound="GeometriaList")


@_attrs_define
class GeometriaList:
    """
    Attributes:
        geometrias_danos (List['GeometriaPublic']):
    """

    geometrias_danos: List["GeometriaPublic"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        geometrias_danos = []
        for geometrias_danos_item_data in self.geometrias_danos:
            geometrias_danos_item = geometrias_danos_item_data.to_dict()
            geometrias_danos.append(geometrias_danos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "geometrias_danos": geometrias_danos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.geometria_public import GeometriaPublic

        d = src_dict.copy()
        geometrias_danos = []
        _geometrias_danos = d.pop("geometrias_danos")
        for geometrias_danos_item_data in _geometrias_danos:
            geometrias_danos_item = GeometriaPublic.from_dict(geometrias_danos_item_data)

            geometrias_danos.append(geometrias_danos_item)

        geometria_list = cls(
            geometrias_danos=geometrias_danos,
        )

        geometria_list.additional_properties = d
        return geometria_list

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
