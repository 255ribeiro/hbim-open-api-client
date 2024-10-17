import datetime
from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import File

T = TypeVar("T", bound="CadastroSchema")


@_attrs_define
class CadastroSchema:
    """
    Attributes:
        id_user (int):
        data_cadastro (datetime.date):
        responsavel_tecnico (str):
        arquivo (File):
    """

    id_user: int
    data_cadastro: datetime.date
    responsavel_tecnico: str
    arquivo: File
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_user = self.id_user

        data_cadastro = self.data_cadastro.isoformat()

        responsavel_tecnico = self.responsavel_tecnico

        arquivo = self.arquivo.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_user": id_user,
                "data_cadastro": data_cadastro,
                "responsavel_tecnico": responsavel_tecnico,
                "arquivo": arquivo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id_user = d.pop("id_user")

        data_cadastro = isoparse(d.pop("data_cadastro")).date()

        responsavel_tecnico = d.pop("responsavel_tecnico")

        arquivo = File(payload=BytesIO(d.pop("arquivo")))

        cadastro_schema = cls(
            id_user=id_user,
            data_cadastro=data_cadastro,
            responsavel_tecnico=responsavel_tecnico,
            arquivo=arquivo,
        )

        cadastro_schema.additional_properties = d
        return cadastro_schema

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
