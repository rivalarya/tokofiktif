"use client"

import type React from "react"
import { useState } from "react"
import { Send, Bot, User } from "lucide-react"

const suggestions = [
  "cara retur barang",
  "cara batalkan pesanan yang sudah dibuat",
  "cara buka toko sebagai penjual",
]

type Message = {
  role: "user" | "bot"
  content: string
}

export default function Home() {
  const [input, setInput] = useState("")
  const [messages, setMessages] = useState<Message[]>([])
  const [loading, setLoading] = useState(false)

  const sendMessage = async (question: string) => {
    if (!question.trim() || loading) return

    const userMsg: Message = { role: "user", content: question }
    setMessages([userMsg])
    setInput("")
    setLoading(true)

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      })
      const data = await res.json()
      const botMsg: Message = {
        role: "bot",
        content: data.answer || "Maaf, terjadi kesalahan.",
      }
      setMessages([userMsg, botMsg])
    } catch {
      setMessages([userMsg, { role: "bot", content: "Gagal terhubung ke server." }])
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    sendMessage(input)
  }

  return (
    <div className="mx-auto flex h-full max-w-2xl flex-col p-4">
      <div className="mb-4 text-center">
        <h1 className="text-xl font-bold">Customer Service TokoFiktif</h1>
        <p className="text-sm text-muted-foreground">
          Tanyakan apa saja tentang TokoFiktif
        </p>
      </div>

      <div className="flex-1 space-y-4 overflow-auto rounded-lg border p-4">
        {messages.length === 0 && (
          <div className="flex h-full items-center justify-center">
            <p className="text-sm text-muted-foreground">
              Mulai percakapan dengan mengetik pesan atau pilih saran di bawah
            </p>
          </div>
        )}
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`flex gap-3 ${msg.role === "user" ? "justify-end" : "justify-start"}`}
          >
            {msg.role === "bot" && (
              <div className="mt-1 flex size-8 shrink-0 items-center justify-center rounded-full bg-primary text-primary-foreground">
                <Bot className="size-4" />
              </div>
            )}
            <div
              className={`max-w-[80%] rounded-xl px-4 py-2 text-sm ${
                msg.role === "user"
                  ? "bg-primary text-primary-foreground"
                  : "bg-muted"
              }`}
            >
              {msg.content}
            </div>
            {msg.role === "user" && (
              <div className="mt-1 flex size-8 shrink-0 items-center justify-center rounded-full bg-secondary">
                <User className="size-4" />
              </div>
            )}
          </div>
        ))}
        {loading && (
          <div className="flex gap-3">
            <div className="mt-1 flex size-8 shrink-0 items-center justify-center rounded-full bg-primary text-primary-foreground">
              <Bot className="size-4" />
            </div>
            <div className="max-w-[80%] rounded-xl bg-muted px-4 py-2 text-sm">
              <span className="animate-pulse">Mengetik...</span>
            </div>
          </div>
        )}
      </div>

      <div className="mt-3 flex flex-wrap gap-2">
        {suggestions.map((s) => (
          <button
            key={s}
            onClick={() => sendMessage(s)}
            disabled={loading}
            className="rounded-full border bg-background px-3 py-1 text-xs text-muted-foreground hover:bg-accent disabled:opacity-50"
          >
            {s}
          </button>
        ))}
      </div>

      <form onSubmit={handleSubmit} className="mt-3 flex gap-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ketik pesan..."
          disabled={loading}
          className="flex h-10 w-full rounded-md border bg-background px-3 py-2 text-sm placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] disabled:opacity-50"
        />
        <button
          type="submit"
          disabled={loading || !input.trim()}
          className="inline-flex h-10 w-10 shrink-0 items-center justify-center rounded-md bg-primary text-primary-foreground hover:bg-primary/90 disabled:opacity-50"
        >
          <Send className="size-4" />
        </button>
      </form>
    </div>
  )
}
