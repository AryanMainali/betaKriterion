/** @type {import('next').NextConfig} */
function getApiOrigin(rawUrl) {
  return (rawUrl || "http://localhost:8000")
    .replace(/\/$/, "")
    .replace(/\/api(?:\/v1)?$/, "");
}

const nextConfig = {
  output: "standalone",
  reactStrictMode: true,
  env: {
    NEXT_PUBLIC_API_URL:
      process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",
    NEXT_PUBLIC_APP_NAME: process.env.NEXT_PUBLIC_APP_NAME || "Kriterion",
  },
  async rewrites() {
    const apiOrigin = getApiOrigin(process.env.NEXT_PUBLIC_API_URL);
    return [
      {
        source: "/api/:path*",
        destination: `${apiOrigin}/api/:path*`,
      },
    ];
  },
};

module.exports = nextConfig;
