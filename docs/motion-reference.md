# Black Friday motion direction

The user supplied a 16.17-second reference video and an Apple-style glass UI image. The video was inspected at nine points across its duration: a floating garment hero transitions into a dark material workspace; fabric finishes change and the garment rotates from front to back. The image shows frosted surfaces, rounded panels, soft directional shadows and overlapping depth.

The implementation translates that behaviour into Velmora rather than copying the reference brand or Apple logo:

- Dark, full-screen homepage with a Blender GLB gown, original satin ribbon geometry, oversized typography and a clear 20% offer.
- Three.js scroll story with three chapters. Scroll progress changes story text, camera framing, garment position and rotation, and an illustrative satin-to-crepe material blend.
- Dedicated dark garment studio with three original Blender models, three material finishes, drag rotation, keyboard-accessible rotate buttons, zoom, reset and pause.
- Nine rendered transparent garment assets, with separate draped, wrap and structured dress concepts. All are labelled as digital concepts; they do not claim exact garment construction or fit.
- Original prices plus the user-selected 20% discount on eight explicit product IDs. Budget matching, price sorting, product structured data and bag totals share the effective-price function.

Three.js 0.186.1 is vendored with its licence. It loads only on routes with scenes. Rendering is capped at 30 fps and 1.5 device pixel ratio, skipped when off-screen or when the document is hidden, and disposed on navigation. Reduced motion starts the scene paused. Static content remains available if WebGL cannot start.

The home story and garment studio load actual rotating 3D mesh geometry from the Blender GLB exports; the floating ribbon is separate procedural geometry. The models are explicitly labelled illustrative design studies, not scans or fit previews of the catalogue pieces.

REA captured the public J. Stimler home page at the time of design and the supplied Cartier Roadster URL, which returned an access-denied response. The layout uses J. Stimler's image-led editorial composition as inspiration. No exact Roadster-specific animation was observable, so this implementation does not claim to reproduce one.

References used to implement the renderer: [Three.js physical materials](https://threejs.org/docs/pages/MeshPhysicalMaterial.html), [Three.js installation](https://threejs.org/manual/pages/installation.html).
