from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path

src = Path('C:/Users/bontl/Downloads/nas investments/images/optimized')
files = ['truck.jpeg', 'truck_2.jpeg', 'sedia_ceo.jpeg', 'tlb.jpeg']

out = src

for name in files:
    p = src / name
    if not p.exists():
        print('missing', p)
        continue
    with Image.open(p) as im:
        # ensure RGB
        im = im.convert('RGB')
        w, h = im.size
        target_ratio = 4/3
        # center crop to target ratio
        cur_ratio = w / h
        if cur_ratio > target_ratio:
            # too wide -> crop sides
            new_w = int(h * target_ratio)
            left = (w - new_w)//2
            im = im.crop((left, 0, left+new_w, h))
        else:
            # too tall -> crop top/bottom
            new_h = int(w / target_ratio)
            top = (h - new_h)//2
            im = im.crop((0, top, w, top+new_h))
        # resize to width 1200
        im = im.resize((1200, int(1200/target_ratio)), Image.LANCZOS)
        # auto contrast and slight brightness/contrast boost
        im = ImageOps.autocontrast(im, cutoff=1)
        enh = ImageEnhance.Brightness(im)
        im = enh.enhance(1.03)
        enhc = ImageEnhance.Contrast(im)
        im = enhc.enhance(1.06)
        # save back
        out_j = out / name
        out_w = out / (p.stem + '.webp')
        im.save(out_j, 'JPEG', quality=85, optimize=True)
        im.save(out_w, 'WEBP', quality=85)
        print('processed', out_j, out_w)
