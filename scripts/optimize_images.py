from PIL import Image
from pathlib import Path

src = Path('C:/Users/bontl/Downloads/nas investments/images')
out = src / 'optimized'
out.mkdir(exist_ok=True)

max_w = 1600
quality = 80

for p in src.glob('*.jp*g'):
    with Image.open(p) as im:
        w, h = im.size
        if w > max_w:
            new_h = int(max_w * h / w)
            im2 = im.resize((max_w, new_h), Image.LANCZOS)
        else:
            im2 = im.copy()
        # save optimized jpeg
        out_jpeg = out / p.name
        im2.save(out_jpeg, 'JPEG', quality=quality, optimize=True)
        # save webp
        out_webp = out / (p.stem + '.webp')
        im2.save(out_webp, 'WEBP', quality=quality)
        print('wrote', out_jpeg, out_webp)
