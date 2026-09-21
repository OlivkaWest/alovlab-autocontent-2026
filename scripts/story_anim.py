# -*- coding: utf-8 -*-
"""AlovLab · сборка анимированных клипов B-roll для HeyGen из кадров-кейфреймов.
Кросс-фейд между кадрами (позиции стабильны → чистое появление). Выход: WebM (VP8) + GIF-фолбэк.
ffmpeg — из playwright-сборки (только VP8). Запуск: python3 scripts/story_anim.py"""
import subprocess, pathlib, io
from PIL import Image

FF = "/opt/pw-browsers/ffmpeg-1011/ffmpeg-linux"
D = pathlib.Path("exports/heygen-broll/stories-course")

def build(keyframes, out_base, holds, fades, final_hold, fps=30):
    imgs = [Image.open(D / k).convert("RGB") for k in keyframes]
    seq = []
    for i in range(len(imgs)):
        h = final_hold if i == len(imgs) - 1 else holds[i]
        seq += [imgs[i]] * h
        if i < len(imgs) - 1:
            for t in range(1, fades[i] + 1):
                seq.append(Image.blend(imgs[i], imgs[i + 1], t / (fades[i] + 1)))
    # pipe JPEG frames -> ffmpeg (playwright build reads only mjpeg via image2pipe)
    webm = D / f"{out_base}.webm"
    proc = subprocess.Popen([FF, "-y", "-f", "image2pipe", "-vcodec", "mjpeg", "-r", str(fps),
                             "-i", "pipe:0", "-c:v", "libvpx", "-b:v", "3M", "-auto-alt-ref", "0",
                             "-pix_fmt", "yuv420p", str(webm)], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    for fr in seq:
        buf = io.BytesIO(); fr.save(buf, "JPEG", quality=93); proc.stdin.write(buf.getvalue())
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("ffmpeg webm encode failed")
    gif = D / f"{out_base}.gif"
    step = max(1, fps // 15)
    gf = [seq[i].resize((540, 960)) for i in range(0, len(seq), step)]
    gf[0].save(gif, save_all=True, append_images=gf[1:], duration=int(1000 / 15), loop=0, optimize=True)
    print(f"{out_base}: webm {webm.stat().st_size//1024}KB · gif {gif.stat().st_size//1024}KB · {len(seq)} кадров / {len(seq)/fps:.1f}с")

if __name__ == "__main__":
    # Сцена 3 · путь новичка: шаги появляются по одному
    build(["scene3-step-1.png", "scene3-step-2.png", "scene3-step-3.png"], "scene3-animated",
          holds=[30, 26], fades=[14, 14], final_hold=70)
