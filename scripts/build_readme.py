#!/usr/bin/env python3
"""Generate the reading list and complete index from the supplied survey metadata."""
from pathlib import Path
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def clean(s):
    s = s.replace(r'\&', '&').replace(r'\_', '_').replace(r'\%', '%').replace(r'\#', '#')
    import unicodedata
    s = re.sub(r'\\(?:textit|textbf|emph|textsuperscript)\{([^{}]*)\}', r'\1', s)
    def accent(m):
        marks = {'"': '\u0308', "'": '\u0301', '`': '\u0300', '^': '\u0302', '~': '\u0303', '=': '\u0304'}
        return unicodedata.normalize('NFC', m[2] + marks[m[1]])
    s = re.sub(r"\\([\"'`^~=])\{?([A-Za-z])\}?", accent, s)
    s = s.replace('---', '—').replace('--', '–').replace('~', ' ')
    return s.replace('{', '').replace('}', '')

def escape(s):
    return clean(s).replace('[', r'\[').replace(']', r'\]').replace('|', r'\|')

def target(e):
    if e.get('url'): return e['url'].replace(' ', '%20')
    if e.get('doi'): return 'https://doi.org/' + e['doi']
    if e.get('eprint'): return 'https://arxiv.org/abs/' + e['eprint']
    return None

DESCRIPTIONS = {
    'introduction': 'Motivation, scope, and related surveys that frame trustworthy recursive self-improvement.',
    'foundations': 'Definitions and trustworthiness requirements, from persistent adaptation to recursive changes in the mechanism that produces future updates.',
    'validity': 'Whether measured gains are genuine, persist in successor systems, and survive changes to the improvement mechanism. Topics include collapse, forgetting, reward hacking, evaluator drift, and independent validation.',
    'behavior': 'Whether behavioral safeguards, human values, and fairness constraints remain effective as experience and accepted updates accumulate.',
    'system-security': 'How attacks, poisoned memories and artifacts, sensitive information, and inherited dependencies affect successors; safeguards for security, privacy, and data governance.',
    'governance': 'Evidence and interventions that keep evolving systems understandable, auditable, and subject to effective human direction.',
    'evaluation': 'Benchmarks, longitudinal testing, and independent evidence for jointly assessing improvement, constraint preservation, and oversight.',
    'outlook': 'Evidence bounds, applications, and open questions about transferring trustworthiness claims across tasks, versions, and recursive revisions.',
}
EMPTY = {
    'scope': 'The survey focuses on persistent updates and recursive revision of improvement mechanisms. Findings from neighboring LLM and agent research are relevant context, with their transfer limits kept explicit.',
    'contributions': 'The organizing contribution is an evidence-oriented view of improvement validity, constraint preservation, and effective oversight across successive revisions.',
    'organization': 'The reading path follows the eight survey chapters below, preserving the supplied section and subsection structure.',
    'rsi-trustworthiness': 'Assess trustworthiness at three levels: the accepted update, the systems that inherit it, and revisions to the mechanism governing future improvement.',
    'behavior-scope': 'Examine behavioral safety, alignment, and fairness across the improvement cycle and across successor systems.',
}

def main(check=False):
    entries = json.loads((ROOT / 'data/papers.json').read_text())
    sections = json.loads((ROOT / 'data/taxonomy.json').read_text())
    papers = {e['ID']: e for e in entries}
    cited = {p['id'] for s in sections for c in [s] + s['subsections'] for p in c['papers']}
    assert len(papers) == len(entries), 'Duplicate citation keys'
    assert cited <= papers.keys(), 'Unresolved taxonomy references'
    lines = ['<div align="center">', '', '# Trustworthy RSI', '',
        '### Trustworthy Recursive Self-Improvement in the Era of Large Models', '',
        '**Foundations, Risks, Evaluation, Applications, and Open Challenges**', '',
        '[![Literature](https://img.shields.io/badge/Literature-'+str(len(cited))+'_classified_%C2%B7_'+str(len(entries))+'_references-0F7C73)](docs/PAPER_INDEX.md)',
        '[![BibTeX](https://img.shields.io/badge/References-BibTeX-213C60)](bibliography/references.bib)',
        '[![Contributions](https://img.shields.io/badge/Contributions-welcome-6A5ACD)](CONTRIBUTING.md)', '',
        '[Survey Website](https://pujiayue.github.io/Trustworthy-RSI/) · [Reading List](#contents) · [Full Paper Index](docs/PAPER_INDEX.md) · [BibTeX](bibliography/references.bib) · [Contributing](CONTRIBUTING.md)', '',
        '</div>', '',
        '[![Trustworthy RSI: improvement validity, constraint preservation, and effective oversight](assets/overview.png)](assets/overview.pdf)', '',
        '> Trustworthy progress requires evidence that gains, safeguards, and human oversight remain effective across successive updates and recursive revisions.', '',
        'Large-model systems increasingly turn experience into persistent changes to models, memories, tools, and workflows. Recursive self-improvement (RSI) extends this process to the mechanisms that generate, evaluate, and implement subsequent changes. This repository accompanies our survey and organizes literature through a **validity–risk–oversight** perspective.', '',
        'We examine four connected themes: **genuine and sustained improvement**; **behavior, alignment, and fairness**; **security, privacy, and data governance**; and **transparency and control**. The taxonomy follows the survey rather than grouping papers only by the component being optimized.', '',
        f'The reading list contains **{len(cited)} distinct references** across eight chapters. The [complete index](docs/PAPER_INDEX.md) and [BibTeX library](bibliography/references.bib) contain **{len(entries)} references** supplied with the survey; '+str(len(entries)-len(cited))+' have no placement in the supplied taxonomy. Papers may appear in multiple subsections.', '',
        '<details>', '<summary>Visual abstract: toward trustworthy RSI</summary>', '', '![Toward trustworthy RSI: validity, constraint preservation, and oversight across successive revisions](assets/visual-abstract.png)', '', '</details>', '', '## Contents', '', '- [Scope & Process Framework](#scope-and-process-framework)']
    for n,s in enumerate(sections,1):
        lines += [f'- [{n}. {s["title"]}](#{s["id"]})']
        lines += [f'  - [{n}.{i} {c["title"]}](#{c["id"]})' for i,c in enumerate(s['subsections'],1)]
    lines += ['- [Resources & Maintenance](#resources-and-maintenance)', '', '<a id="scope-and-process-framework"></a>', '## Scope & Process Framework', '',
        '**Persistent self-improvement** retains changes for future use. **Recursive self-improvement** additionally revises the mechanism that produces subsequent updates. A higher task score or a self-referential design alone does not establish sustained or trustworthy improvement.', '',
        '| Process | Question |', '| :-- | :-- |',
        '| **S1 · Improvement diagnosis** | What limitation should the next revision address? |',
        '| **S2 · Proposal generation** | Which changes should be proposed? |',
        '| **S3 · Proposal evaluation** | Which changes meet the acceptance criteria? |',
        '| **S4 · Update implementation** | How are accepted changes retained in the successor system? |',
        '| **RI · Recursive improvement** | What changes when S1–S4 revise the update mechanism itself? |', '',
        'The four themes are assessed at the **update**, **successor**, and **meta-improvement** levels. Listed works include direct RSI studies, related self-evolving systems, and enabling foundations; placement in the taxonomy does not imply that a paper demonstrates open-ended RSI or validates a safeguard across all levels.', '']
    def bullet(p):
        e = papers[p['id']]
        title = escape(e['title']); label = escape(p['label']); url = target(e)
        linked = f'[{title}]({url})' if url else f'**{title}**'
        tag = f'**{label}** — ' if clean(p['label']).casefold() != clean(e['title']).casefold() else ''
        venue = clean(e.get('booktitle') or e.get('journal') or '')
        # Keep entries compact; the complete index carries all supplied publication metadata.
        if 'arxiv' in venue.lower(): venue = 'arXiv'
        meta = str(e['year']) + (f' · {escape(venue)}' if venue and len(venue)<65 else '')
        return f'- {tag}{linked}. *{meta}* · [Reference](docs/PAPER_INDEX.md#{e["ID"].lower()})'
    for n,s in enumerate(sections,1):
        lines += [f'<a id="{s["id"]}"></a>', f'## {n}. {s["title"]}', '', DESCRIPTIONS[s['id']], '']
        lines += [bullet(p) for p in s['papers']]
        if s['papers']: lines += ['']
        for i,c in enumerate(s['subsections'],1):
            lines += [f'<a id="{c["id"]}"></a>', f'### {n}.{i} {c["title"]}', '']
            if c['papers']: lines += [bullet(p) for p in c['papers']] + ['']
            else: lines += [EMPTY.get(c['id'], 'This subsection identifies evidence limits and remaining research questions. The supplied classification tree assigns no individual references here.'), '']
        lines += ['[↑ Contents](#contents)', '']
    lines += ['<a id="resources-and-maintenance"></a>', '## Resources & Maintenance', '',
        '- [Full paper index](docs/PAPER_INDEX.md): titles, authors, supplied publication metadata, citation keys, and taxonomy placement.',
        '- [BibTeX library](bibliography/references.bib): the complete survey bibliography, excluding two template-testing entries.',
        '- [Machine-readable literature](data/papers.json) and [taxonomy](data/taxonomy.json).',
        '- [Contribution guide](CONTRIBUTING.md): propose a paper, fix metadata, or refine a taxonomy placement.',
        '- [Repository provenance](docs/PROVENANCE.md): source materials, figure selection, and verification boundaries.', '',
        'To regenerate the list and index after updating the JSON sources:', '', '```bash', 'python3 scripts/build_readme.py', 'python3 scripts/validate.py', '```', '',
        'Reference metadata follows the supplied survey bibliography and has not been independently audited paper by paper. The repository does not assign evidence-strength labels to individual papers. Corrections and precise source links are welcome.', '',
        '### Acknowledgments', '',
        'The repository presentation is inspired by [Awesome RSI](https://github.com/lobehub/awesome-rsi): an overview figure, navigable topic hierarchy, and linked literature list. The taxonomy and bibliography here come from our survey materials.', '']
    index = ['# Complete Reference Index', '', '[← Reading list](../README.md) · [BibTeX library](../bibliography/references.bib)', '',
        f'{len(entries)} references; {len(cited)} appear in the supplied taxonomy and {len(entries)-len(cited)} are additional bibliography entries. Publication metadata is reproduced from the supplied bibliography; classification is organizational rather than an evidence rating.', '',
        '## Classified References', '']
    memberships = {}
    for n,s in enumerate(sections,1):
        for i,c in enumerate([s]+s['subsections']):
            number = str(n) if i == 0 else f'{n}.{i}'
            for p in c['papers']: memberships.setdefault(p['id'], []).append(f'[{number} {c["title"]}](../README.md#{c["id"]})')
    def record(e):
        url=target(e)
        title=escape(e['title'])
        result=[f'<a id="{e["ID"].lower()}"></a>', f'### {title}', '',
            f'- **Citation key:** `{e["ID"]}`', f'- **Authors:** {escape(e["author"])}', f'- **Year:** {e["year"]}']
        for field,label in [('booktitle','Venue'),('journal','Publication'),('publisher','Publisher'),('doi','DOI'),('eprint','arXiv')]:
            if e.get(field):result.append(f'- **{label}:** {escape(e[field])}')
        if url:result.append(f'- **Source:** [{url}]({url})')
        result.append('- **Taxonomy:** '+('; '.join(memberships[e['ID']]) if e['ID'] in memberships else 'Not placed in the supplied classification tree.'))
        return result+['']
    ordering=lambda e:(-int(e['year']),clean(e['title']).casefold())
    for e in sorted((p for p in entries if p['ID'] in cited),key=ordering):index+=record(e)
    index += ['## Additional Bibliography Entries', '', 'These references are retained from the supplied bibliography without inventing a taxonomy placement.', '']
    for e in sorted((p for p in entries if p['ID'] not in cited),key=ordering):index+=record(e)
    outputs={ROOT/'README.md':'\n'.join(lines),ROOT/'docs/PAPER_INDEX.md':'\n'.join(index)}
    for path,content in outputs.items():
        if check:
            if not path.exists() or path.read_text()!=content:
                raise SystemExit(f'Generated file is out of date: {path.relative_to(ROOT)}')
        else:path.write_text(content)
    print(f'{"Checked" if check else "Generated"} README and index: {len(cited)} classified / {len(entries)} total references.')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true')
    main(parser.parse_args().check)
