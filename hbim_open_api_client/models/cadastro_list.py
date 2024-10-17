from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cadastro_public import CadastroPublic


T = TypeVar("T", bound="CadastroList")


@_attrs_define
class CadastroList:
    """
    Attributes:
        cadastros (List['CadastroPublic']):
    """

    cadastros: List["CadastroPublic"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cadastros = []
        for cadastros_item_data in self.cadastros:
            cadastros_item = cadastros_item_data.to_dict()
            cadastros.append(cadastros_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cadastros": cadastros,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cadastro_public import CadastroPublic

        d = src_dict.copy()
        cadastros = []
        _cadastros = d.pop("cadastros")
        for cadastros_item_data in _cadastros:
            cadastros_item = CadastroPublic.from_dict(cadastros_item_data)

            cadastros.append(cadastros_item)

        cadastro_list = cls(
            cadastros=cadastros,
        )

        cadastro_list.additional_properties = d
        return cadastro_list

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
