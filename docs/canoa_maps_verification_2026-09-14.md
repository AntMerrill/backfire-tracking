# Canoa, Ecuador — map/satellite/street-level verification

John asked to pull a Google Maps overview of Canoa to check his own
observation: no bridges or highways in the town itself, and to locate "the
crappy little park" and a hill with an antenna behind a playground, for
comparison against footage used in Ballard's produced videos. This session
has no browser tool connected (Claude-in-Chrome needs a manual reconnect
click, per standing notes), so Google's static map and Street View
endpoints were tried first and both rejected the request outright (`403`,
API key required — Google locked these down since they used to work
key-free). Fell back to three key-free sources instead: **Yandex Maps'
static API** (satellite/road tiles), **OpenStreetMap's Nominatim and
Overpass APIs** (place/feature data), and **KartaView** (crowdsourced
street-level photos, the closest available substitute for Street View).
Nine images saved total, every request logged below so this can be
re-verified or redone against Google directly whenever browser access is
available.

## Satellite imagery — how each image was pulled

Plain HTTP GET, no authentication, via `curl`, against
`static-maps.yandex.ru`. Coordinates in `ll=lon,lat` order (Yandex's
convention, not the usual lat,lon).

- **`01_canoa_overview_z14_satellite.jpg`** —
  `?ll=-80.4667,-0.4667&z=14&l=sat&size=650,450`
  Wide view: Canoa reads as a thin ribbon of buildings hugging the beach,
  farmland/tree cover on both sides, ocean to the west. Imagery credited
  on-frame to "Airbus DS 2017."
- **`02_canoa_overview_z14_labeled.png`** — same center/zoom, road layer
  (`l=map`) instead of satellite — mostly blank at this zoom, only useful
  for the "посёлок Canoa / Canoa" label confirming the location.
- **`03_canoa_highway_approach_z16_satellite.jpg`** —
  `?ll=-80.4467,-0.4767&z=16&l=sat&size=650,450`
  South of the town core: a single two-lane paved road (Ecuador's coastal
  "Ruta del Spondylus") running through farmland/forest, meeting a
  roundabout near the coast — the regional highway that reaches Canoa from
  outside, not a road inside the town.
- **`04_canoa_town_center_z16_satellite.jpg`** —
  `?ll=-80.4543,-0.4603&z=16&l=sat&size=650,450`
  Coordinates estimated from image 01's pixel offset, not looked up —
  landed correctly on the town core. Shows the street grid: a compact,
  small-town layout, a narrow river/estuary channel cutting in from the
  north edge, shrimp ponds/farmland north of that, and the same paved
  coastal road passing along the town's east side rather than through its
  center.
- **`05_canoa_best_overview_z17_park_pinned.jpg`** —
  `?ll=-80.4548,-0.4615&z=17&l=sat&size=650,450&pt=-80.4540703,-0.4607513,pm2rdl`
  Zoom 17 is the max Yandex will serve for this location (18 and 19 both
  `404` — no imagery at that resolution from this provider here). Pin
  dropped on the OSM-tagged park center. A compass arrow was added
  afterward (top-left, via Pillow) — Yandex's static endpoint has no
  rotation/bearing parameter, so every tile it serves is already north-up
  by construction; marked that explicitly rather than leaving it implicit.
- **`06_canoa_best_overview_z17_clean.jpg`** — identical view, no pin, for
  an unobstructed look at the same block.
- **`07_canoa_bridge_antonio_aveiga.jpg`** —
  `?ll=-80.4546273,-0.4598545&z=17&l=sat&size=650,450&pt=-80.4546273,-0.4598545,pm2grl~-80.4494409,-0.4594024,pm2blm`
  Centered on the Antonio Aveiga bridge (see below); a paved road is
  directly visible crossing the river at that point.

All satellite images pulled 2026-09-14, session-local time ~09:30–09:45
Pacific.

## What OpenStreetMap has for Canoa

Queried Overpass (`overpass-api.de/api/interpreter`, no key required) for
every named node/way in a box roughly covering the town
(`-0.478,-80.468,-0.452,-80.443`) — 153 results. Highlights:

- **38 named residential streets**, including "Malecón de Canoa" (the
  beachfront promenade) — a mapped street grid, not an empty area.
- **Businesses**: 22 restaurants, 17 hotels, 7 hostels, 5 bars, several
  bakeries/convenience stores/pharmacies — a small, active tourist town, not an empty one.
- **2 schools, 2 places of worship** (a Catholic church, a Kingdom Hall), a
  cemetery.
- **Recreation**: a paragliding operator ("Opetumo . Parapente Canoa"), a
  hang-glider launch point tagged on a clifftop, a campsite.
- **2 rivers**: "Río Canoa" and "Río Muchacho."
- **1 communications mast**, operator "Claro" (a regional telecom
  carrier) — `-0.4652198, -80.4506969`, south of the town core, on the
  higher/forested ground visible in image 09 below.
- **Playground**: nothing tagged `leisure=playground` anywhere in this
  area. There's a second, unnamed `leisure=park` way ("cA" — reads like a
  data-entry artifact, not an actual name) at `-0.4618928, -80.4517494`,
  ~380m from the antenna mast, next to what the satellite shows as a small
  painted plaza/court at the town's southern edge — the closest match to
  "playground" OSM has, but not confirmed as one under that tag.

## The park

Nominatim (`nominatim.openstreetmap.org/search?q=parque+Canoa+Ecuador`, no
key required) turns up exactly one tagged park in the whole town:

> **Parque Central**, Canoa, San Vicente, Manabí, Ecuador — `leisure=park`,
> center approx. -0.46075, -80.45407, bounding box roughly 40m &times; 65m.

That tiny bounding box matches "crappy little park" — not a proper
green-space park, a small clearing/plaza wedged into the street grid near
the river mouth. Its location is pinned in `05_canoa_best_overview_z17_park_pinned.jpg`.

## Correction: there are bridges

Queried Overpass again, this time specifically for `bridge=yes` ways in a
tighter box. **This corrects the earlier read of "nothing resembling a
bridge"** — OSM has four:

| Name | Road class | Center (lat, lon) | Distance from Parque Central |
|---|---|---|---|
| Antonio Aveiga | tertiary | -0.4599, -80.4546 | ~150m — inside the town grid |
| (unnamed) | footway | -0.4596, -80.4539 | ~150m — inside the town grid |
| (unnamed) | footway | -0.4606, -80.4579 | ~400m, near the beach/river mouth |
| Troncal del Pacífico | **trunk** | -0.4594, -80.4494 | ~500m east — the regional highway |

Image 07 is centered on the Antonio Aveiga bridge: a paved road is directly
visible crossing the river right at that point, connecting the town's
street grid to the road heading north. Not a large structure, but a
confirmed, in-town bridge — not something confined to the outskirts like the
trunk-highway crossing.

The same broader query also confirmed **"Troncal del Pacífico"** as a named
`highway=trunk` way passing near the town, so "no highways at all" doesn't
hold either once the regional trunk road is counted. What still holds: no
highway or bridge inside the town rises to the scale suggested by
aerial/drone-style shots like the ones spliced into Video B or the "Hidden
War" trailer's Ukraine b-roll — everything found here is small-town scale
(a two-lane road, a footbridge), not the multi-lane infrastructure that
kind of footage implies.

## Street-level imagery — KartaView, since Street View is blocked

Google's Street View Static API returned the same `403` as the maps
endpoint. **KartaView** (formerly OpenStreetCam, crowdsourced dashcam
photos, CC BY-SA 4.0, no key required for read access via
`api.openstreetcam.org`) has coverage here: a single driving sequence
(`sequenceId 992431`) shot **2017-12-27**, with over 1,600 frames through
the area. Only pulled the frames nearest the two points of interest so far
— this sequence has far more in it if a specific angle is needed later.

- **`08_kartaview_park_area_2017-12-27.jpg`** — photo id `184532089`, shot
  at `-0.461104, -80.454292` (right at Parque Central), heading 10.63°
  (facing roughly north), 18:56:50 local time. Shows a paved road with
  painted lane markings, a small colorful plaza/playground area (yellow,
  red, and purple-painted curbs, a bench, play structures visible past the
  palm trees) — this is very likely the "crappy little park"/playground
  area itself, at ground level. A hill is visible on the far left horizon.
- **`09_kartaview_near_antenna_mast_2017-12-27.jpg`** — photo id
  `184532015`, shot at `-0.465844, -80.454165` (near the Claro mast),
  heading 251.42° (facing WSW, i.e. away from the mast, not toward it),
  18:55:52 local time. Shows a paved residential street running toward low
  hills on the horizon, power lines, and a green tsunami-evacuation sign —
  useful streetscape context, but this specific frame doesn't capture the
  antenna itself.

**Not yet found:** a single frame that cleanly frames "the hill behind the
playground with an antenna" the way John described it from the fake
videos. The two frames above are the closest hits from a point-radius
search against the two coordinates of interest; the full 1,600+-frame
sequence hasn't been walked frame-by-frame to find a better-angled shot,
and the sequence-pagination endpoint that would make that practical
returned inconsistent results this session (worth retrying).

## What this does and doesn't establish

- **Confirms the substance of John's original point:** no highway
  interchange, and nothing resembling large-scale bridge infrastructure,
  sits inside the town. But it's not literally true that there are zero
  bridges or zero highways anywhere near Canoa — there's a small in-town
  road bridge, two footbridges, and the regional coastal highway passing
  just east of town. The corrected claim is about scale, not absence.
- **The park and antenna are both specific, locatable things, not vague
  claims** —
  vague claims. Coordinates for both are in this doc and pinned on the
  satellite imagery.
- **Not Google** — satellite imagery is Yandex/Airbus DS (2017 credit,
  likely older than current Google imagery); street-level imagery is
  KartaView, a different, sparser crowdsourced dataset than Street View.
  Treat all of this as corroborating, not identical to, what a direct
  Google Maps + Street View check would show — worth redoing there
  directly once browser access is available.

## Source

- Images: `docs/assets/canoa_maps_2026-09-14/` (9 files, listed above with
  exact request URLs/IDs).
- APIs used: `static-maps.yandex.ru` (satellite/road tiles),
  `nominatim.openstreetmap.org` (place search),
  `overpass-api.de/api/interpreter` (feature queries),
  `api.openstreetcam.org` + `cdn.kartaview.org` (street-level photos, CC
  BY-SA 4.0).
- Feeds into: `senate_testimony_canoa_2026-09-14.md` (this repo),
  `veritastimmy/docs/ecuador_house_comparison_2026-09-12.md` (Video B's
  unpaved street, consistent with image 08 here).
