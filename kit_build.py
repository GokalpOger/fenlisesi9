# Paket üretim yardımcısı. Kullanım: from kit_build import build, PALETTES
import os
HERE=os.path.dirname(os.path.abspath(__file__))
def build(cfg,out):
    t=open(os.path.join(HERE,'kit_template.html'),encoding='utf-8').read()
    for k,v in cfg.items(): t=t.replace('{{'+k+'}}',v)
    left=[l.strip()[:80] for l in t.split('\n') if '{{' in l]
    assert not left, 'Doldurulmamış yer tutucu: '+str(left[:3])
    open(out,'w',encoding='utf-8').write(t); print(out,len(t))
PALETTES={
 'mat':'',
 'fiz':'[data-theme="light"]{--navy:#9a3b00;--navy2:#d9540f;--sky:#ffe8d6;--gold:#1b4f9c;--gold2:#dce8ff}\n[data-theme="dark"]{--navy:#ffb37a;--navy2:#f07a2a;--sky:#4a2410;--gold:#8fb4ff;--gold2:#16264a}',
 'kim':'[data-theme="light"]{--navy:#14532d;--navy2:#1f8a4c;--sky:#dcf3e4;--gold:#b45309;--gold2:#fff1dc}\n[data-theme="dark"]{--navy:#8ee6b0;--navy2:#3fbf75;--sky:#12331f;--gold:#f5b35a;--gold2:#3a2610}',
 'biy':'[data-theme="light"]{--navy:#0f4c5c;--navy2:#0e8a9a;--sky:#d6f1f4;--gold:#b5541d;--gold2:#ffe9dc}\n[data-theme="dark"]{--navy:#8fdde8;--navy2:#2fb8c9;--sky:#0f3238;--gold:#f0a06a;--gold2:#3d2214}'}
