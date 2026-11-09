import React from "react";
import { Composition, Sequence, AbsoluteFill } from "remotion";
import { Bg } from "./kit/kit";
import { S1Title } from "./scenes/S1Title";
import { S2Origin } from "./scenes/S2Origin";
import { S3Map } from "./scenes/S3Map";
import { S4Build } from "./scenes/S4Build";
import { S5Cta } from "./scenes/S5Cta";

const FPS = 30;
// S1 0-5s(150) · S2 5-12s(210) · S3 12-17s(150) · S4 17-30s(390) · S5 30-37.6s(228)
const DURS = [150, 210, 150, 390, 228];
const TOTAL = DURS.reduce((a, b) => a + b, 0); // 1128 = 37.6s @30fps

export const Collage: React.FC = () => {
  let cursor = 0;
  const scenes = [S1Title, S2Origin, S3Map, S4Build, S5Cta];
  return (
    <AbsoluteFill>
      {scenes.map((Scene, i) => {
        const from = cursor;
        cursor += DURS[i];
        return (
          <Sequence key={i} from={from} durationInFrames={DURS[i]}>
            <Scene />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Collage"
        component={Collage}
        durationInFrames={TOTAL}
        fps={FPS}
        width={1080}
        height={1920}
      />
    </>
  );
};
