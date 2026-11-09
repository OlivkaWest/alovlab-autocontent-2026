import React from "react";
import { useCurrentFrame, interpolate } from "remotion";
import { Bg, WordReveal, Character, COLORS, fadeSlideIn } from "../kit/kit";
import mapData from "../data/map.json";

const CITY_XY: Record<string, [number, number]> = {
  "Сан-Франциско": [60, 130],
  Москва: [330, 95],
  Лондон: [250, 100],
  Берлин: [280, 100],
};

export const S3Map: React.FC = () => {
  const frame = useCurrentFrame();
  const mapIn = fadeSlideIn(frame, 10, 16);
  const stampIn = fadeSlideIn(frame, 100, 14);

  return (
    <Bg>
      <div
        style={{
          position: "absolute",
          top: 70,
          left: 30,
          right: 30,
          textAlign: "center",
        }}
      >
        <WordReveal
          text="За месяцы — по всему миру"
          start={0}
          style={{ fontSize: 36, color: COLORS.ink, fontWeight: 700 }}
        />
      </div>

      <div
        style={{
          position: "absolute",
          top: 280,
          left: 30,
          right: 30,
          opacity: mapIn,
          transform: `translateY(${(1 - mapIn) * 20}px)`,
        }}
      >
        <svg viewBox="0 0 400 220" width="100%" height={260}>
          <rect
            x={0}
            y={0}
            width={400}
            height={220}
            fill="#F3EDE1"
            rx={6}
          />
          <rect
            x={4}
            y={4}
            width={392}
            height={212}
            fill="none"
            stroke={COLORS.ink}
            strokeOpacity={0.15}
          />
          {/* very simplified world silhouette blocks, stylised not geographic-accurate */}
          <rect x={30} y={70} width={120} height={50} fill="#D9A94B" opacity={0.6} rx={10} />
          <rect x={170} y={60} width={90} height={60} fill="#D9A94B" opacity={0.6} rx={10} />
          <rect x={270} y={65} width={100} height={55} fill="#D9A94B" opacity={0.6} rx={10} />
          <rect x={60} y={150} width={60} height={40} fill="#D9A94B" opacity={0.4} rx={10} />
          <rect x={200} y={150} width={70} height={35} fill="#D9A94B" opacity={0.4} rx={10} />

          {mapData.routes.map((r, i) => {
            const from = CITY_XY[r.from] ?? [60, 130];
            const to = CITY_XY[r.to] ?? [300, 100];
            const dur = 20;
            const start = 24 + i * 10;
            const p = interpolate(frame, [start, start + dur], [0, 1], {
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
            });
            const mx = (from[0] + to[0]) / 2;
            const my = Math.min(from[1], to[1]) - 30;
            return (
              <path
                key={i}
                d={`M ${from[0]} ${from[1]} Q ${mx} ${my} ${to[0]} ${to[1]}`}
                fill="none"
                stroke={COLORS.red}
                strokeWidth={2.5}
                strokeDasharray="300"
                strokeDashoffset={300 * (1 - p)}
              />
            );
          })}
          {Object.entries(CITY_XY).map(([name, [x, y]]) => (
            <g key={name}>
              <circle cx={x} cy={y} r={4} fill={COLORS.red} />
              <text x={x + 7} y={y + 4} fontSize={11} fill={COLORS.ink}>
                {name}
              </text>
            </g>
          ))}
        </svg>
      </div>

      <div
        style={{
          position: "absolute",
          top: 230,
          right: 40,
          opacity: stampIn,
          transform: `rotate(-8deg) scale(${0.8 + stampIn * 0.2})`,
          border: `3px solid ${COLORS.red}`,
          color: COLORS.red,
          fontWeight: 800,
          fontSize: 18,
          padding: "8px 12px",
          textAlign: "center",
          borderRadius: 4,
          background: COLORS.bg,
        }}
      >
        СЛОВО ГОДА
        <br />
        2025
      </div>

      <div style={{ position: "absolute", bottom: 50, right: 36 }}>
        <Character pose="pointing" size={260} />
      </div>
    </Bg>
  );
};
