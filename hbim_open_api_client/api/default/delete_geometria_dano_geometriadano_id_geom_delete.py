from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.geometria_public import GeometriaPublic
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    id_geom: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/geometriadano/{id_geom}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GeometriaPublic, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GeometriaPublic.from_dict(response.json())

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
) -> Response[Union[GeometriaPublic, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id_geom: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GeometriaPublic, HTTPValidationError]]:
    """Delete Geometria Dano

    Args:
        id_geom (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GeometriaPublic, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id_geom=id_geom,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id_geom: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GeometriaPublic, HTTPValidationError]]:
    """Delete Geometria Dano

    Args:
        id_geom (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GeometriaPublic, HTTPValidationError]
    """

    return sync_detailed(
        id_geom=id_geom,
        client=client,
    ).parsed


async def asyncio_detailed(
    id_geom: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GeometriaPublic, HTTPValidationError]]:
    """Delete Geometria Dano

    Args:
        id_geom (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GeometriaPublic, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id_geom=id_geom,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id_geom: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GeometriaPublic, HTTPValidationError]]:
    """Delete Geometria Dano

    Args:
        id_geom (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GeometriaPublic, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            id_geom=id_geom,
            client=client,
        )
    ).parsed
