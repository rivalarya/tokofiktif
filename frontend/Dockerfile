FROM node:lts-alpine AS base
RUN apk add --no-cache libc6-compat
RUN corepack enable && corepack prepare pnpm@11.0.9 --activate

FROM base AS deps
WORKDIR /app
COPY frontend/package.json frontend/pnpm-lock.yaml* frontend/pnpm-workspace.yaml ./frontend/
WORKDIR /app/frontend
RUN --mount=type=cache,target=/root/.local/share/pnpm/store \
    pnpm install --frozen-lockfile

FROM base AS builder
WORKDIR /app
COPY --from=deps /app/frontend/node_modules ./frontend/node_modules
COPY frontend/ ./frontend/
WORKDIR /app/frontend
ENV CI=true
RUN pnpm run build

FROM base AS runner
WORKDIR /app
ENV NODE_ENV=production
ENV PORT=3000
ENV HOSTNAME=0.0.0.0

RUN addgroup --system --gid 1001 nodejs \
 && adduser --system --uid 1001 nextjs \
 && chown nextjs:nodejs /app

USER nextjs

COPY --chown=nextjs:nodejs --from=builder /app/frontend/public ./public
COPY --chown=nextjs:nodejs --from=builder /app/frontend/.next ./.next
COPY --chown=nextjs:nodejs --from=builder /app/frontend/node_modules ./node_modules
COPY --chown=nextjs:nodejs --from=builder /app/frontend/package.json ./package.json

EXPOSE 3000
CMD ["node", "node_modules/next/dist/bin/next", "start"]
