# Sales Performance Analysis Project

This project tracks and improves sales calls for Berlin, an AI-powered SEO automation platform.

## Files & Structure

- **`sales_bible.md`** - Master reference guide for sales calls. Contains call framework, questions, positioning strategies, and learning log from previous calls.

- **`transcripts/`** - Directory containing sales call transcripts converted to text format. Files named by prospect and company.

- **`llm_instructions.prompt`** - Instructions for LLMs analyzing call transcripts. Defines analysis framework and bible update procedures.

## Workflow

1. Add new call transcript to `/transcripts/` directory
2. Run LLM analysis using `llm_instructions.prompt` as context
3. Update `sales_bible.md` with learnings and improvements
4. Use updated bible for next call preparation

## Goal

Create a continuously improving sales process where each call makes the next one more effective through documented learnings and refined strategies.