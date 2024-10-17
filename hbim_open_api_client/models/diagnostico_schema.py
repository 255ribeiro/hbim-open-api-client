from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

T = TypeVar("T", bound="DiagnosticoSchema")


@_attrs_define
class DiagnosticoSchema:
    """
    Attributes:
        nome (str):
        agente_dano (str):
        descricao_causa (str):
        relacao_elem_const (str):
        id_cadastro (int):
        id_tipo_dano (int):
        id_geometria (int):
        documento_referencia (File):
    """

    nome: str
    agente_dano: str
    descricao_causa: str
    relacao_elem_const: str
    id_cadastro: int
    id_tipo_dano: int
    id_geometria: int
    documento_referencia: File
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nome = self.nome

        agente_dano = self.agente_dano

        descricao_causa = self.descricao_causa

        relacao_elem_const = self.relacao_elem_const

        id_cadastro = self.id_cadastro

        id_tipo_dano = self.id_tipo_dano

        id_geometria = self.id_geometria

        documento_referencia = self.documento_referencia.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nome": nome,
                "agente_dano": agente_dano,
                "descricao_causa": descricao_causa,
                "relacao_elem_const": relacao_elem_const,
                "id_cadastro": id_cadastro,
                "id_tipo_dano": id_tipo_dano,
                "id_geometria": id_geometria,
                "documento_referencia": documento_referencia,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nome = d.pop("nome")

        agente_dano = d.pop("agente_dano")

        descricao_causa = d.pop("descricao_causa")

        relacao_elem_const = d.pop("relacao_elem_const")

        id_cadastro = d.pop("id_cadastro")

        id_tipo_dano = d.pop("id_tipo_dano")

        id_geometria = d.pop("id_geometria")

        documento_referencia = File(payload=BytesIO(d.pop("documento_referencia")))

        diagnostico_schema = cls(
            nome=nome,
            agente_dano=agente_dano,
            descricao_causa=descricao_causa,
            relacao_elem_const=relacao_elem_const,
            id_cadastro=id_cadastro,
            id_tipo_dano=id_tipo_dano,
            id_geometria=id_geometria,
            documento_referencia=documento_referencia,
        )

        diagnostico_schema.additional_properties = d
        return diagnostico_schema

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
