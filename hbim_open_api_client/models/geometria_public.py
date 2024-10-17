from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

T = TypeVar("T", bound="GeometriaPublic")


@_attrs_define
class GeometriaPublic:
    """
    Attributes:
        id (int):
        nome (str):
        globalid_ifc (str):
        descricao (str):
        arquivo_geometria (File):
        localizacao (str):
    """

    id: int
    nome: str
    globalid_ifc: str
    descricao: str
    arquivo_geometria: File
    localizacao: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        nome = self.nome

        globalid_ifc = self.globalid_ifc

        descricao = self.descricao

        arquivo_geometria = self.arquivo_geometria.to_tuple()

        localizacao = self.localizacao

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nome": nome,
                "globalid_ifc": globalid_ifc,
                "descricao": descricao,
                "arquivo_geometria": arquivo_geometria,
                "localizacao": localizacao,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        nome = d.pop("nome")

        globalid_ifc = d.pop("globalid_ifc")

        descricao = d.pop("descricao")

        arquivo_geometria = File(payload=BytesIO(d.pop("arquivo_geometria")))

        localizacao = d.pop("localizacao")

        geometria_public = cls(
            id=id,
            nome=nome,
            globalid_ifc=globalid_ifc,
            descricao=descricao,
            arquivo_geometria=arquivo_geometria,
            localizacao=localizacao,
        )

        geometria_public.additional_properties = d
        return geometria_public

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
