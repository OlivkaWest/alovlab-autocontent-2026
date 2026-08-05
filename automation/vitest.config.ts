import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["test/**/*.test.ts"],
    environment: "node",
    globals: false,
    testTimeout: 20000,
    // Тестовый ключ, чтобы низкоуровневый heygenFetch доходил до (застабленного) fetch.
    env: { HEYGEN_API_KEY: "test_key_0123456789", HEYGEN_MOCK_MODE: "true" },
  },
});
