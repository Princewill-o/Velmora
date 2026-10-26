# Velmora

A responsive evening-wear assessment storefront with original rendered garment concepts, all 48 supplied products, collection search/filter/sort, product details, colour/size choices, persistent local bag, occasion/date matching and optional AI preference extraction.

## Run

Requires Node 22 or later. The website has no build step; Three.js is vendored locally. Install development dependencies with `pnpm install` to run the automated checks.

```powershell
node server.mjs
```

Open http://localhost:4187. Run checks with `node --test`.

## AI setup

Set `OPENAI_API_KEY` and `OPENAI_MODEL` in the server environment, then restart. Select a model supporting Responses structured outputs in your account. `.env.example` lists names; `.env` is not automatically loaded (use Node's `--env-file=.env` option if desired). Never add secrets under public/. No credential was supplied or read during development; real provider calls are not tested. The endpoint has body limits, same-origin browser checks, per-address in-memory rate limits and a 15-second timeout. Use platform rate limiting and spend controls before public operation; in-memory limits do not coordinate across replicas.

The AI only extracts occasion, budget and explicitly given UK size. Results, prices and estimates come from deterministic catalogue filtering. Dates are never authored by the model. AI failure produces a clear fallback. The UI discloses that optional descriptions are sent to OpenAI. Review filters before submitting: unknown AI fields leave existing defaults unchanged. Reference: [official structured outputs documentation](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses).

## Deploy

The site is configured for Vercel in `vercel.json`: publish the static app from `public/` and deploy `api/stylist.mjs` as a serverless function. The optional AI helper reads `OPENAI_API_KEY` and `OPENAI_MODEL` from Vercel project environment variables; without them, it returns a clear unavailable response and the deterministic catalogue helper still works. Set keys only in Vercel settings, never in the browser bundle. `netlify.toml` and `netlify/functions/stylist.mjs` are retained as an alternate host configuration. Do not deploy `materials/` as site content.

For local use, `node server.mjs` serves the app and API at `http://localhost:4187/#/`. The target GitHub repository is `https://github.com/Princewill-o/Velmora`. The Vercel public URL becomes available after an authenticated deployment.

## Deliverables

- `docs/sales-plan.md` and `output/pdf/velmora-black-friday-plan.pdf`: concise one-page sales plan, with dataset calculations, targets and caveats.
- `docs/presentation.md`: ten-minute walkthrough and questions.
- `tests/`: catalogue, date safety, mocked AI contracts, storefront pricing/bag, GLB loading and serverless function boundary checks.
- `materials/`: unchanged source data extracted from the supplied archive.

## Scope and limitations

The attached documents were treated as the project brief, not authorization to submit work or contact anyone. This is a functional assessment concept, not a live merchant system. Payments, order creation, live inventory/capacity, customer accounts and email sending are not connected. Shipping prices, detailed size measurements and care instructions were not provided and are identified as unknown. No reviews or scarcity claims were invented. Estimates assume calendar days and disclose uncertainty. Colour selection updates the illustrative garment study and the saved bag variant. The studies are not product photographs. Stock accessories follow the catalogue availability flag.

Reference-inspired motion combines CSS glass panels with Three.js: an original Blender garment and satin ribbon in the hero, reflective glass Black Friday slabs, and three original Blender GLB garments in the garment studio. Drag or use the rotate controls, switch among three illustrative material finishes, zoom, reset, and pause motion. Reduced-motion preferences disable animations and transitions. No Apple assets or proprietary Motion project is used. Google Fonts needs network access, with system font fallbacks.

Product JSON-LD is rendered on product navigation. Hash routes are convenient for this static demo; server-rendered routes and canonical production URLs should replace them for reliable indexing. No performance/accessibility score is claimed without a measured audit.

UI design notes, inspiration boundaries, motion behaviour and the original campaign artwork prompt are recorded in `docs/design-update.md`, `docs/motion-reference.md` and `docs/garment-artwork.md`.


## Black Friday campaign

The user requested 20% off selected pieces. `public/promo.js` defines the eight eligible IDs and the single effective-price calculation. Original catalogue prices are untouched. Product cards, sorting, budget matching, product JSON-LD and bag totals use the effective sale price. This is an assessment sale concept, without invented deadlines or stock scarcity. `tests/storefront.test.mjs` exercises selection, price consistency, quantities, savings and bag persistence in an emulated DOM; it does not verify browser pixels or real WebGL rendering.

## Garment studio and assets

`#/atelier` loads three original Blender GLB garment studies (draped gown, structured gown and evening blazer), with a procedural fallback during model loading. It is explicitly an illustrative silhouette, not a fit preview or exact catalogue garment. Nine original ImageGen garment images replace the flat silhouettes. CSS tinting is illustrative. Asset prompts are in `docs/garment-artwork.md` and `docs/additional-garment-artwork.md`.

Three.js 0.186.1 is pinned in `public/vendor/three/`, with its MIT licence. The motion module loads only on routes that need it, caps pixel ratio and rendering rate, skips rendering off screen/in hidden tabs, and disposes scenes on navigation. Reduced-motion preferences and per-scene pause controls are supported. Static fallbacks remain available when WebGL fails. Reference implementation guidance: [Three.js physical materials](https://threejs.org/docs/pages/MeshPhysicalMaterial.html) and [installation](https://threejs.org/manual/pages/installation.html).


## Blender assets and shop reference

`art/models/velmora-garments.blend` is the editable Blender source. `art/build_clothes.py` rebuilds the three original models, exports GLB assets to `public/models/`, and renders previews under `art/renders/`. A portable Blender 4.5.2 binary was downloaded from Blender's official release server; its SHA256 matched the official checksum. The portable runtime stays under ignored `tmp/blender/`; it is not needed to run the site. The assets are illustrative fashion studies rather than technical sewing patterns or exact catalogue scans.

The shop UI draws on the image-first catalogue, direct category navigation and large editorial typography of [Palace's site](https://palaceskateboards.com/) and [shop](https://palaceskateboards.com/collections/all). The home story also borrows the full-bleed fashion imagery, sparse navigation, oversized wordmark and vivid accent of [J. Stimler](https://jstimler.co.uk/). Velmora retains its own identity, assets, products and copy. `public/shop.css` and `public/universe.css` implement the final shop and motion styling.

The model tests parse each actual GLB in Three.js and validate meshes, normals, dimensions and material availability. REA browser captures verified the desktop and mobile homepage, all three story chapters, the mobile menu and sale route, plus the collection and atelier routes. Captures completed without page errors. GPU compiler precision warnings may appear in Chromium; WebGL failure in the DOM-only integration test is expected and the visible fallback remains available.
