from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.relacao_diagnostico_evento_public import RelacaoDiagnosticoEventoPublic
from ...models.relacao_diagnostico_evento_schema import RelacaoDiagnosticoEventoSchema
from ...types import Response


def _get_kwargs(
    id_relac_event: int,
    *,
    body: RelacaoDiagnosticoEventoSchema,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/relacao_eventos/{id_relac_event}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, RelacaoDiagnosticoEventoPublic]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RelacaoDiagnosticoEventoPublic.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RelacaoDiagnosticoEventoPublic]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id_relac_event: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RelacaoDiagnosticoEventoSchema,
) -> Response[Union[HTTPValidationError, RelacaoDiagnosticoEventoPublic]]:
    """Update Relacao Eventos

    Args:
        id_relac_event (int):
        body (RelacaoDiagnosticoEventoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RelacaoDiagnosticoEventoPublic]]
    """

    kwargs = _get_kwargs(
        id_relac_event=id_relac_event,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id_relac_event: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RelacaoDiagnosticoEventoSchema,
) -> Optional[Union[HTTPValidationError, RelacaoDiagnosticoEventoPublic]]:
    """Update Relacao Eventos

    Args:
        id_relac_event (int):
        body (RelacaoDiagnosticoEventoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, RelacaoDiagnosticoEventoPublic]
    """

    return sync_detailed(
        id_relac_event=id_relac_event,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id_relac_event: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RelacaoDiagnosticoEventoSchema,
) -> Response[Union[HTTPValidationError, RelacaoDiagnosticoEventoPublic]]:
    """Update Relacao Eventos

    Args:
        id_relac_event (int):
        body (RelacaoDiagnosticoEventoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RelacaoDiagnosticoEventoPublic]]
    """

    kwargs = _get_kwargs(
        id_relac_event=id_relac_event,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id_relac_event: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RelacaoDiagnosticoEventoSchema,
) -> Optional[Union[HTTPValidationError, RelacaoDiagnosticoEventoPublic]]:
    """Update Relacao Eventos

    Args:
        id_relac_event (int):
        body (RelacaoDiagnosticoEventoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, RelacaoDiagnosticoEventoPublic]
    """

    return (
        await asyncio_detailed(
            id_relac_event=id_relac_event,
            client=client,
            body=body,
        )
    ).parsed
