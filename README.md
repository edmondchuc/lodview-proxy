# LodView Proxy

A simple FastAPI app to proxy requests to [lodview.it](https://lodview.it/) and serialize the results using Python's [RDFLib](https://github.com/RDFLib/rdflib).

Online service: https://lodview-proxy.deta.dev

Some responses from [lodview.it](https://lodview.it/) lose the base URI of the resource.

Example, have a look at this JSON-LD response for https://w3id.org/tern/ontologies/tern/Attribute.

```json
{
  "@graph": [
    {
      "@id": "_:b0",
      "@type": "http://www.w3.org/ns/shacl#PropertyShape",
      "http://www.w3.org/ns/shacl#maxCount": 1,
      "http://www.w3.org/ns/shacl#minCount": 1,
      "nodeKind": "http://www.w3.org/ns/shacl#IRI",
      "path": "isAttributeOf"
    },
    {
      "@id": "_:b1",
      "@type": "http://www.w3.org/ns/shacl#PropertyShape",
      "http://www.w3.org/ns/shacl#maxCount": 1,
      "http://www.w3.org/ns/shacl#minCount": 1,
      "name": "has simple value",
      "nodeKind": "http://www.w3.org/ns/shacl#IRIOrLiteral",
      "path": "hasSimpleValue"
    },
    {
      "@id": "_:b2",
      "@type": "owl:Restriction",
      "cardinality": "1",
      "onProperty": "hasValue"
    },
    {
      "@id": "_:b3",
      "@type": "http://www.w3.org/ns/shacl#PropertyShape",
      "class": "Value",
      "http://www.w3.org/ns/shacl#maxCount": 1,
      "http://www.w3.org/ns/shacl#minCount": 1,
      "name": "has value",
      "nodeKind": "http://www.w3.org/ns/shacl#IRI",
      "path": "hasValue"
    },
    {
      "@id": "_:b4",
      "@type": "http://www.w3.org/ns/shacl#PropertyShape",
      "http://www.w3.org/ns/shacl#maxCount": 1,
      "name": "type",
      "nodeKind": "http://www.w3.org/ns/shacl#IRI",
      "path": "dcterms:type"
    },
    {
      "@id": "_:b5",
      "@type": "http://www.w3.org/ns/shacl#PropertyShape",
      "http://www.w3.org/ns/shacl#maxCount": 1,
      "http://www.w3.org/ns/shacl#minCount": 1,
      "nodeKind": "http://www.w3.org/ns/shacl#IRI",
      "path": "attribute"
    },
    {
      "@id": "_:b6",
      "@type": "http://www.w3.org/ns/shacl#PropertyShape",
      "class": "RDFDataset",
      "http://www.w3.org/ns/shacl#maxCount": 1,
      "http://www.w3.org/ns/shacl#minCount": 1,
      "nodeKind": "http://www.w3.org/ns/shacl#IRI",
      "path": "void:inDataset"
    },
    {
      "@id": "_:b7",
      "@type": "owl:Restriction",
      "allValuesFrom": "Value",
      "onProperty": "hasValue"
    },
    {
      "@id": "./",
      "@type": [
        "owl:Class",
        "http://www.w3.org/ns/shacl#NodeShape"
      ],
      "label": "Attribute",
      "subClassOf": [
        "_:b2",
        "http://www.w3.org/ns/ssn/Property",
        "_:b7"
      ],
      "definition": "A key-value pair. Same design pattern as [schema:PropertyValue](https://schema.org/PropertyValue).",
      "property": [
        "_:b4",
        "_:b5",
        "_:b0",
        "_:b6",
        "_:b3",
        "_:b1"
      ]
    }
  ],
  "@context": {
    "nodeKind": {
      "@id": "http://www.w3.org/ns/shacl#nodeKind",
      "@type": "@id"
    },
    "path": {
      "@id": "http://www.w3.org/ns/shacl#path",
      "@type": "@id"
    },
    "minCount": {
      "@id": "http://www.w3.org/ns/shacl#minCount",
      "@type": "http://www.w3.org/2001/XMLSchema#integer"
    },
    "maxCount": {
      "@id": "http://www.w3.org/ns/shacl#maxCount",
      "@type": "http://www.w3.org/2001/XMLSchema#integer"
    },
    "name": {
      "@id": "http://www.w3.org/ns/shacl#name"
    },
    "onProperty": {
      "@id": "http://www.w3.org/2002/07/owl#onProperty",
      "@type": "@id"
    },
    "cardinality": {
      "@id": "http://www.w3.org/2002/07/owl#cardinality",
      "@type": "http://www.w3.org/2001/XMLSchema#nonNegativeInteger"
    },
    "class": {
      "@id": "http://www.w3.org/ns/shacl#class",
      "@type": "@id"
    },
    "label": {
      "@id": "http://www.w3.org/2000/01/rdf-schema#label"
    },
    "property": {
      "@id": "http://www.w3.org/ns/shacl#property",
      "@type": "@id"
    },
    "subClassOf": {
      "@id": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
      "@type": "@id"
    },
    "definition": {
      "@id": "http://www.w3.org/2004/02/skos/core#definition"
    },
    "allValuesFrom": {
      "@id": "http://www.w3.org/2002/07/owl#allValuesFrom",
      "@type": "@id"
    },
    "geonames": "http://www.geonames.org/ontology#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "bio": "http://purl.org/vocab/bio/0.1/",
    "schema-org": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "bag": "http://bag.basisregistraties.overheid.nl/def/bag#",
    "conf": "http://lodview.it/conf#",
    "metalex": "http://www.metalex.eu/metalex/2008-05-02#",
    "ocd": "http://dati.camera.it/ocd/",
    "rel": "http://purl.org/vocab/relationship/",
    "bne": "http://datos.bne.es/def/",
    "dcterms": "http://purl.org/dc/terms/",
    "dbpprop": "http://dbpedia.org/property/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "bbc": "http://www.bbc.co.uk/ontologies/",
    "void": "http://rdfs.org/ns/void#",
    "dbpedia-owl": "http://dbpedia.org/ontology/",
    "dbpedia": "http://dbpedia.org/resource/",
    "frbr": "http://purl.org/vocab/frbr/core#",
    "claros": "http://purl.org/NET/Claros/vocab#",
    "dwc": "http://rs.tdwg.org/dwc/terms/",
    "crm-owl": "http://purl.org/NET/crm-owl#",
    "meta": "http://example.org/metadata#",
    "bmuseum": "http://collection.britishmuseum.org/id/ontology/",
    "ods": "http://lod.xdams.org/ontologies/ods/",
    "linkedjazz": "http://linkedjazz.org/ontology/",
    "gml": "http://www.opengis.net/gml/",
    "muninn": "http://rdf.muninn-project.org/ontologies/documents#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "yago": "http://dbpedia.org/class/yago/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "units": "http://dbpedia.org/units/",
    "rso": "http://www.researchspace.org/ontology/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "oad": "http://lod.xdams.org/reload/oad/",
    "crm120111": "http://erlangen-crm.org/120111/",
    "cdoc": "http://www.cidoc-crm.org/cidoc-crm#",
    "bibleontology": "http://bibleontology.com/property#",
    "prov": "http://www.w3.org/ns/prov#",
    "crm": "http://erlangen-crm.org/current/",
    "cc": "http://creativecommons.org/ns#",
    "shoah": "http://dati.cdec.it/lod/shoah/",
    "npg": "http://ns.nature.com/terms/",
    "org": "http://www.w3.org/ns/org#",
    "gn": "http://www.geonames.org/ontology#",
    "ibc": "http://dati.ibc.it/ibc/",
    "aemetonto": "http://aemet.linkeddata.es/ontology/",
    "oreterms": "http://www.openarchives.org/ore/terms/",
    "skos-xl": "http://www.w3.org/2008/05/skos-xl#",
    "lgdo": "http://linkedgeodata.org/ontology/capital",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "eac-cpf": "http://archivi.ibc.regione.emilia-romagna.it/ontology/eac-cpf/",
    "bibo": "http://purl.org/ontology/bibo/",
    "time": "http://www.w3.org/2006/time#",
    "dc": "http://purl.org/dc/elements/1.1/",
    "prism21": "http://prismstandard.org/namespaces/basic/2.1/",
    "po": "http://purl.org/ontology/po/"
  }
}
```

The Turtle response is fine, however, they use `@base` which is not widely supported yet in RDF parsers and serializers.

```turtle
@base          <https://w3id.org/tern/ontologies/tern/Attribute> .
@prefix geonames: <http://www.geonames.org/ontology#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix bag:   <http://bag.basisregistraties.overheid.nl/def/bag#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix schema-org: <http://schema.org/> .
@prefix bio:   <http://purl.org/vocab/bio/0.1/> .
@prefix conf:  <http://lodview.it/conf#> .
@prefix metalex: <http://www.metalex.eu/metalex/2008-05-02#> .
@prefix ocd:   <http://dati.camera.it/ocd/> .
@prefix bne:   <http://datos.bne.es/def/> .
@prefix rel:   <http://purl.org/vocab/relationship/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dbpprop: <http://dbpedia.org/property/> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix bbc:   <http://www.bbc.co.uk/ontologies/> .
@prefix dbpedia-owl: <http://dbpedia.org/ontology/> .
@prefix void:  <http://rdfs.org/ns/void#> .
@prefix dbpedia: <http://dbpedia.org/resource/> .
@prefix frbr:  <http://purl.org/vocab/frbr/core#> .
@prefix dwc:   <http://rs.tdwg.org/dwc/terms/> .
@prefix claros: <http://purl.org/NET/Claros/vocab#> .
@prefix crm-owl: <http://purl.org/NET/crm-owl#> .
@prefix meta:  <http://example.org/metadata#> .
@prefix bmuseum: <http://collection.britishmuseum.org/id/ontology/> .
@prefix ods:   <http://lod.xdams.org/ontologies/ods/> .
@prefix linkedjazz: <http://linkedjazz.org/ontology/> .
@prefix muninn: <http://rdf.muninn-project.org/ontologies/documents#> .
@prefix gml:   <http://www.opengis.net/gml/> .
@prefix yago:  <http://dbpedia.org/class/yago/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix units: <http://dbpedia.org/units/> .
@prefix rso:   <http://www.researchspace.org/ontology/> .
@prefix geo:   <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix oad:   <http://lod.xdams.org/reload/oad/> .
@prefix crm120111: <http://erlangen-crm.org/120111/> .
@prefix cdoc:  <http://www.cidoc-crm.org/cidoc-crm#> .
@prefix prov:  <http://www.w3.org/ns/prov#> .
@prefix bibleontology: <http://bibleontology.com/property#> .
@prefix crm:   <http://erlangen-crm.org/current/> .
@prefix cc:    <http://creativecommons.org/ns#> .
@prefix npg:   <http://ns.nature.com/terms/> .
@prefix shoah: <http://dati.cdec.it/lod/shoah/> .
@prefix org:   <http://www.w3.org/ns/org#> .
@prefix gn:    <http://www.geonames.org/ontology#> .
@prefix ibc:   <http://dati.ibc.it/ibc/> .
@prefix aemetonto: <http://aemet.linkeddata.es/ontology/> .
@prefix skos-xl: <http://www.w3.org/2008/05/skos-xl#> .
@prefix oreterms: <http://www.openarchives.org/ore/terms/> .
@prefix lgdo:  <http://linkedgeodata.org/ontology/capital> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix eac-cpf: <http://archivi.ibc.regione.emilia-romagna.it/ontology/eac-cpf/> .
@prefix bibo:  <http://purl.org/ontology/bibo/> .
@prefix time:  <http://www.w3.org/2006/time#> .
@prefix po:    <http://purl.org/ontology/po/> .
@prefix prism21: <http://prismstandard.org/namespaces/basic/2.1/> .
@prefix dc:    <http://purl.org/dc/elements/1.1/> .

<>      a                owl:Class , <http://www.w3.org/ns/shacl#NodeShape> ;
        rdfs:label       "Attribute" ;
        rdfs:subClassOf  <http://www.w3.org/ns/ssn/Property> ;
        rdfs:subClassOf  [ a                owl:Restriction ;
                           owl:cardinality  "1"^^xsd:nonNegativeInteger ;
                           owl:onProperty   <hasValue>
                         ] ;
        rdfs:subClassOf  [ a                  owl:Restriction ;
                           owl:allValuesFrom  <Value> ;
                           owl:onProperty     <hasValue>
                         ] ;
        skos:definition  "A key-value pair. Same design pattern as [schema:PropertyValue](https://schema.org/PropertyValue)." ;
        <http://www.w3.org/ns/shacl#property>
                [ a       <http://www.w3.org/ns/shacl#PropertyShape> ;
                  <http://www.w3.org/ns/shacl#class>
                          <Value> ;
                  <http://www.w3.org/ns/shacl#maxCount>
                          1 ;
                  <http://www.w3.org/ns/shacl#minCount>
                          1 ;
                  <http://www.w3.org/ns/shacl#name>
                          "has value" ;
                  <http://www.w3.org/ns/shacl#nodeKind>
                          <http://www.w3.org/ns/shacl#IRI> ;
                  <http://www.w3.org/ns/shacl#path>
                          <hasValue>
                ] ;
        <http://www.w3.org/ns/shacl#property>
                [ a       <http://www.w3.org/ns/shacl#PropertyShape> ;
                  <http://www.w3.org/ns/shacl#maxCount>
                          1 ;
                  <http://www.w3.org/ns/shacl#minCount>
                          1 ;
                  <http://www.w3.org/ns/shacl#nodeKind>
                          <http://www.w3.org/ns/shacl#IRI> ;
                  <http://www.w3.org/ns/shacl#path>
                          <isAttributeOf>
                ] ;
        <http://www.w3.org/ns/shacl#property>
                [ a       <http://www.w3.org/ns/shacl#PropertyShape> ;
                  <http://www.w3.org/ns/shacl#maxCount>
                          1 ;
                  <http://www.w3.org/ns/shacl#minCount>
                          1 ;
                  <http://www.w3.org/ns/shacl#nodeKind>
                          <http://www.w3.org/ns/shacl#IRI> ;
                  <http://www.w3.org/ns/shacl#path>
                          <attribute>
                ] ;
        <http://www.w3.org/ns/shacl#property>
                [ a       <http://www.w3.org/ns/shacl#PropertyShape> ;
                  <http://www.w3.org/ns/shacl#maxCount>
                          1 ;
                  <http://www.w3.org/ns/shacl#name>
                          "type" ;
                  <http://www.w3.org/ns/shacl#nodeKind>
                          <http://www.w3.org/ns/shacl#IRI> ;
                  <http://www.w3.org/ns/shacl#path>
                          dcterms:type
                ] ;
        <http://www.w3.org/ns/shacl#property>
                [ a       <http://www.w3.org/ns/shacl#PropertyShape> ;
                  <http://www.w3.org/ns/shacl#class>
                          <RDFDataset> ;
                  <http://www.w3.org/ns/shacl#maxCount>
                          1 ;
                  <http://www.w3.org/ns/shacl#minCount>
                          1 ;
                  <http://www.w3.org/ns/shacl#nodeKind>
                          <http://www.w3.org/ns/shacl#IRI> ;
                  <http://www.w3.org/ns/shacl#path>
                          void:inDataset
                ] ;
        <http://www.w3.org/ns/shacl#property>
                [ a       <http://www.w3.org/ns/shacl#PropertyShape> ;
                  <http://www.w3.org/ns/shacl#maxCount>
                          1 ;
                  <http://www.w3.org/ns/shacl#minCount>
                          1 ;
                  <http://www.w3.org/ns/shacl#name>
                          "has simple value" ;
                  <http://www.w3.org/ns/shacl#nodeKind>
                          <http://www.w3.org/ns/shacl#IRIOrLiteral> ;
                  <http://www.w3.org/ns/shacl#path>
                          <hasSimpleValue>
                ] .

```