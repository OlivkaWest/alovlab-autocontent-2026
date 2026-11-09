import React from "react";
import { useCurrentFrame } from "remotion";
import { Bg, WordReveal, Character, COLORS, fadeSlideIn } from "../kit/kit";

const Cutout: React.FC<{
  text: string;
  bg: string;
  color: string;
  rotate: number;
  start: number;
}> = ({ text, bg, color, rotate, start }) => {
  const frame = useCurrentFrame();
  const o = fadeSlideIn(frame, start, 10);
  return (
    <span
      style={{
        display: "inline-block",
        background: bg,
        color,
        fontWeight: 900,
        fontSize: 64,
        padding: "4px 14px",
        margin: "0 4px",
        transform: `rotate(${rotate}deg) scale(${0.85 + o * 0.15})`,
        opacity: o,
        boxShadow: "0 6px 10px rgba(0,0,0,0.25)",
      }}
    >
      {text}
    </span>
  );
};

export const S1Title: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <Bg>
      <div
        style={{
          position: "absolute",
          top: 90,
          left: 40,
          right: 40,
          textAlign: "center",
        }}
      >
        <WordReveal
          text="Теперь Claude Code"
          start={0}
          style={{ fontSize: 34, color: "#7A7266", fontWeight: 600 }}
        />
      </div>

      <div
        style={{
          position: "absolute",
          top: 230,
          left: 20,
          right: 20,
          textAlign: "center",
          lineHeight: 1.1,
        }}
      >
        <div>
          <Cutout text="ВАЙБ" bg="#1C1A17" color="#fff" rotate={-3} start={18} />
          <Cutout text="КО" bg="#E8C33B" color="#1C1A17" rotate={2} start={26} />
          <Cutout text="ДИНГ" bg="#C23B2B" color="#fff" rotate={-1} start={32} />
        </div>
      </div>

      <div
        style={{
          position: "absolute",
          top: 430,
          left: 40,
          right: 40,
          textAlign: "center",
        }}
      >
        <WordReveal
          text="И ты откуда взялось слово"
          start={70}
          style={{ fontSize: 30, color: COLORS.ink, fontWeight: 500 }}
        />
      </div>

      <div style={{ position: "absolute", bottom: 60, right: 40 }}>
        <Character pose="neutral" size={300} />
      </div>
    </Bg>
  );
};
