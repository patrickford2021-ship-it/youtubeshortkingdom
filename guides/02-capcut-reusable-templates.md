# Guide 2 — Reusable CapCut Templates (Quote Card, Score Graphic, Ranking Board)

Goal: build each graphic **once**, perfectly, then copy it into every video and only change the words/numbers. That's how you keep the series consistent and cut edit time in half.

Assumes **CapCut desktop** (long-form is much easier there). If you're on mobile, tell me and I'll adjust the steps.
Colors and fonts come from `00-brand-style-sheet.md` — have it open.

---

## The system: one "Master Graphics" project

CapCut doesn't have a great built-in way to save multi-layer graphics as templates, so we use the trick editors use: **a project whose only job is to hold your templates.**

1. Create a new project. Name it **`_MASTER GRAPHICS 16x9`**. Set the ratio to **16:9**.
2. Create a second one: **`_MASTER GRAPHICS 9x16`** for Shorts. (Build 16:9 first; you'll adapt later.)
3. Inside the master, lay your templates out one after another on the timeline, each 5 seconds long, with a 1-second gap between them:
   `[Quote Card] gap [Score Graphic] gap [Ranking Board] gap ...`
4. **To use a template:** open the master, select every layer of that template (drag a box around them on the timeline), copy, open your video project, paste. Then edit the text.
5. **Never edit the master while working on a video.** If you improve a template, update the master on purpose, and note it in the changelog at the bottom of this file.

Two shortcuts that help:
- **Text style presets:** after styling a text box, look for "Save preset" / "Save as preset" in the text panel. Save `QUOTE TEXT`, `EP TITLE`, `SCORE NUMBER`, `LABEL`. Now any new text box is one click from on-brand.
- **Compound clip:** select all layers of one template → right-click → **Create compound clip**. It becomes one tidy block you can copy around. Double-click to get inside and change text. (Use this once a template is final.)

✅ **Check:** you have both master projects created and the brand sheet open.

---

## Template A — Quote Card

What it looks like (16:9):

```
┌──────────────────────────────────────────────┐
│                                              │
│   "                                          │
│     Short quote text, one or two lines.      │
│                                         "    │
│                       — CHARACTER NAME       │
│   S01E03 · Mr. Lahey's Got My Porno Tape!    │
└──────────────────────────────────────────────┘
```

Build it, one layer at a time (bottom layer first):

1. **Background:** add a solid color — Asphalt `#14161A` — 5 s long. (Media → Library/Stock → solid color, or any plain image recolored.)
2. **Texture (optional but nice):** a subtle grain or paper texture overlay at 10–15% opacity. Makes it feel less "PowerPoint." Search stock for "film grain" or "paper texture."
3. **Panel:** add a shape (rectangle) in Trailer Siding `#23262D`, about 80% of the screen width, centered. Rounded corners if your version allows.
4. **Big quote marks:** text box with just `"` in Bebas/Anton, size ~300, Neon Yellow `#FFD23F`, top-left of the panel. Duplicate it for the closing mark, bottom-right.
5. **Quote text:** body font, size 60–72, Paper White, centered, **max 2 lines**. Type a placeholder like `QUOTE GOES HERE`. Save its style as preset `QUOTE TEXT`.
6. **Attribution:** `— CHARACTER` in the heading font, size ~48, Teal `#3FB8AF`, right-aligned under the quote.
7. **Episode tag:** `S00E00 · Episode Title` in body font, size 36–40, Ashtray Grey, bottom-left. Save as preset `LABEL`.
8. **Animation (In only):**
   - Panel: *Fade in*, 0.3 s.
   - Quote marks: *Zoom in / Pop*, 0.3 s, starting 0.2 s after the panel.
   - Quote text: a **typewriter** or **word-by-word** text animation, timed to finish about when you finish saying the line in the voiceover. This is the "animated quote card" feel.
   - Attribution + episode tag: *Fade in*, 0.3 s, after the quote finishes.
9. Select all layers → **Create compound clip** → rename `TPL Quote Card`.

**Using it:** paste → double-click in → change quote, character, episode tag → stretch to match the VO.

**Rules:** keep quotes short (one line of dialogue, not a whole exchange). Spell swears with asterisks on screen (`f**k`). Never put an actor's photo on the card — the character name is enough. If you want a visual, use the character card illustration (built later).

✅ **Check:** paste it into a blank project, change the text to a real quote from your notes, play it. Readable on your phone? Done.

---

## Template B — Score Graphic

The verdict moment. Viewers will learn to wait for it, so it should feel like a payoff.

```
┌──────────────────────────────────────────────┐
│  S01E03                                      │
│  MR. LAHEY'S GOT MY PORNO TAPE!              │
│                                              │
│  HUMOR            ████████░░   8             │
│  STORY / SCHEME   ███████░░░   7             │
│  CHARACTERS       █████████░   9             │
│  QUOTABILITY      ████████░░   8             │
│  REWATCHABILITY   ███████░░░   7             │
│                                   ┌───────┐  │
│                                   │ 39/50 │  │
│  Fans (IMDb): 8.0                 └───────┘  │
└──────────────────────────────────────────────┘
```

Build:

1. **Background + panel** — copy them from the Quote Card (consistency for free).
2. **Header:** `S00E00` (LABEL preset, Teal) and the episode title (heading font, size 70–90, Paper White) top-left.
3. **Category labels:** five text boxes, heading font, size ~44, Paper White, stacked left: HUMOR, STORY / SCHEME, CHARACTERS, QUOTABILITY, REWATCHABILITY.
4. **Score bars** (this is the new skill — keyframes):
   - For each category add a thin rectangle (track) in Trailer Siding, and on top of it a rectangle (fill) in Neon Yellow, same height.
   - Select the **fill** bar. Move the playhead to where you want it to start → in the right panel, set its width (Scale X, or Scale with the lock off) to ~0 and **add a keyframe** (the little diamond).
   - Move the playhead 0.5 s later → stretch the bar to its score (score 7 = 70% of the track length) → CapCut adds the second keyframe automatically.
   - Tip: set the **anchor/position** so it grows from the left, not the center. If yours grows from the center, keyframe its position too so the left edge stays put.
   - Stagger the five bars 0.15 s apart so they fill like a cascade.
5. **Number next to each bar:** heading font, size ~60. Pop in when its bar finishes.
6. **Total box:** a Neon Yellow rounded rectangle with `39/50` in heading font, size 200+, Asphalt color text. It slams in last (*Zoom in*, 0.3 s) — add a short "thud" or "ding" sound effect under it.
   - Color the total box using the score color rules from the style sheet (40+ yellow, 30s teal, 20s grey, under 20 red).
7. **Fan score (small, bottom-left):** `Fans (IMDb): 8.0` in LABEL style, Ashtray Grey. This is where you show agreement/disagreement with the fandom — it's a hook in itself ("Fans gave this an 8. I'm about to disagree.").
8. Compound clip → `TPL Score Graphic`.

**Updating per episode:** change the text, then on each fill bar move the *second* keyframe's width to the new score. That's the only fiddly part; it takes ~2 minutes once you've done it twice.

**Shorts version:** stack it vertically — title on top, bars in the middle, total huge at the bottom-center, above the 350 px danger zone.

✅ **Check:** build one with fake scores (8/7/9/8/7). Bars should grow left-to-right, total should land last.

---

## Template C — Season Ranking Board

The heart of the season videos. Same board every season so the series feels connected.

```
┌──────────────────────────────────────────────┐
│ SEASON 1 · EVERY EPISODE RANKED              │
│ ┌──┬────────────────────────────────┬─────┐  │
│ │ 1│ ??????                          │  ?? │  │
│ │ 2│ ??????                          │  ?? │  │
│ │ 3│ Mrs. Peterson's Dog Gets F**ked │  41 │  │
│ │ 4│ Mr. Lahey's Got My Porno Tape!  │  39 │  │
│ │ 5│ ...                             │  .. │  │
│ │ 6│ ...                             │  .. │  │
│ └──┴────────────────────────────────┴─────┘  │
└──────────────────────────────────────────────┘
```

Why it works: you count **worst to best**, so the board fills from the bottom up and the top slots stay hidden as `??????`. Every time you return to the board, viewers see their favorite hasn't shown up yet → they keep watching.

Build (for a 10-row board; delete rows for shorter seasons — S1 has 6):

1. **Background + header:** Asphalt background. Header text `SEASON X · EVERY EPISODE RANKED` in heading font, Neon Yellow, top-left.
2. **One row first** (then duplicate it):
   - Row panel: rectangle, Trailer Siding `#23262D`, full width minus margins, height ~80 px (10 rows) or ~120 px (6 rows).
   - Rank number: heading font, Neon Yellow, left.
   - Title: body font, size ~40, Paper White, short titles only — abbreviate long ones (`Who the Hell Invited These Idiots…`).
   - Score: heading font, right-aligned, colored by the score color rules.
3. **Group the row** (compound clip) → duplicate it down the screen until you have all rows. Space evenly.
4. **Hidden state:** for unrevealed rows, title = `??????` and score = `??`, at 50% opacity.
5. **Reveal animation:** when an episode is revealed, the row's text swaps from `??????` to the real title. Easiest method: put the "hidden" row and the "revealed" row on top of each other; cut the hidden one at the reveal point; give the revealed one a 0.3 s *Fade/Slide in* + a quick white flash on the panel.
6. **The board appears multiple times** in a season video (after each episode segment). Build the full board once, then for each appearance, copy it and change only which rows are revealed. Keep a copy of each state in the project labeled `Board after #6`, `Board after #5`...
7. **Optional but great — the all-time leaderboard version:** same design, header `ALL-TIME LEADERBOARD`, top 10 across every season so far, with a small `S03` tag on each row. Shows up at the end of each season video to show where the new season's episodes landed. The dashboard tracks this list for you.

✅ **Check:** build a 6-row board for Season 1 with every row hidden, then reveal row 6. Does the reveal feel satisfying at full speed? If it's slow, shorten the animation.

---

## Changelog (update when you change the master)

| Date | Template | Change |
|---|---|---|
| | | |
