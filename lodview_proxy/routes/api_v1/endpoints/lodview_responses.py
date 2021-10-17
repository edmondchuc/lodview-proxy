turtle_example = """
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix void: <http://rdfs.org/ns/void#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/tern/ontologies/tern/MaterialSample> a rdfs:Class,
        sh:NodeShape ;
    rdfs:label "Material sample" ;
    rdfs:subClassOf [ a owl:Restriction ;
            owl:allValuesFrom <https://w3id.org/tern/ontologies/tern/Attribute> ;
            owl:onProperty <https://w3id.org/tern/ontologies/tern/hasAttribute> ],
        [ ],
        [ ],
        [ ],
        [ a owl:Restriction ;
            owl:allValuesFrom [ a owl:Class ;
                    owl:unionOf [ rdf:first <https://w3id.org/tern/ontologies/tern/Sampling> ;
                            rdf:rest [ ] ] ] ;
            owl:onProperty <http://www.w3.org/ns/sosa/isFeatureOfInterestOf> ],
        [ ],
        [ a owl:Restriction ;
            owl:allValuesFrom <https://w3id.org/tern/ontologies/loc/Geometry> ;
            owl:onProperty <http://www.opengis.net/ont/geosparql#hasGeometry> ],
        [ ],
        [ a owl:Restriction ;
            owl:allValuesFrom <https://w3id.org/tern/ontologies/tern/Sample> ;
            owl:onProperty <http://www.w3.org/ns/sosa/hasSample> ],
        [ a owl:Restriction ;
            owl:minCardinality "1"^^xsd:nonNegativeInteger ;
            owl:onProperty <http://www.w3.org/ns/sosa/isSampleOf> ],
        [ a owl:Restriction ;
            owl:allValuesFrom xsd:string ;
            owl:onProperty dcterms:identifier ],
        [ ],
        [ a owl:Restriction ;
            owl:allValuesFrom <https://w3id.org/tern/ontologies/tern/FeatureOfInterest> ;
            owl:onProperty <http://www.w3.org/ns/sosa/isSampleOf> ],
        [ ],
        [ ],
        [ ],
        [ ],
        [ a owl:Restriction ;
            owl:minCardinality "1"^^xsd:nonNegativeInteger ;
            owl:onProperty <http://www.w3.org/ns/sosa/isResultOf> ],
        [ a owl:Restriction ;
            owl:allValuesFrom <https://w3id.org/tern/ontologies/tern/Sampling> ;
            owl:onProperty <http://www.w3.org/ns/sosa/isResultOf> ],
        [ a owl:Restriction ;
            owl:cardinality "1"^^xsd:nonNegativeInteger ;
            owl:onProperty <https://w3id.org/tern/ontologies/tern/featureType> ],
        [ a owl:Restriction ;
            owl:cardinality "1"^^xsd:nonNegativeInteger ;
            owl:onProperty void:inDataset ],
        [ a owl:Restriction ;
            owl:maxCardinality "1"^^xsd:nonNegativeInteger ;
            owl:onProperty rdfs:comment ],
        [ ],
        [ a owl:Restriction ;
            owl:allValuesFrom <https://w3id.org/tern/ontologies/tern/RDFDataset> ;
            owl:onProperty void:inDataset ],
        dwc:MaterialSample,
        rdfs:Resource,
        <http://www.w3.org/ns/sosa/FeatureOfInterest>,
        <http://www.w3.org/ns/sosa/Sample>,
        <https://w3id.org/tern/ontologies/tern/FeatureOfInterest>,
        <https://w3id.org/tern/ontologies/tern/MaterialSample>,
        <https://w3id.org/tern/ontologies/tern/Result>,
        <https://w3id.org/tern/ontologies/tern/Sample>,
        <https://w3id.org/tern/ontologies/tern/Value> ;
    skos:definition "A physical result of a sampling (or subsampling) event. In biological collections, the material sample is typically collected, and either preserved or destructively processed." ;
    skos:example "A whole organism preserved in a collection. A part of an organism isolated for some purpose. A soil sample. A marine microbial sample." ;
    sh:property [ a sh:PropertyShape ;
            sh:path dwc:materialSampleID ] .

"""

json_ld_example = """
[
  {
    "@id": "https://w3id.org/tern/ontologies/tern/MaterialSample",
    "@type": [
      "http://www.w3.org/ns/shacl#NodeShape",
      "http://www.w3.org/2000/01/rdf-schema#Class"
    ],
    "http://www.w3.org/2000/01/rdf-schema#label": [
      {
        "@value": "Material sample"
      }
    ],
    "http://www.w3.org/2000/01/rdf-schema#subClassOf": [
      {
        "@id": "http://rs.tdwg.org/dwc/terms/MaterialSample"
      },
      {
        "@id": "https://w3id.org/tern/ontologies/tern/Result"
      },
      {
        "@id": "http://www.w3.org/2000/01/rdf-schema#Resource"
      },
      {
        "@id": "http://www.w3.org/ns/sosa/FeatureOfInterest"
      },
      {
        "@id": "https://w3id.org/tern/ontologies/tern/Sample"
      },
      {
        "@id": "https://w3id.org/tern/ontologies/tern/FeatureOfInterest"
      },
      {
        "@id": "https://w3id.org/tern/ontologies/tern/MaterialSample"
      },
      {
        "@id": "http://www.w3.org/ns/sosa/Sample"
      },
      {
        "@id": "https://w3id.org/tern/ontologies/tern/Value"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b1"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b2"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b3"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b4"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b5"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b6"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b7"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b8"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b9"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b10"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b11"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b12"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b13"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b14"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b15"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b16"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b17"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b18"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b22"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b23"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b24"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b25"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b26"
      },
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b27"
      }
    ],
    "http://www.w3.org/2004/02/skos/core#definition": [
      {
        "@value": "A physical result of a sampling (or subsampling) event. In biological collections, the material sample is typically collected, and either preserved or destructively processed."
      }
    ],
    "http://www.w3.org/2004/02/skos/core#example": [
      {
        "@value": "A whole organism preserved in a collection. A part of an organism isolated for some purpose. A soil sample. A marine microbial sample."
      }
    ],
    "http://www.w3.org/ns/shacl#property": [
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b28"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b1",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#maxCardinality": [
      {
        "@type": "http://www.w3.org/2001/XMLSchema#nonNegativeInteger",
        "@value": "1"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "http://www.w3.org/2000/01/rdf-schema#comment"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b2"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b3",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#allValuesFrom": [
      {
        "@id": "https://w3id.org/tern/ontologies/tern/FeatureOfInterest"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "http://www.w3.org/ns/sosa/isSampleOf"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b4"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b5"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b6",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#allValuesFrom": [
      {
        "@id": "https://w3id.org/tern/ontologies/tern/Sample"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "http://www.w3.org/ns/sosa/hasSample"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b7",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#allValuesFrom": [
      {
        "@id": "https://w3id.org/tern/ontologies/tern/RDFDataset"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "http://rdfs.org/ns/void#inDataset"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b8"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b9"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b10",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#allValuesFrom": [
      {
        "@id": "https://w3id.org/tern/ontologies/tern/Sampling"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "http://www.w3.org/ns/sosa/isResultOf"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b11",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#minCardinality": [
      {
        "@type": "http://www.w3.org/2001/XMLSchema#nonNegativeInteger",
        "@value": "1"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "http://www.w3.org/ns/sosa/isSampleOf"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b12",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#cardinality": [
      {
        "@type": "http://www.w3.org/2001/XMLSchema#nonNegativeInteger",
        "@value": "1"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "http://rdfs.org/ns/void#inDataset"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b13",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#allValuesFrom": [
      {
        "@id": "http://www.w3.org/2001/XMLSchema#string"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "http://purl.org/dc/terms/identifier"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b14",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#cardinality": [
      {
        "@type": "http://www.w3.org/2001/XMLSchema#nonNegativeInteger",
        "@value": "1"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "https://w3id.org/tern/ontologies/tern/featureType"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b15",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#allValuesFrom": [
      {
        "@id": "https://w3id.org/tern/ontologies/tern/Attribute"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "https://w3id.org/tern/ontologies/tern/hasAttribute"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b16"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b17"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b18",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#allValuesFrom": [
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b19"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "http://www.w3.org/ns/sosa/isFeatureOfInterestOf"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b19",
    "@type": [
      "http://www.w3.org/2002/07/owl#Class"
    ],
    "http://www.w3.org/2002/07/owl#unionOf": [
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b20"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b20",
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [
      {
        "@id": "https://w3id.org/tern/ontologies/tern/Sampling"
      }
    ],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [
      {
        "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b21"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b21"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b22"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b23",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#minCardinality": [
      {
        "@type": "http://www.w3.org/2001/XMLSchema#nonNegativeInteger",
        "@value": "1"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "http://www.w3.org/ns/sosa/isResultOf"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b24"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b25",
    "@type": [
      "http://www.w3.org/2002/07/owl#Restriction"
    ],
    "http://www.w3.org/2002/07/owl#allValuesFrom": [
      {
        "@id": "https://w3id.org/tern/ontologies/loc/Geometry"
      }
    ],
    "http://www.w3.org/2002/07/owl#onProperty": [
      {
        "@id": "http://www.opengis.net/ont/geosparql#hasGeometry"
      }
    ]
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b26"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b27"
  },
  {
    "@id": "_:n11556c946d87459e9b67dc0a6eebcac8b28",
    "@type": [
      "http://www.w3.org/ns/shacl#PropertyShape"
    ],
    "http://www.w3.org/ns/shacl#path": [
      {
        "@id": "http://rs.tdwg.org/dwc/terms/materialSampleID"
      }
    ]
  }
]
"""

responses = {
    200: {
        'content': {
            'text/turtle': {
                'example': turtle_example
            },
            'application/ld+json': {
                'example': json_ld_example
            }
        },
        'description': "Return the RDF serialization of a resource using Python's "
                       "[RDFLib](https://github.com/RDFLib/rdflib).",
    }
}
