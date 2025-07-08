module.exports = {
  branches: [
    "main",
    {
      name: "dev",
      channel: "dev",
      prerelease: "beta",
    },
  ],
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    [
      "@semantic-release/git",
      {
        message: "chore(release): ${nextRelease.version} [skip ci]",
      },
    ],
    "@semantic-release/github",
  ],
};