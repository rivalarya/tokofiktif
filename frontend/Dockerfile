FROM node:lts-alpine AS base
RUN apk add --no-cache libc6-compat
RUN corepack enable && corepack prepare pnpm@11.0.9 --activate

FROM base AS deps
WORKDIR /app
COPY package.json pnpm-lock.yaml* pnpm-workspace.yaml ./
RUN --mount=type=cache,target=/root/.local/share/pnpm/store \
    pnpm install --frozen-lockfile

FROM base AS builder
WORKDIR /app
ENV CI=true
COPY --from=deps /app/node_modules ./node_modules
COPY . .
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

COPY --chown=nextjs:nodejs --from=builder /app/public ./public
COPY --chown=nextjs:nodejs --from=builder /app/.next ./.next
COPY --chown=nextjs:nodejs --from=builder /app/node_modules ./node_modules
COPY --chown=nextjs:nodejs --from=builder /app/package.json ./package.json

EXPOSE 3000
CMD ["node", "node_modules/next/dist/bin/next", "start"]