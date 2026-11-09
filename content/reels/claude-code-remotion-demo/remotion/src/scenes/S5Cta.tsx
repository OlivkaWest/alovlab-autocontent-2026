import React from "react";
import { useCurrentFrame } from "remotion";
import {
  Bg,
  WordReveal,
  PaperCard,
  Character,
  COLORS,
  fadeSlideIn,
} from "../kit/kit";

export const S5Cta: React.FC = () => {
  const frame = useCurrentFrame();
  const cardIn = fadeSlideIn(frame, 10, 16);
  const btnIn = fadeSlideIn(frame, 70, 14);
  const checkA = fadeSlideIn(frame, 120, 10);
  const checkB = fadeSlideIn(frame, 140, 10);

  return (
    <Bg>
      <div
        style={{
          position: "absolute",
          top: 60,
          left: 30,
          right: 30,
          textAlign: "center",
        }}
      >
        <WordReveal
          text="Промпт целиком"
          start={0}
          style={{ fontSize: 36, color: COLORS.ink, fontWeight: 800 }}
        />
      </div>

      <div
        style={{
          position: "absolute",
          top: 170,
          left: 36,
          right: 36,
          opacity: cardIn,
          transform: `translateY(${(1 - cardIn) * 24}px)`,
        }}
      >
        <PaperCard rotate={-1}>
          <div
            style={{
              fontSize: 16,
              fontWeight: 800,
              color: COLORS.red,
              letterSpacing: 1,
              marginBottom: 10,
            }}
          >
            ПОДАРОК · ПРОМПТ
          </div>
          <div style={{ fontSize: 30, fontWeight: 800, color: COLORS.ink, lineHeight: 1.25 }}>
            Коллаж в стиле Vox:
            <br />
            промпт для Claude Code
          </div>
        </PaperCard>
      </div>

      <div
        style={{
          position: "absolute",
          top: 430,
          left: 36,
          right: 36,
          display: "flex",
          gap: 14,
        }}
      >
        <div
          style={{
            opacity: checkA,
            background: "#fff",
            border: `1px solid ${COLORS.ink}22`,
            borderRadius: 999,
            padding: "10px 16px",
            fontSize: 18,
            fontWeight: 700,
            color: COLORS.ink,
          }}
        >
          ✓ что нужно для запуска
        </div>
        <div
          style={{
            opacity: checkB,
            background: "#fff",
            border: `1px solid ${COLORS.ink}22`,
            borderRadius: 999,
            padding: "10px 16px",
            fontSize: 18,
            fontWeight: 700,
            color: COLORS.ink,
          }}
        >
          ✓ примеры правок
        </div>
      </div>

      <div
        style={{
          position: "absolute",
          top: 520,
          left: 36,
          right: 36,
          opacity: btnIn,
          transform: `scale(${0.9 + btnIn * 0.1})`,
        }}
      >
        <div
          style={{
            background: COLORS.red,
            color: "#fff",
            textAlign: "center",
            fontWeight: 800,
            fontSize: 24,
            padding: "18px 0",
            borderRadius: 999,
            boxShadow: "0 14px 24px rgba(194,59,43,0.35)",
          }}
        >
          ↑ забирай в Telegram
        </div>
      </div>

      <div style={{ position: "absolute", bottom: 40, right: 30 }}>
        <Character pose="pointup" size={260} />
      </div>
    </Bg>
  );
};
