# Shop and Blender update

The user requested a clothing-business UI informed by Palace, with Three.js clothing and Blender authoring.

## UI reference

The public [Palace homepage](https://palaceskateboards.com/) and [collection](https://palaceskateboards.com/collections/all) were inspected through their public HTML and CSS. The useful ideas were direct category browsing, large garment imagery, concise labels and a strong editorial hierarchy. Velmora's implementation uses a full-screen directory, bold home typography, a four-column desktop/two-column mobile catalogue and clear sale pricing. No Palace products, logos, photography or proprietary font files were copied into the site.

## Original Blender work

- Source: `art/build_clothes.py`, `art/models/velmora-garments.blend`.
- Models: `public/models/draped-gown.glb`, `public/models/structured-gown.glb`, `public/models/evening-blazer.glb`.
- Inspected renders: `art/renders/`.
- Blender: portable 4.5.2, official release download, verified SHA256 `a24ec8dc2ee097294624f90e210c3528da5624320460f03270a387ca22a33734`.

The gowns include hollow fabric surfaces, thickness, straps or a structured neckline, pleats and seam details. The blazer includes sleeves, shoulder panels, notched lapels, welt-pocket details and a brass button. The source is editable. These are illustrative garment studies, not production patterns, body scans or exact representations of supplied catalogue pieces.

## Three.js integration

GLTFLoader loads the original Blender exports, centres and scales each garment, and exposes selection of three models. The material controls change the satin material while preserving the separate lining and hardware. The existing rotation, zoom, reset, reduced-motion and pause controls remain available. Scene resources and superseded loads are disposed when navigating or changing garments.

The Black Friday concept still uses the user-selected 20% offer on eight IDs; all effective prices come from one function.

## Verification

Node tests exercise sale prices, budget filtering, product choices, quantity changes, persisted bags and loading each GLB in Three.js. Blender render outputs were inspected and the shoulder construction refined. REA Chromium captures verified desktop and mobile home, story chapter navigation, the mobile menu to the sale edit, a mobile product page, the collection and the studio. Captures completed without page errors or failed HTTP responses. Chromium emitted a non-fatal GPU precision warning during WebGL compilation; no accessibility or performance score is claimed.
