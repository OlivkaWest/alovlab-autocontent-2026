import React from "react";
import { useCurrentFrame, interpolate } from "remotion";
import { Bg, WordReveal, Character, COLORS, fadeSlideIn } from "../kit/kit";

const Terminal: React.FC<{ children: React.ReactNode; title?: string }> = ({
  children,
  title = "~/коллаж",
}) => (
  <div
    style={{
      position: "absolute",
      top: 250,
      left: 24,
      right: 24,
      background: "#1C1A17",
      borderRadius: 16,
      boxShadow: "0 20px 40px rgba(0,0,0,0.35)",
      overflow: "hidden",
    }}
  >
    <div
      style={{
        display: "flex",
        alignItems: "center",
        gap: 8,
        padding: "12px 16px",
        borderBottom: "1px solid #2E2B26",
      }}
    >
      <span style={{ width: 11, height: 11, borderRadius: 6, background: "#E8605A" }} />
      <span style={{ width: 11, height: 11, borderRadius: 6, background: "#E8C33B" }} />
      <span style={{ width: 11, height: 11, borderRadius: 6, background: "#5FBF6B" }} />
      <span style={{ color: "#B7AF9F", fontSize: 15, marginLeft: 6 }}>
        Claude Code {title}
      </span>
    </div>
    <div style={{ padding: "18px 20px", minHeight: 320, fontFamily: "Menlo, monospace" }}>
      {children}
    </div>
  </div>
);

const Line: React.FC<{
  text: string;
  color?: string;
  bold?: boolean;
  start: number;
}> = ({ text, color = "#D8D1C2", bold, start }) => {
  const frame = useCurrentFrame();
  const o = fadeSlideIn(frame, start, 8);
  return (
    <div
      style={{
        color,
        fontWeight: bold ? 700 : 400,
        fontSize: 17,
        lineHeight: 1.6,
        opacity: o,
      }}
    >
      {text}
    </div>
  );
};

export const S4Build: React.FC = () => {
  const frame = useCurrentFrame();

  // local phases within this scene (390f total @30fps)
  const phase1 = frame < 46; // "Как это сделать" + character alone
  const phase2 = frame >= 46 && frame < 110; // empty terminal
  const phase3 = frame >= 110 && frame < 230; // prompt pasted
  const phase4 = frame >= 230 && frame < 300; // npm install + write files
  const phase5 = frame >= 300; // render progress + timeline

  const renderPct = Math.min(
    100,
    Math.round(interpolate(frame, [300, 380], [0, 100], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }))
  );

  return (
    <Bg>
      {phase1 && (
        <>
          <div
            style={{
              position: "absolute",
              top: 110,
              left: 30,
              right: 30,
              textAlign: "center",
            }}
          >
            <WordReveal
              text="Как это сделать."
              start={0}
              style={{ fontSize: 36, color: COLORS.ink, fontWeight: 700 }}
            />
          </div>
          <div
            style={{
              position: "absolute",
              bottom: 260,
              left: 0,
              right: 0,
              display: "flex",
              justifyContent: "center",
            }}
          >
            <Character pose="thinking" clipId="s4" size={300} />
          </div>
        </>
      )}

      {phase2 && (
        <>
          <div
            style={{
              position: "absolute",
              top: 100,
              left: 30,
              right: 30,
              textAlign: "center",
            }}
          >
            <WordReveal
              text="пустой"
              start={46}
              style={{ fontSize: 32, color: COLORS.ink, fontWeight: 700 }}
            />
          </div>
          <Terminal>
            <div style={{ color: "#6E675A", fontSize: 15 }}>
              Новый чат · локально · ~/коллаж
            </div>
            <div
              style={{
                marginTop: 16,
                background: "#262320",
                borderRadius: 8,
                padding: "10px 14px",
                color: "#6E675A",
              }}
            >
              ›
            </div>
          </Terminal>
        </>
      )}

      {phase3 && (
        <>
          <div
            style={{
              position: "absolute",
              top: 90,
              left: 30,
              right: 30,
              textAlign: "center",
            }}
          >
            <WordReveal
              text="вставляешь мой промпт."
              start={110}
              style={{ fontSize: 30, color: COLORS.ink, fontWeight: 700 }}
            />
          </div>
          <Terminal>
            <Line start={128} text="Тема ролика: [откуда взялось слово «вайб кодинг»]." />
            <Line start={138} text=" " />
            <Line
              start={144}
              text="Ты моушн-дизайнер и разработчик Remotion. Сделай"
            />
            <Line text="короткую объясняющую анимацию в стиле бумажного" start={152} />
            <Line text="коллажа, как в роликах Vox. Всё — кодом, без ручной" start={160} />
            <Line text="анимации." start={168} />
            <Line start={178} text=" " />
            <Line start={182} text="Формат: 1080×1920, 30 к/с, 30–38 секунд, 5 сцен." color="#8FB7A8" />
            <Line start={196} text="(полный промпт — в Telegram, см. CTA)" color="#6E675A" />
          </Terminal>
        </>
      )}

      {phase4 && (
        <>
          <div
            style={{
              position: "absolute",
              top: 90,
              left: 30,
              right: 30,
              textAlign: "center",
            }}
          >
            <WordReveal
              text="Он сам ставит Remotion,"
              start={230}
              style={{ fontSize: 28, color: COLORS.ink, fontWeight: 700 }}
            />
          </div>
          <Terminal>
            <Line start={238} text="● Bash(npm install remotion @remotion/cli …)" />
            <Line start={248} text="  └ added 253 packages in 7s" color="#8FB7A8" />
            <Line start={262} text="● Write — сцены и детали коллажа" />
            <Line start={270} text="  └ src/Root.tsx" color="#8FB7A8" />
            <Line start={276} text="  └ src/kit/kit.tsx" color="#8FB7A8" />
            <Line start={282} text="  └ src/scenes/S1Title.tsx … S5Cta.tsx" color="#8FB7A8" />
            <Line start={290} text="  └ src/data/map.json" color="#8FB7A8" />
          </Terminal>
        </>
      )}

      {phase5 && (
        <>
          <div
            style={{
              position: "absolute",
              top: 90,
              left: 30,
              right: 30,
              textAlign: "center",
            }}
          >
            <WordReveal
              text="пишет сцены и рендерит"
              start={300}
              style={{ fontSize: 28, color: COLORS.ink, fontWeight: 700 }}
            />
          </div>
          <Terminal>
            <Line start={300} text="● Рендер Collage" />
            <div
              style={{
                marginTop: 10,
                background: "#262320",
                borderRadius: 999,
                height: 14,
                overflow: "hidden",
              }}
            >
              <div
                style={{
                  width: `${renderPct}%`,
                  height: "100%",
                  background: COLORS.red,
                  borderRadius: 999,
                }}
              />
            </div>
            <Line
              start={300}
              text={`${Math.round((renderPct / 100) * 1128)}/1128`}
              color="#8FB7A8"
            />
            {frame > 360 && (
              <Line
                start={360}
                text="Каждая сцена = блок на таймлайне"
                bold
                color="#E8C33B"
              />
            )}
          </Terminal>
        </>
      )}

      <div style={{ position: "absolute", bottom: 20, right: 28 }}>
        {phase4 || phase5 ? (
          <Character pose="shock" clipId="s4" size={190} />
        ) : null}
      </div>
    </Bg>
  );
};
