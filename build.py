from pathlib import Path
import base64, gzip, io, json, shutil, subprocess, sys, tarfile
root=Path(__file__).parent
src=root/'src'; dist=root/'dist'
parts_dir=root/'public-source'/'parts'
ordered=['00.txt','01.txt','02.txt','03.txt','04.txt','05a.txt','05b.txt','06a.txt','06b.txt']
if parts_dir.exists():
    payload=''.join((parts_dir/name).read_text(encoding='ascii') for name in ordered)
    raw=base64.b64decode(payload)
    shutil.rmtree(src,ignore_errors=True)
    with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tf:
        for member in tf.getmembers():
            target=(root/member.name).resolve()
            if root.resolve() not in target.parents and target != root.resolve():
                raise SystemExit('Unsafe source archive member')
        tf.extractall(root)
    print('Restored sanitized investor source archive')
private_menu=root/'private-data'/'menu.internal.json'
if private_menu.exists() and (root/'tools'/'generate_public_data.py').exists():
    subprocess.run([sys.executable,str(root/'tools'/'generate_public_data.py')],check=True)
public_menu=src/'data'/'menu.public.json'
if (src/'downloads').exists(): raise SystemExit('Build blocked: src/downloads exists')
public=json.loads(public_menu.read_text(encoding='utf-8'))
assert len(public['days'])==14 and len(public['meals'])==70 and all(len(d['meals'])==5 for d in public['days'])
text=public_menu.read_text(encoding='utf-8')
for token in ['ingredient_cost_','price_retail_byn_kg','price_small_business_byn_kg','price_wholesale_byn_kg','cost_small_business_byn']:
    if token in text: raise SystemExit(f'Build blocked: internal field {token} in public menu')
shutil.rmtree(dist,ignore_errors=True); shutil.copytree(src,dist)
(dist/'.nojekyll').write_text('',encoding='utf-8'); (dist/'robots.txt').write_text('User-agent: *\nDisallow: /\n',encoding='utf-8')
assert not any(p.suffix.lower() in {'.pdf','.xlsx'} for p in dist.rglob('*') if p.is_file())
for p in dist.rglob('*.html'): assert 'downloads/' not in p.read_text(encoding='utf-8')
print('Investor build OK:',dist)
