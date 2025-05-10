# SOCMINT Implementation Prompts + General Guidelines

# General Development Guidelines (Must-Follow)

1. **Only make the exact changes I request** — do not modify, remove, or alter any other code, styling, or page elements unless explicitly instructed. If my request conflicts with existing code or functionality, pause and ask for confirmation before proceeding. Always follow this rule.
2. **Before you generate any code**, explain exactly what you plan to do. Include affected files, components, and edge cases. Wait for my confirmation before proceeding.
3. **You are my AI pair programmer.** I want to build [FEATURE]. Break this into steps and outline a build plan. Label each step clearly and tell me when you're ready to begin. Wait for my go-ahead.
4. **Generate a reusable UI kit** using [ShadCN / Tailwind / Custom CSS]. Include button styles, typography, input fields, and spacing tokens. Keep it consistent, clean, and minimal.
5. **Generate a complete test suite** for this function/module. Include edge cases, invalid inputs, and expected outputs. Label each test and include comments explaining the logic.
6. **Profile this code for bottlenecks.** Suggest two optimizations labeled 'Option A' and 'Option B' with trade-offs. Focus on real-world scenarios, not micro-optimizations.
7. **Write a complete README** for this project, including installation, usage, commands, and deployment steps. Assume the reader is a solo indie dev. Add emoji callouts if helpful.Also, include Arabic.
8. **Generate a clean, responsive HTML + CSS starter** with no dependencies. Include a homepage, about page, and contact form. Design should be minimalist, centered layout, mobile-first.