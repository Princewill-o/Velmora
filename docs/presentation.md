# Velmora: ten-minute assessment walkthrough

Use the local preview at `http://localhost:4187/#/`. Keep this explicit: the storefront, AI integration and campaign are an assessment concept, not a live shop.

## Run of show

**0:00–1:00 | The business problem.** The brief describes a one-year-old London eveningwear label: 48 made-to-order pieces, 760 Instagram followers and no reviews. Mobile confidence and delivery certainty matter more than a blanket discount. Paid social currently loses contribution before fulfilment overhead.

**1:00–3:30 | Home and Black Friday story.** Show the dark editorial home, the three chapter navigation and the scroll-linked Blender gown. Scroll or select Fabric and Your evening; point out that the camera, position, rotation and satin/crepe finish change. Open a hotspot. Explain J. Stimler’s full-bleed editorial cues and Palace’s direct category browsing as references, while all Velmora assets and brand design remain original. The yellow 20% feature applies to eight selected catalogue styles, with original prices available in the collection.

**3:30–5:00 | Collection and product.** Open the eight-piece sale edit, filter categories and inspect one product. Show catalogue facts, original/sale prices, sizes and colour choices, estimate, fit/care caveats and the no-guarantee language. Add a size to the bag; show subtotal and savings. The digital images and Blender models are illustrative studies, not verified product photography or fit previews.

**5:00–6:30 | Buying helper.** Use the deterministic occasion, budget, size and region/date filters. Show a real catalogue match and an impossible date/no-match state. Optional AI parses only explicitly stated occasion, budget and UK size; deterministic catalogue logic returns every product and price. Without server credentials, the AI explains it is unavailable and the filters still work. No API key is shipped to the browser.

**6:30–8:30 | Money and plan.** Walk through the one-page plan. Instagram mobile converts at 0.35% (56/16,027) versus 1.19% desktop; 56 of 478 mobile checkouts complete. Paid social returns 1.25× ROAS. At 55% gross margin, £3,376 revenue contributes £1,856.80 before other costs; subtracting £2,700 ad spend leaves **−£843.20**. Gross-margin-only break-even is 1.82× ROAS, and actual break-even is higher after fees, shipping and returns. Data describes association, not causation.

**8:30–9:30 | What to cut.** Cut blanket discounts, invented reviews or urgency, an unconstrained chatbot, paid-social scale before checkout diagnosis, and any delivery promise unsupported by the catalogue. A 20% discount reduces gross profit to 43.75% of discounted revenue before marketing and fulfilment. Respect the 20-piece weekly studio cap and backlog.

**9:30–10:00 | Validation and next step.** Fifteen automated checks pass. REA captures covered desktop and mobile, story navigation, mobile menu, sale collection and studio without page errors. Browser capture did show a non-fatal Three.js GPU precision warning. To launch, attach the repository to Git, deploy using the included Netlify configuration, set optional server-side AI environment variables, connect the real commerce system, and validate actual product measurements, margins, shipping and capacity.

## Likely questions

- **Is it live?** No. The catalogue and local bag work; checkout and payment are not connected. No public host or repository remote is configured in this workspace.
- **Does it promise fit or arrival?** No. Supplied sizes and calendar-day lead estimates are displayed; measurements, carrier cost and exact dispatch dates are unavailable.
- **Does AI choose a dress or invent product facts?** No. It extracts preferences; the 48-row catalogue and deterministic filters supply product matches and prices.
- **Why these graphics?** No verified product photos were supplied. Original concept imagery and Blender models make the idea tangible while being clearly labelled.
- **What evidence supports a conversion lift?** None yet. Targets are hypotheses; measure with event QA and a holdout where the volume supports it.
