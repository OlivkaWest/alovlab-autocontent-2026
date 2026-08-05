import { describe, it, expect, vi, afterEach } from "vitest";
import { heygenFetch } from "../src/heygen/client";
import { HeygenError } from "../src/heygen/errors";

function jsonResponse(status: number, body: unknown): Response {
  return {
    ok: status >= 200 && status < 300,
    status,
    json: async () => body,
    text: async () => JSON.stringify(body),
  } as unknown as Response;
}

afterEach(() => vi.unstubAllGlobals());

const noSleep = async () => {};

describe("heygenFetch retry", () => {
  it("повторяет временную ошибку (500) и добивается успеха", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce(jsonResponse(500, { m: "err" }))
      .mockResolvedValueOnce(jsonResponse(500, { m: "err" }))
      .mockResolvedValueOnce(jsonResponse(200, { ok: true }));
    vi.stubGlobal("fetch", fetchMock);

    const res = await heygenFetch("/v2/x", {}, { retries: 3, baseDelayMs: 1, sleep: noSleep });
    expect(res).toEqual({ ok: true });
    expect(fetchMock).toHaveBeenCalledTimes(3);
  });

  it("НЕ повторяет постоянную ошибку (401)", async () => {
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse(401, { m: "no" }));
    vi.stubGlobal("fetch", fetchMock);

    await expect(heygenFetch("/v2/x", {}, { retries: 3, baseDelayMs: 1, sleep: noSleep })).rejects.toBeInstanceOf(HeygenError);
    expect(fetchMock).toHaveBeenCalledTimes(1);
  });

  it("после исчерпания попыток бросает retriable-ошибку", async () => {
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse(429, { m: "slow" }));
    vi.stubGlobal("fetch", fetchMock);

    await expect(heygenFetch("/v2/x", {}, { retries: 2, baseDelayMs: 1, sleep: noSleep })).rejects.toMatchObject({ kind: "rate_limit" });
    expect(fetchMock).toHaveBeenCalledTimes(3); // 1 + 2 повтора
  });
});
