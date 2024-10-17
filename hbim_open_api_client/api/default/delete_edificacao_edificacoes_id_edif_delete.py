from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edificacao_public import EdificacaoPublic
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    id_edif: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/edificacoes/{id_edif}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EdificacaoPublic, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EdificacaoPublic.from_dict(response.json())

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
) -> Response[Union[EdificacaoPublic, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id_edif: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[EdificacaoPublic, HTTPValidationError]]:
    """Delete Edificacao

    Args:
        id_edif (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EdificacaoPublic, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id_edif=id_edif,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id_edif: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[EdificacaoPublic, HTTPValidationError]]:
    """Delete Edificacao

    Args:
        id_edif (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EdificacaoPublic, HTTPValidationError]
    """

    return sync_detailed(
        id_edif=id_edif,
        client=client,
    ).parsed


async def asyncio_detailed(
    id_edif: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[EdificacaoPublic, HTTPValidationError]]:
    """Delete Edificacao

    Args:
        id_edif (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EdificacaoPublic, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id_edif=id_edif,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id_edif: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[EdificacaoPublic, HTTPValidationError]]:
    """Delete Edificacao

    Args:
        id_edif (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EdificacaoPublic, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            id_edif=id_edif,
            client=client,
        )
    ).parsed
