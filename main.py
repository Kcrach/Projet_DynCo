from pyld import jsonld
import codecs
import json

# read file
with open('dataset.json') as myfile:
    doc = json.load(myfile)

# read file
with open('ctx.json') as myfile:
    context = json.load(myfile)

# compact a document according to a particular context
# see: https://json-ld.org/spec/latest/json-ld/#compacted-document-form
expanded = jsonld.expand(doc,  {'expandContext': context})

print(json.dumps(expanded, indent=2))

with open('expanded.json', 'w') as f:
    json.dump(expanded,f,indent=2)

nquads = jsonld.to_rdf(expanded, {'format' : 'application/n-quads'})

with codecs.open('nquads.nq', 'w', 'utf-8') as f:
    f.write(nquads)