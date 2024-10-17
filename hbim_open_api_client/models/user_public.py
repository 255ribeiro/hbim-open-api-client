import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="UserPublic")


@_attrs_define
class UserPublic:
    """
    Attributes:
        id (int):
        username (str):
        nome (str):
        email (str):
        formacao_academica (str):
        data_nascimento (datetime.date):
    """

    id: int
    username: str
    nome: str
    email: str
    formacao_academica: str
    data_nascimento: datetime.date
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        username = self.username

        nome = self.nome

        email = self.email

        formacao_academica = self.formacao_academica

        data_nascimento = self.data_nascimento.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "nome": nome,
                "email": email,
                "formacao_academica": formacao_academica,
                "data_nascimento": data_nascimento,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        username = d.pop("username")

        nome = d.pop("nome")

        email = d.pop("email")

        formacao_academica = d.pop("formacao_academica")

        data_nascimento = isoparse(d.pop("data_nascimento")).date()

        user_public = cls(
            id=id,
            username=username,
            nome=nome,
            email=email,
            formacao_academica=formacao_academica,
            data_nascimento=data_nascimento,
        )

        user_public.additional_properties = d
        return user_public

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
