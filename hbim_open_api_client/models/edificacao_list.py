from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.edificacao_public import EdificacaoPublic


T = TypeVar("T", bound="EdificacaoList")


@_attrs_define
class EdificacaoList:
    """
    Attributes:
        edificacoes (List['EdificacaoPublic']):
    """

    edificacoes: List["EdificacaoPublic"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edificacoes = []
        for edificacoes_item_data in self.edificacoes:
            edificacoes_item = edificacoes_item_data.to_dict()
            edificacoes.append(edificacoes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edificacoes": edificacoes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.edificacao_public import EdificacaoPublic

        d = src_dict.copy()
        edificacoes = []
        _edificacoes = d.pop("edificacoes")
        for edificacoes_item_data in _edificacoes:
            edificacoes_item = EdificacaoPublic.from_dict(edificacoes_item_data)

            edificacoes.append(edificacoes_item)

        edificacao_list = cls(
            edificacoes=edificacoes,
        )

        edificacao_list.additional_properties = d
        return edificacao_list

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
