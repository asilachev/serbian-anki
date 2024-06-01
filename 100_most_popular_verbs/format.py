import json

content = None
# TODO: Move source to params
with open('source.json') as f:
    content = f.read()

content_json = json.loads(content)
verbs = []
for v in content_json['verbs']:
    verbs.append(v['verb'])
u_verbs = list(set(verbs))
result = []
for v in content_json['verbs']:
    verb = v['verb']
    if verb in u_verbs:
        del u_verbs[u_verbs.index(verb)]
        result.append(v)

with open('source.json', 'w') as f:
    json.dump({'verbs': result}, f, ensure_ascii=False, indent=4)

result_anki = '#separator:pipe\n#html:true\n#tags column:5\n'
for r in result:
    ul_content = [f'<li>{c}</li>' for c in r['present_conjugation']]
    str = f'{r["verb"]}|{r["translation"]}|"<ul>{"".join(ul_content)}</ul>"|{r["example_sentence"]}'
    result_anki += f'{str}\n'

# TODO: Move output to params
with open('output.txt', 'w') as f:
    f.write(result_anki)

