import { describe, it, expect } from "vitest";
import {
  buildAssembleArgs,
  buildConcatArgs,
  buildScaleArgs,
  assertSafeArg,
  OUT_WIDTH,
  OUT_HEIGHT,
} from "../src/video/ffmpeg";
import { buildGrokPayload } from "../src/grok/payload";
import { GrokError } from "../src/grok/errors";

describe("FFmpeg command builders", () => {
  it("scale приводит к 9:16 без обрезки", () => {
    const args = buildScaleArgs("in.mp4", "out.mp4");
    expect(args).toContain("-i");
    expect(args.join(" ")).toContain(`${OUT_WIDTH}:${OUT_HEIGHT}`);
    expect(args.join(" ")).toContain("force_original_aspect_ratio=decrease");
  });

  it("assemble мапит видео и вшивает субтитры из файла", () => {
    const args = buildAssembleArgs({ videoInput: "v.mp4", voiceInput: "a.mp4", subtitleFile: "s.srt", output: "o.mp4", burnSubtitles: true });
    expect(args).toContain("-filter_complex");
    expect(args.join(" ")).toContain("subtitles=");
    expect(args[args.length - 1]).toBe("o.mp4");
  });

  it("музыка приглушается под голосом", () => {
    const args = buildAssembleArgs({ videoInput: "v.mp4", voiceInput: "a.mp4", musicInput: "m.mp3", output: "o.mp4", burnSubtitles: false });
    expect(args.join(" ")).toContain("amix");
    expect(args.join(" ")).toContain("volume=0.18");
  });
});

describe("защита от shell injection", () => {
  it("аргументы — массив, опасная строка остаётся ОДНИМ элементом (без shell)", () => {
    const evil = "/tmp/a;rm-rf-slash.mp4"; // без пробелов — валидный путь
    const args = buildConcatArgs("list.txt", evil);
    // Опасная строка не разбивается и не интерпретируется — это один argv-элемент.
    expect(args).toContain(evil);
    expect(args.filter((a) => a === evil)).toHaveLength(1);
  });

  it("assertSafeArg отсекает пробелы и переводы строк", () => {
    expect(() => assertSafeArg("a b")).toThrow();
    expect(() => assertSafeArg("a\nrm -rf /")).toThrow();
    expect(assertSafeArg("/ok/path_01.mp4")).toBe("/ok/path_01.mp4");
  });
});

describe("Grok payload", () => {
  it("валидный text-to-video", () => {
    const p: any = buildGrokPayload("grok-imagine-video", { mode: "text_to_video", prompt: "cinematic", durationSeconds: 5, aspectRatio: "9:16", resolution: "720p" });
    expect(p.model).toBe("grok-imagine-video");
    expect(p.duration).toBe(5);
  });
  it("бросает на пустом промпте и на image-to-video без файла", () => {
    expect(() => buildGrokPayload("m", { mode: "text_to_video", prompt: "", durationSeconds: 5, aspectRatio: "9:16", resolution: "720p" })).toThrow(GrokError);
    expect(() => buildGrokPayload("m", { mode: "image_to_video", prompt: "p", durationSeconds: 5, aspectRatio: "9:16", resolution: "720p" })).toThrow(GrokError);
  });
});
