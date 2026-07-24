# -*- coding: utf-8 -*-
"""
Compresse toute image d'un dossier (captures Unreal notamment) pour rester
sous une taille maximale (3 Mo par défaut).

Utilisation :
    python compress_screenshots.py "C:\\chemin\\vers\\Screenshots"
    python compress_screenshots.py "C:\\chemin\\vers\\Screenshots" --max-mb 3 --out "C:\\chemin\\sortie"

Stratégie, dans l'ordre, jusqu'à passer sous la limite :
  1. Ré-encode en JPEG qualité 95, diminue la qualité par paliers.
  2. Si la qualité minimale ne suffit pas, réduit la résolution (x0.85 à
     chaque passage) puis recommence à haute qualité.
Les fichiers déjà sous la limite sont recopiés tels quels (le PNG n'est
converti que si nécessaire, pour ne pas dégrader inutilement).
"""
import argparse
import shutil
import sys
from pathlib import Path

from PIL import Image

EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".tga"}


def compress_to_limit(src: Path, dst: Path, max_bytes: int) -> tuple[int, str]:
    if src.stat().st_size <= max_bytes and src.suffix.lower() in (".jpg", ".jpeg"):
        shutil.copy2(src, dst)
        return src.stat().st_size, "copié tel quel (déjà sous la limite)"

    img = Image.open(src).convert("RGB")  # JPEG n'a pas de canal alpha

    if src.stat().st_size <= max_bytes:
        # PNG déjà petit : on le garde en PNG, pas de perte inutile.
        img.save(dst.with_suffix(".png"), "PNG", optimize=True)
        size = dst.with_suffix(".png").stat().st_size
        if size <= max_bytes:
            return size, "recompressé en PNG optimisé"
        # Rare, mais si le PNG optimisé dépasse quand même : bascule JPEG.
        dst.with_suffix(".png").unlink(missing_ok=True)

    quality = 95
    scale = 1.0
    for _ in range(40):
        w, h = int(img.width * scale), int(img.height * scale)
        candidate = img.resize((w, h), Image.LANCZOS) if scale < 1.0 else img
        candidate.save(dst, "JPEG", quality=quality, optimize=True)
        size = dst.stat().st_size
        if size <= max_bytes:
            return size, f"JPEG q{quality} @ {w}x{h}"
        if quality > 40:
            quality -= 5
        else:
            scale *= 0.85
            quality = 85
    return dst.stat().st_size, "limite non atteinte après 40 tentatives"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("folder", help="Dossier contenant les captures (recherche récursive)")
    p.add_argument("--max-mb", type=float, default=3.0, help="Taille max par image en Mo (défaut 3)")
    p.add_argument("--out", default=None, help="Dossier de sortie (défaut : à côté, suffixe _compressed)")
    args = p.parse_args()

    src_dir = Path(args.folder)
    if not src_dir.is_dir():
        print(f"Dossier introuvable : {src_dir}")
        sys.exit(1)

    out_dir = Path(args.out) if args.out else src_dir.parent / f"{src_dir.name}_compressed"
    out_dir.mkdir(parents=True, exist_ok=True)
    max_bytes = int(args.max_mb * 1024 * 1024)

    files = [f for f in src_dir.rglob("*") if f.suffix.lower() in EXTS]
    if not files:
        print(f"Aucune image trouvée dans {src_dir}")
        return

    print(f"{len(files)} image(s) trouvée(s). Limite : {args.max_mb} Mo. Sortie : {out_dir}\n")
    for f in files:
        rel = f.relative_to(src_dir)
        dst = out_dir / rel.with_suffix(".jpg")
        dst.parent.mkdir(parents=True, exist_ok=True)
        before = f.stat().st_size
        size, note = compress_to_limit(f, dst, max_bytes)
        status = "OK" if size <= max_bytes else "AU-DESSUS"
        print(f"[{status}] {rel}  {before/1_048_576:.1f} Mo -> {size/1_048_576:.2f} Mo  ({note})")

    print(f"\nTerminé. Images compressées dans : {out_dir}")


if __name__ == "__main__":
    main()
