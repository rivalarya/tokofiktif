import type { Metadata } from "next";
import SidebarWrapper from "./SidebarWrapper";
import "./globals.css";

export const metadata: Metadata = {
  title: "TokoFiktif",
  description: "TokoFiktif Customer Service",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="id">
      <body className="flex h-screen overflow-hidden">
        <SidebarWrapper />
        <div className="flex flex-1 flex-col">
          <header className="flex items-center justify-end gap-4 border-b px-6 py-3 md:px-6">
            <div className="flex-1 md:hidden" />
            <a
              href="https://rival.my.id/case-study/why-you-dont-need-a-bigger-model"
              target="_blank"
              rel="noopener noreferrer"
              className="text-sm text-muted-foreground hover:text-foreground underline underline-offset-2"
            >
              Case Study
            </a>
            <a
              href="https://github.com/rivalarya/tokofiktif"
              target="_blank"
              rel="noopener noreferrer"
              className="text-sm text-muted-foreground hover:text-foreground underline underline-offset-2"
            >
              GitHub
            </a>
          </header>
          <main className="flex-1 overflow-auto">{children}</main>
        </div>
      </body>
    </html>
  );
}