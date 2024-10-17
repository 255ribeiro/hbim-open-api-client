from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.tipo_dano_public import TipoDanoPublic
from ...models.tipo_dano_schema import TipoDanoSchema
from ...types import Response


def _get_kwargs(
    id_tipo: int,
    *,
    body: TipoDanoSchema,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/tipo_dano/{id_tipo}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, TipoDanoPublic]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TipoDanoPublic.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, TipoDanoPublic]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id_tipo: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TipoDanoSchema,
) -> Response[Union[HTTPValidationError, TipoDanoPublic]]:
    """Update Tipo Dano

    Args:
        id_tipo (int):
        body (TipoDanoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, TipoDanoPublic]]
    """

    kwargs = _get_kwargs(
        id_tipo=id_tipo,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id_tipo: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TipoDanoSchema,
) -> Optional[Union[HTTPValidationError, TipoDanoPublic]]:
    """Update Tipo Dano

    Args:
        id_tipo (int):
        body (TipoDanoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, TipoDanoPublic]
    """

    return sync_detailed(
        id_tipo=id_tipo,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id_tipo: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TipoDanoSchema,
) -> Response[Union[HTTPValidationError, TipoDanoPublic]]:
    """Update Tipo Dano

    Args:
        id_tipo (int):
        body (TipoDanoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, TipoDanoPublic]]
    """

    kwargs = _get_kwargs(
        id_tipo=id_tipo,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id_tipo: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TipoDanoSchema,
) -> Optional[Union[HTTPValidationError, TipoDanoPublic]]:
    """Update Tipo Dano

    Args:
        id_tipo (int):
        body (TipoDanoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, TipoDanoPublic]
    """

    return (
        await asyncio_detailed(
            id_tipo=id_tipo,
            client=client,
            body=body,
        )
    ).parsed
