from pyld import jsonld
import codecs
import json
from pyshacl import validate

# read file
with open('dataset.json') as myfile:
    doc = json.load(myfile)

# read file
with open('ctx.json') as myfile:
    context = json.load(myfile)

# compact a document according to a particular context
# see: https://json-ld.org/spec/latest/json-ld/#compacted-document-form
expanded = jsonld.expand(doc,  {'expandContext': context})

with open('expanded.json', 'w') as f:
    json.dump(expanded,f,indent=2)

nquads = jsonld.normalize(
    expanded, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})
    
with codecs.open('nquads.nq', 'w', 'utf-8') as f:
   f.write(nquads)

with codecs.open('trace_model.shacl.ttl', 'r', 'utf-8') as f:
    model = f.read()

with codecs.open('trace_model.shacl.ttl', 'w', 'utf-8') as f:
    f.write(model)