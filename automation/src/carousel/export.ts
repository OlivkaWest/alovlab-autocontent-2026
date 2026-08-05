import fs from "node:fs";
import path from "node:path";
import archiver from "archiver";
import { projectDir } from "../store/projects";
import { renderCards, renderPreview } from "./render";
import { cardFileName } from "./template";
import { CarouselExport, type Carousel, type Project } from "../store/types";
import { createLogger } from "../logger";

const log = createLogger("carousel-export");

/** ZIP со всеми PNG. Пути передаём массивом — без shell, без инъекций. */
function zipFiles(files: string[], zipPath: string): Promise<string> {
  return new Promise((resolve, reject) => {
    const output = fs.createWriteStream(zipPath);
    const archive = archiver("zip", { zlib: { level: 9 } });
    output.on("close", () => resolve(zipPath));
    archive.on("error", reject);
    archive.pipe(output);
    for (const f of files) archive.file(f, { name: path.basename(f) });
    archive.finalize();
  });
}

/**
 * Полный экспорт карусели проекта:
 *  — по одному PNG на карточку (01_cover.png …);
 *  — ZIP со всеми карточками;
 *  — JSON с текстом и метаданными;
 *  — превью всей карусели.
 */
export async function exportCarousel(project: Project): Promise<CarouselExport> {
  if (!project.carousel) throw new Error("У проекта нет карусели — сначала сгенерируй её");
  const carousel: Carousel = project.carousel;

  const dir = path.join(projectDir(project.id), "carousel");
  const pngDir = path.join(dir, "png");
  fs.mkdirSync(pngDir, { recursive: true });

  // 1. PNG-карточки
  const rendered = await renderCards(carousel.cards, pngDir);
  const pngFiles = rendered.map((r) => r.file);

  // 2. JSON с текстом и метаданными
  const jsonFile = path.join(dir, "carousel.json");
  fs.writeFileSync(
    jsonFile,
    JSON.stringify(
      {
        projectId: project.id,
        title: carousel.title,
        caption: carousel.caption,
        cta: carousel.cta,
        cards: carousel.cards.map((c) => ({
          file: cardFileName(c),
          role: c.role,
          title: c.title,
          body: c.body,
          accent: c.accent,
        })),
        format: "Instagram 4:5 · 1080×1350",
      },
      null,
      2
    ),
    "utf8"
  );

  // 3. ZIP
  const zipFile = path.join(dir, "carousel.zip");
  await zipFiles([...pngFiles, jsonFile], zipFile);

  // 4. Превью
  const previewFile = path.join(dir, "preview.png");
  await renderPreview(carousel.cards, previewFile);

  log.info(`Экспорт карусели готов: ${pngFiles.length} PNG, ZIP, JSON, превью`);

  return CarouselExport.parse({
    pngFiles,
    zipFile,
    jsonFile,
    previewFile,
  });
}
