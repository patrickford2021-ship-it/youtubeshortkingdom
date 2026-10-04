# Fandom Research Plan

## What's already in episodes.json (pulled 2026-10-04)
- Titles, air dates, synopses: Wikipedia episode list.
- IMDb rating + vote count for all 105 episodes and the 10 specials/films.
  - Heads-up on numbers: IMDb treats the Xmas special as S4E9; we treat it as a special.
  - Live at Red Rocks only has 44 votes — don't cite it as "fan consensus."

## What's NOT filled in yet (on purpose)
- `reddit_sentiment` is null for every episode. It will only be filled from actual threads, never guessed.
- Plan: before each **season** video, pull the top r/trailerparkboys "best/worst episode of Season X" and "ranking" threads, and record per episode: `loved / mixed / disliked / rarely mentioned` + one-line why, with thread links in `reddit_notes`.
- Do this AFTER you've scored that season, so it informs the "me vs. the fans" angle without steering your opinions.

## Fan-score quick look (IMDb only, not Reddit)
Highest-rated by season per IMDb (useful for "going against the fans" hooks later — but hidden on the dashboard until you score):
- Season 3 E5 "Closer to the Heart" (9.2) and S12E10 (9.2) are the top-rated episodes on IMDb overall.
- Netflix-era seasons (8–12) generally rate lower on IMDb than the original run (1–7); S10 is the lowest-rated season.
