"use client"

import { useState, useEffect } from "react"
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
import { ChevronDown } from "lucide-react"

type FaqItem = {
  id: number
  category: string
  question: string
  answer: string
}

function groupByCategory(items: FaqItem[]): Record<string, FaqItem[]> {
  const groups: Record<string, FaqItem[]> = {}
  for (const item of items) {
    if (!groups[item.category]) groups[item.category] = []
    groups[item.category].push(item)
  }
  return groups
}

export default function SidebarClient() {
  const [faqs, setFaqs] = useState<FaqItem[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch("/api/faq")
      .then((res) => res.json())
      .then((data) => setFaqs(data))
      .catch(() => setFaqs([]))
      .finally(() => setLoading(false))
  }, [])

  const groups = groupByCategory(faqs)

  if (loading) {
    return (
      <div className="space-y-2 p-3">
        {[1, 2, 3].map((i) => (
          <div key={i} className="h-4 animate-pulse rounded bg-sidebar-accent" />
        ))}
      </div>
    )
  }

  return (
    <div className="space-y-1">
      {Object.entries(groups).map(([category, items]) => (
        <Collapsible key={category}>
          <CollapsibleTrigger className="flex w-full items-center gap-2 rounded-md px-3 py-2 text-sm font-medium text-sidebar-foreground hover:bg-sidebar-accent [&[data-state=open]>svg]:rotate-180">
            <ChevronDown className="size-4 shrink-0 transition-transform duration-200" />
            {category}
          </CollapsibleTrigger>
          <CollapsibleContent className="ml-4 space-y-1">
            {items.map((item) => (
              <Collapsible key={item.id}>
                <CollapsibleTrigger className="w-full rounded-md px-3 py-1.5 text-left text-xs text-sidebar-foreground/80 hover:bg-sidebar-accent">
                  {item.question}
                </CollapsibleTrigger>
                <CollapsibleContent>
                  <p className="px-3 py-2 text-xs text-sidebar-foreground/60">
                    {item.answer}
                  </p>
                </CollapsibleContent>
              </Collapsible>
            ))}
          </CollapsibleContent>
        </Collapsible>
      ))}
    </div>
  )
}