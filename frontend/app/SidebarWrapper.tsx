"use client"

import { useState } from "react"
import { Menu, X } from "lucide-react"
import SidebarClient from "./SidebarClient"

export default function SidebarWrapper() {
  const [open, setOpen] = useState(false)

  return (
    <>
      <button
        onClick={() => setOpen(true)}
        className="fixed left-4 top-3 z-50 rounded-md p-1.5 text-sidebar-foreground hover:bg-sidebar-accent md:hidden"
      >
        <Menu className="size-5" />
      </button>

      {open && (
        <div
          className="fixed inset-0 z-40 bg-black/40 md:hidden"
          onClick={() => setOpen(false)}
        />
      )}

      <aside
        className={`
          fixed inset-y-0 left-0 z-50 flex w-72 flex-col border-r bg-sidebar transition-transform duration-200
          md:static md:translate-x-0
          ${open ? "translate-x-0" : "-translate-x-full"}
        `}
      >
        <div className="flex items-center justify-between border-b px-4 py-3">
          <span className="font-semibold text-sidebar-foreground">TokoFiktif</span>
          <button
            onClick={() => setOpen(false)}
            className="rounded-md p-1 text-sidebar-foreground hover:bg-sidebar-accent md:hidden"
          >
            <X className="size-4" />
          </button>
        </div>
        <div className="flex-1 overflow-auto p-2">
          <SidebarClient />
        </div>
      </aside>
    </>
  )
}