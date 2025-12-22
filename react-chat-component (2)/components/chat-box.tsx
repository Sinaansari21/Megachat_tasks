"use client"

import type React from "react"

import { useState, useRef, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Send, MessageCircle } from "lucide-react"

interface Message {
  id: string
  text: string
  sender: "user" | "system"
  timestamp: Date
}

export function ChatBox() {
  const [messages, setMessages] = useState<Message[]>([])
  const [inputValue, setInputValue] = useState("")
  const messagesEndRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages])

  const handleSendMessage = () => {
    if (!inputValue.trim()) return

    // Add user message
    const userMessage: Message = {
      id: `user-${Date.now()}`,
      text: inputValue,
      sender: "user",
      timestamp: new Date(),
    }

    setMessages((prev) => [...prev, userMessage])

    // Mock system response
    setTimeout(() => {
      const systemMessage: Message = {
        id: `system-${Date.now()}`,
        text: "سلام! پیام شما دریافت شد. این یک پاسخ نمونه از سیستم است.",
        sender: "system",
        timestamp: new Date(),
      }
      setMessages((prev) => [...prev, systemMessage])
    }, 500)

    // Clear input
    setInputValue("")
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") {
      handleSendMessage()
    }
  }

  return (
    <div className="w-full max-w-3xl mx-auto flex flex-col h-[700px] bg-card/80 backdrop-blur-xl border border-border/50 rounded-2xl shadow-2xl overflow-hidden">
      <div className="relative bg-gradient-to-r from-primary/10 via-primary/5 to-transparent border-b border-border/50 px-6 py-4">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-primary/10 rounded-xl">
            <MessageCircle className="h-5 w-5 text-primary" />
          </div>
          <div>
            <h2 className="text-lg font-semibold text-foreground">گفتگو</h2>
            <p className="text-xs text-muted-foreground">آنلاین</p>
          </div>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto px-6 py-6 space-y-4 bg-background/40">
        {messages.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full text-center space-y-3">
            <div className="p-4 bg-muted/50 rounded-2xl">
              <MessageCircle className="h-12 w-12 text-muted-foreground/50" />
            </div>
            <div>
              <p className="text-sm font-medium text-foreground">پیامی وجود ندارد</p>
              <p className="text-xs text-muted-foreground mt-1">مکالمه را با ارسال پیام شروع کنید</p>
            </div>
          </div>
        ) : (
          <>
            {messages.map((message) => (
              <div
                key={message.id}
                className={`flex ${message.sender === "user" ? "justify-end" : "justify-start"} animate-in fade-in slide-in-from-bottom-2 duration-300`}
              >
                <div
                  className={`max-w-[75%] rounded-2xl px-5 py-3 shadow-sm ${
                    message.sender === "user"
                      ? "bg-primary text-primary-foreground rounded-br-md"
                      : "bg-card text-card-foreground border border-border/50 rounded-bl-md"
                  }`}
                >
                  <p className="text-sm leading-relaxed text-pretty">{message.text}</p>
                  <span
                    className={`text-xs mt-2 block ${message.sender === "user" ? "opacity-80" : "text-muted-foreground"}`}
                  >
                    {message.timestamp.toLocaleTimeString("fa-IR", {
                      hour: "2-digit",
                      minute: "2-digit",
                    })}
                  </span>
                </div>
              </div>
            ))}
            <div ref={messagesEndRef} />
          </>
        )}
      </div>

      <div className="border-t border-border/50 px-6 py-4 bg-card/60 backdrop-blur-sm">
        <div className="flex gap-3 items-end">
          <div className="flex-1 relative">
            <Input
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="پیام خود را بنویسید..."
              className="h-12 px-5 bg-background/80 border-border/70 rounded-xl focus:ring-2 focus:ring-primary/30 focus:border-primary transition-all text-sm"
              dir="rtl"
            />
          </div>
          <Button
            onClick={handleSendMessage}
            disabled={!inputValue.trim()}
            className="h-12 w-12 rounded-xl shadow-lg transition-all hover:scale-105 disabled:opacity-50 disabled:hover:scale-100"
          >
            <Send className="h-5 w-5" />
          </Button>
        </div>
      </div>
    </div>
  )
}
