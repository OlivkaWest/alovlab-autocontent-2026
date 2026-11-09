import React from "react";
import { useCurrentFrame, interpolate } from "remotion";
import {
  Bg,
  WordReveal,
  PaperCard,
  RedUnderline,
  Character,
  COLORS,
  Tag,
  fadeSlideIn,
} from "../kit/kit";

export const S2Origin: React.FC = () => {
  const frame = useCurrentFrame();
  const cardIn = fadeSlideIn(frame, 10, 16);
  const stampIn = fadeSlideIn(frame, 60, 14);
  const quoteIn = fadeSlideIn(frame, 100, 14);

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
          text="Слово родилось в одном посте"
          start={0}
          style={{ fontSize: 34, color: COLORS.ink, fontWeight: 700 }}
        />
      </div>

      <div
        style={{
          position: "absolute",
          top: 180,
          left: 36,
          right: 36,
          opacity: cardIn,
          transform: `translateY(${(1 - cardIn) * 24}px)`,
        }}
      >
        <PaperCard rotate={-1.5}>
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              fontSize: 18,
              color: "#8A8070",
              fontWeight: 700,
              letterSpacing: 1,
              marginBottom: 10,
            }}
          >
            <span>ФЕВРАЛЬ 2025</span>
            <span>ТЕХНОЛОГИИ</span>
          </div>
          <div style={{ fontSize: 36, fontWeight: 800, color: COLORS.ink }}>
            Слово родилось
            <br />в одном посте
          </div>
          <div
            style={{
              fontStyle: "italic",
              fontSize: 20,
              color: "#4a443c",
              marginTop: 14,
            }}
          >
            Андрей Карпаты, бывший директор по ИИ в Tesla, пишет в X про
            «vibe coding»
          </div>

          <div
            style={{
              position: "absolute",
              right: 26,
              top: 140,
              opacity: stampIn,
              transform: `rotate(-8deg) scale(${0.8 + stampIn * 0.2})`,
              border: `3px solid ${COLORS.red}`,
              color: COLORS.red,
              fontWeight: 800,
              fontSize: 18,
              padding: "6px 10px",
              textAlign: "center",
              borderRadius: 4,
            }}
          >
            2 ФЕВРАЛЯ
            <br />
            2025
          </div>
        </PaperCard>
      </div>

      <div
        style={{
          position: "absolute",
          top: 560,
          left: 36,
          opacity: quoteIn,
          transform: `translateX(${(1 - quoteIn) * -20}px)`,
        }}
      >
        <div
          style={{
            background: "#E8C33B",
            color: COLORS.ink,
            fontWeight: 800,
            fontSize: 26,
            padding: "16px 20px",
            maxWidth: 300,
            boxShadow: "0 10px 20px rgba(0,0,0,0.18)",
          }}
        >
          «Просто говоришь, что нужно»
          <RedUnderline width={220} start={115} />
        </div>
      </div>

      <div style={{ position: "absolute", bottom: 54, left: 36 }}>
        <Tag label="вырезки" />
      </div>

      <div style={{ position: "absolute", bottom: 44, right: 30 }}>
        <Character pose="thumbsup" size={260} />
      </div>
    </Bg>
  );
};
