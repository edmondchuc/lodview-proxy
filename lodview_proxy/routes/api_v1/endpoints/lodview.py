import httpx
from fastapi import Response
from fastapi.routing import APIRouter
from rdflib import Graph, SH

from lodview_proxy import settings
from lodview_proxy.routes.api_v1.endpoints import lodview_responses

router = APIRouter()


mimetypes = {
    'text/turtle': 'turtle',
    'application/ld+json': 'json-ld',
}


@router.get('/lodview', responses=lodview_responses.responses)
async def lodview(IRI: str, sparql: str, output: str = 'text/turtle'):
    """Proxy requests to [lodview.it](https://lodview.it) and serialize the results using
    Python's [RDFLib](https://github.com/RDFLib/rdflib).

    Examples:

        - IRI: https://w3id.org/tern/ontologies/tern/MaterialSample
        - sparql: https://graphdb.tern.org.au/repositories/knowledge_graph_core?infer=false
        - output: text/turtle

    Note: `output` must be one of [`text/turtle`, `application/ld+json`].

    This will send to [lodview.it](https://lodview.it) as:
    ```
    https://lodview.it/lodview/?IRI=https://w3id.org/tern/ontologies/tern/MaterialSample&sparql=https://graphdb.tern.org.au/repositories/knowledge_graph_core?infer=false&output=text/turtle
    ```

    """
    async with httpx.AsyncClient() as client:
        client: httpx.AsyncClient
        params = {
            'IRI': IRI,
            'sparql': sparql,
            # Some rdflib serializers don't understand base.
            'output': 'text/turtle',
        }
        r = await client.get(settings.LODVIEW_PROXY_URL, params=params)
        r.raise_for_status()

        g = Graph()
        g.bind('sh', SH)
        g.parse(data=r.text, format='turtle')
        return Response(content=g.serialize(format=mimetypes[output]), media_type=output)
