import zipfile, re
from pathlib import Path
base = Path(r"c:/Users/ClaudiaAlvarezDiaz/Documents/EJIE/Repo OSAKIDETZA/Osakidetza/Context")
files = [
 base/'Notas reuniones'/'notas previas.docx',
 base/'Referencia aragón'/'GELPO - Rol Administrador - Manual usuario.docx',
 base/'Referencia aragón'/'Administración Catálogo Materiales.docx',
]
for f in files:
    print("\n" + "="*80)
    print(f"FILE: {f}")
    try:
        with zipfile.ZipFile(f) as z:
            xml = z.read('word/document.xml').decode('utf-8', errors='ignore')
        text = re.sub(r'<[^>]+>', ' ', xml)
        text = re.sub(r'\s+', ' ', text).strip()
        print(text[:12000])
    except Exception as e:
        print('ERROR:', e)
