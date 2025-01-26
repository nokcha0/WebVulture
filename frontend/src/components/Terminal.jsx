import React, { useEffect, useState } from "react";
import { fetchEventSource } from "@microsoft/fetch-event-source";

export default function Terminal() {
  const [messages, setMessages] = useState([""]);

  useEffect(() => {
    let isSubscribed = true;

    const fetchData = async () => {
      await fetchEventSource("http://127.0.0.1:8000/stream", {
        onmessage(ev) {
          if (isSubscribed) {
            console.log(`Received event: ${ev.data} ${ev.event}`);
            setMessages((prev) => [...prev, ev.data]);
          }
        },
        onerror(err) {
          console.error("EventSource failed:", err);
        },
      });
    };
    fetchData();

    return () => {
      isSubscribed = false; // Cleanup function to avoid double effects
    };
  }, []);

  return (
    <div className="terminal-container">
      <div className="terminal-header">
        <span className="terminal-title no-select-text">Terminal</span>
      </div>

      <div
        className="terminal-body"
        style={{
          overflowY: "auto",
          maxHeight: "400px",
          border: "1px solid #ccc",
          padding: "10px",
          fontFamily: "monospace",
        }}
      >
        {messages.map((msg, index) => (
          <p key={index} style={{ margin: "5px 0", whiteSpace: "pre-wrap" }}>
            {msg}
          </p>
        ))}
      </div>
    </div>
  );
}
