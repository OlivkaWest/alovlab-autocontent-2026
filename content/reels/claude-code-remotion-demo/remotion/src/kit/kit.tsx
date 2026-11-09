import React from "react";
import { interpolate, useCurrentFrame, staticFile } from "remotion";

export const COLORS = {
  bg: "#E9E1D3",
  paper: "#F3EDE1",
  ink: "#2B2621",
  red: "#C23B2B",
  blue: "#2B5FC2",
  tape: "#DCD2BC",
};

export const Bg: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div
    style={{
      width: "100%",
      height: "100%",
      background: COLORS.bg,
      fontFamily: "Helvetica, Arial, sans-serif",
      position: "relative",
    }}
  >
    {children}
  </div>
);

export const fadeSlideIn = (frame: number, start: number, dur = 18) =>
  interpolate(frame, [start, start + dur], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

export const WordReveal: React.FC<{
  text: string;
  start: number;
  style?: React.CSSProperties;
  perWord?: number;
}> = ({ text, start, style, perWord = 6 }) => {
  const frame = useCurrentFrame();
  const words = text.split(" ");
  return (
    <div style={{ ...style }}>
      {words.map((w, i) => {
        const o = fadeSlideIn(frame, start + i * perWord, 10);
        return (
          <span
            key={i}
            style={{
              opacity: o,
              transform: `translateY(${(1 - o) * 14}px)`,
              display: "inline-block",
              marginRight: 10,
            }}
          >
            {w}
          </span>
        );
      })}
    </div>
  );
};

export const PaperCard: React.FC<{
  children: React.ReactNode;
  style?: React.CSSProperties;
  rotate?: number;
}> = ({ children, style, rotate = -1.2 }) => (
  <div
    style={{
      background: COLORS.paper,
      boxShadow: "0 18px 34px rgba(43,38,33,0.18)",
      clipPath:
        "polygon(1% 3%, 14% 0%, 30% 2%, 46% 0%, 63% 2%, 80% 0%, 97% 3%, 100% 20%, 98% 45%, 100% 70%, 97% 97%, 80% 100%, 60% 98%, 40% 100%, 20% 98%, 2% 100%, 0% 75%, 2% 50%, 0% 25%)",
      padding: "34px 30px",
      transform: `rotate(${rotate}deg)`,
      ...style,
    }}
  >
    {children}
  </div>
);

export const RedUnderline: React.FC<{ width: number; start: number }> = ({
  width,
  start,
}) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [start, start + 14], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <svg width={width} height={16} style={{ display: "block", marginTop: 4 }}>
      <path
        d={`M4 8 Q ${width / 2} ${p > 0.5 ? 14 : 2}, ${4 + (width - 8) * p} 8`}
        stroke={COLORS.red}
        strokeWidth={6}
        fill="none"
        strokeLinecap="round"
      />
    </svg>
  );
};

export const Tag: React.FC<{ label: string }> = ({ label }) => (
  <div
    style={{
      display: "inline-flex",
      alignItems: "center",
      gap: 8,
      background: "#fff",
      border: `1px solid ${COLORS.ink}22`,
      borderRadius: 999,
      padding: "8px 16px",
      fontSize: 22,
      color: COLORS.ink,
      boxShadow: "0 6px 14px rgba(43,38,33,0.10)",
    }}
  >
    ✂ {label}
  </div>
);

const POSES = [
  "neutral",
  "thumbsup",
  "pointing",
  "thinking",
  "shock",
  "pointup",
] as const;
export type Pose = (typeof POSES)[number];

/**
 * Falls back to a labeled placeholder circle when the real PNG (generated
 * from character-prompts.md with Identity Lock) isn't in public/character/ yet.
 */
export const Character: React.FC<{ pose: Pose; size?: number }> = ({
  pose,
  size = 300,
}) => {
  const [missing, setMissing] = React.useState(false);
  if (missing) {
    return (
      <div
        style={{
          width: size,
          height: size,
          borderRadius: "50%",
          background: "#D8CCB0",
          border: `4px solid ${COLORS.ink}`,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontSize: size * 0.4,
          fontWeight: 700,
          color: COLORS.ink,
        }}
        title={`placeholder for ${pose}`}
      >
        И
      </div>
    );
  }
  return (
    <img
      src={staticFile(`character/${pose}.png`)}
      width={size}
      height={size}
      style={{ objectFit: "contain" }}
      onError={() => setMissing(true)}
    />
  );
};
