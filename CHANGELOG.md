# CHANGELOG


## v1.3.1 (2026-02-12)

### Bug Fixes

- Remove ws msg for cryto stdout, add doc TOC
  ([`d23fbae`](https://github.com/sadsfae/goldteeth/commit/d23fbaee9a398ac57bdfc756cbe805d0d4c0d4df))

### Chores

- Remove incorrect ws poll msg for crypto
  ([`4e95a74`](https://github.com/sadsfae/goldteeth/commit/4e95a7493837493d348e341907172c3264f2ba10))


## v1.3.0 (2026-02-12)

### Chores

- Minor doc update
  ([`07bb2c6`](https://github.com/sadsfae/goldteeth/commit/07bb2c6a2d48b25604133c1b8840f8b64358ab50))

- One more README update
  ([`a7e9957`](https://github.com/sadsfae/goldteeth/commit/a7e9957272c4ba09549a1089de92167eeac4087b))

- Update README
  ([`489348b`](https://github.com/sadsfae/goldteeth/commit/489348b55b1e338cd2f17faf10f82876b8f0bb92))

- Update UI image
  ([`9d82d82`](https://github.com/sadsfae/goldteeth/commit/9d82d822e3058631f1b710d30617d635839dc17f))

- **release**: V1.3.0 [skip ci]
  ([`9978d37`](https://github.com/sadsfae/goldteeth/commit/9978d37853c6320051334bd253655ccfc1a62cd7))

### Features

- Websocket recovery loop, fix stale data.
  ([`a986a5f`](https://github.com/sadsfae/goldteeth/commit/a986a5f8dfd0de243002be311eaf97a482763f88))

* Add websocket recovery loops to help with FINNHUB free API limits. * Add HTTP fallback mechanism.
  * Fix potential stale data bug when websocket crashed (due to API limits). This now resets last
  price to None. * Split out INTERVAL to CRYPTO_INTERVAL and STOCK_INTERVAL * Wrap websocket in
  permanent loop to try to work around stock API limits.


## v1.2.0 (2026-02-07)

### Chores

- **release**: V1.2.0 [skip ci]
  ([`5b25a26`](https://github.com/sadsfae/goldteeth/commit/5b25a2623bc49576939070900ab819a1627d39d2))

### Features

- Make GUI import env variables on launch.
  ([`056ac02`](https://github.com/sadsfae/goldteeth/commit/056ac0256f0451c1cd603461f718b893d86646bd))

* We now pull in (or update) env vars into os.environ on load * Minor refactor

- Simplify UI design
  ([`fb5420c`](https://github.com/sadsfae/goldteeth/commit/fb5420c5d59cd423fcd331fce95cd2eb77f20b19))

* only use one button * use a smaller activity window * shrink overall UI elements

- Support both no/free/paid coingecko API keys.
  ([`f1d454f`](https://github.com/sadsfae/goldteeth/commit/f1d454f66728fc3e2eba18ff045fac81397b0f41))

* Still supports no API key at all for crypto * Supports free/demo keys * Now supports paid plan API
  keys (uses different url)


## v1.1.1 (2026-01-29)

### Bug Fixes

- Update notification titles
  ([`32f24f3`](https://github.com/sadsfae/goldteeth/commit/32f24f3e125101f6e28680117cef8afdf791bbb3))

### Chores

- **release**: V1.1.1 [skip ci]
  ([`2587ab8`](https://github.com/sadsfae/goldteeth/commit/2587ab818f2b38226c4aed20884dc9b8fdc0f052))


## v1.1.0 (2026-01-23)

### Chores

- **release**: V1.1.0 [skip ci]
  ([`d58815c`](https://github.com/sadsfae/goldteeth/commit/d58815c3744110598d884a549a1c705cb1bfc6b4))

### Features

- Add .gitignore
  ([`a618fdd`](https://github.com/sadsfae/goldteeth/commit/a618fdd1e4c8c29e964075728814307802fcb230))


## v1.0.0 (2026-01-23)

### Chores

- **release**: V1.0.0 [skip ci]
  ([`1e96163`](https://github.com/sadsfae/goldteeth/commit/1e9616359df24bb6c5d1da62d0364fed4f53189b))

### Features

- Rework structure entirely.
  ([`4bc8f9e`](https://github.com/sadsfae/goldteeth/commit/4bc8f9e2c5a25179ba3fd055aa7a02214a3ebbca))

BREAKING CHANGE: structure changes, pypi now proper package not module.

### BREAKING CHANGES

- Structure changes, pypi now proper package not module.


## v0.1.10 (2026-01-23)

### Bug Fixes

- Pypi package location/refs
  ([`99843f0`](https://github.com/sadsfae/goldteeth/commit/99843f042caf4793f2e0c3699f5dbf5f17a0beec))

### Chores

- **release**: V0.1.10 [skip ci]
  ([`81023a6`](https://github.com/sadsfae/goldteeth/commit/81023a66e6764f56ded33c0ce6bb676a1d804f8b))


## v0.1.9 (2026-01-23)

### Bug Fixes

- Forcing release of v0.1.9
  ([`72491d8`](https://github.com/sadsfae/goldteeth/commit/72491d8356d94972214cfe1756e77411212de827))

### Chores

- **release**: V0.1.9 [skip ci]
  ([`d399e8b`](https://github.com/sadsfae/goldteeth/commit/d399e8b5667e5f74b53bcd1c8148c535e15bc5be))


## v0.1.8 (2026-01-22)

### Bug Fixes

- Forcing release of v0.1.8
  ([`957ab92`](https://github.com/sadsfae/goldteeth/commit/957ab92035de50bad74a8725256793fa9aeb9c8e))

### Chores

- **release**: V0.1.8 [skip ci]
  ([`96bab02`](https://github.com/sadsfae/goldteeth/commit/96bab028733844c0c3c817b75003173942237076))


## v0.1.7 (2026-01-22)

### Bug Fixes

- Bump again
  ([`c048607`](https://github.com/sadsfae/goldteeth/commit/c048607ff2711a76fac97e978e0ef3d0907aebd4))

- Bump small readme, see if this works
  ([`5263f1f`](https://github.com/sadsfae/goldteeth/commit/5263f1fe827c605df6c2f0609b0876a44ef5f9f5))

- Force next release cycle
  ([`6e11c22`](https://github.com/sadsfae/goldteeth/commit/6e11c2205a559a8d1ce6a06e32964e3985da17e1))

- Fully test pypi + gha automation
  ([`5921a4f`](https://github.com/sadsfae/goldteeth/commit/5921a4f9392951963d72d951f645d14d45ef3008))

- Readme change to trigger GHA
  ([`35a9d36`](https://github.com/sadsfae/goldteeth/commit/35a9d36f1602d8c35c4470f3cd84d1bf3f22d841))

- Sync git tags to trigger release
  ([`706dd3a`](https://github.com/sadsfae/goldteeth/commit/706dd3a419388363d1dffc07b6681302132dbaa2))

### Chores

- **release**: V0.1.7 [skip ci]
  ([`c524df6`](https://github.com/sadsfae/goldteeth/commit/c524df67be83e27dc3394d264c5c50da14529491))


## v0.1.6 (2026-01-22)

### Bug Fixes

- Sync git tags to trigger release
  ([`54f7a6c`](https://github.com/sadsfae/goldteeth/commit/54f7a6cce0f4bfddecc7068c3bf0d01c5d17feb8))

### Chores

- **release**: V0.1.6 [skip ci]
  ([`f51ca43`](https://github.com/sadsfae/goldteeth/commit/f51ca43fac8d325969ef53048edd3451bddb5b8b))


## v0.1.5 (2026-01-22)

### Bug Fixes

- Sync git tags to trigger release
  ([`0c2b230`](https://github.com/sadsfae/goldteeth/commit/0c2b23092b45d4649533e1dbed77e0a11fd44caa))

### Chores

- **release**: V0.1.5 [skip ci]
  ([`2a0b7d8`](https://github.com/sadsfae/goldteeth/commit/2a0b7d8d64b3290ad123d2b0d3660af20fc3a224))


## v0.1.4 (2026-01-22)

### Bug Fixes

- Sync git tags to trigger release
  ([`bcfe336`](https://github.com/sadsfae/goldteeth/commit/bcfe33664289dccf4a8468978dc73603372bc4f9))

### Chores

- **release**: V0.1.4 [skip ci]
  ([`8c7fea6`](https://github.com/sadsfae/goldteeth/commit/8c7fea68d27ad0497e962e2e0d8867986a9b4da0))


## v0.1.3 (2026-01-22)

### Bug Fixes

- Sync git tags to trigger 0.1.8 release
  ([`3c5ed21`](https://github.com/sadsfae/goldteeth/commit/3c5ed216c933212d78c325588e4c12b26060edc0))

### Chores

- **release**: V0.1.3 [skip ci]
  ([`930a2e8`](https://github.com/sadsfae/goldteeth/commit/930a2e8ef6cd842497491b2b771ab9cc0a9aad27))


## v0.1.2 (2026-01-22)

### Chores

- **release**: V0.1.2 [skip ci]
  ([`5262191`](https://github.com/sadsfae/goldteeth/commit/5262191fb3769819c54045331b3c0b2f3fa35f9c))


## v0.1.1 (2026-01-22)

### Chores

- **release**: V0.1.1 [skip ci]
  ([`f16a5a3`](https://github.com/sadsfae/goldteeth/commit/f16a5a3e663f84937b11c1dbc8bb1308c8fec06e))


## v0.1.0 (2026-01-22)

### Bug Fixes

- Direction arrow now shows for small %
  ([`63989f0`](https://github.com/sadsfae/goldteeth/commit/63989f03a7db4063094d5e345f5e0f5308ebb611))

- Handle after-hours market prices
  ([`ee31262`](https://github.com/sadsfae/goldteeth/commit/ee312622ba5e19d1d979d6a8b6ea3b406523ac10))

- Pypi package init
  ([`37adac7`](https://github.com/sadsfae/goldteeth/commit/37adac705a3000937037b03653413b590e87c4ee))

- Pypi syntax
  ([`a2e8ecd`](https://github.com/sadsfae/goldteeth/commit/a2e8ecddc6c5cc4e9c7f80bfab4c76aed98a81cd))

- Python-semantic-release needs env ref
  ([`2e5760b`](https://github.com/sadsfae/goldteeth/commit/2e5760b87ea66492b76d135fff9e06ee6b04480a))

- Readme
  ([`7a35f52`](https://github.com/sadsfae/goldteeth/commit/7a35f52760c74e00e7600165213c402fb5c96396))

- Repair pypi auth and sync version
  ([`2c8b1f4`](https://github.com/sadsfae/goldteeth/commit/2c8b1f49794a95a230b501f482eee2c8a625be8e))

- Testing pypi automation
  ([`784d857`](https://github.com/sadsfae/goldteeth/commit/784d85713e9af3d280a3d60140097c9f004065ec))

- Use proper error messages for crypto vs stocks
  ([`29860db`](https://github.com/sadsfae/goldteeth/commit/29860db7dd81ec9ed0be5f6b95590a504b4424d6))

* Also support using a coingecko API key if you have one.

### Chores

- Sync local version with pypi
  ([`0f0ffbf`](https://github.com/sadsfae/goldteeth/commit/0f0ffbf2f306e6633d78597f62c849842e755c08))

- Sync local version with pypi and update workflow
  ([`f74c75f`](https://github.com/sadsfae/goldteeth/commit/f74c75f1c76c51b937f0b19d0f9633bedca8419e))

### Features

- Add % above/below target in watch mode.
  ([`d09c69c`](https://github.com/sadsfae/goldteeth/commit/d09c69c84c07ee93124e10892a602ac787afc9a7))

* Also add a few more coins

fixes: https://github.com/sadsfae/pricewatch/issues/8

- Add desktop notifications to GUI
  ([`cd12e87`](https://github.com/sadsfae/goldteeth/commit/cd12e8722a2bb5ec5db4c559c0f98d146bb1aec4))

- Add notifications for CLI on Linux and OSX
  ([`fe94224`](https://github.com/sadsfae/goldteeth/commit/fe94224501a2f452433423b04ff496ac2a556ec1))

- Add tkinter GUI.
  ([`4cc5ea3`](https://github.com/sadsfae/goldteeth/commit/4cc5ea32c09581f8d3022765c23a1647a9d36081))

* Add a tkinter based python GUI (why not lol) * Also give it dark mode / light mode * Update docs

- Colored arrows, vol graph, lower % of vol
  ([`db99770`](https://github.com/sadsfae/goldteeth/commit/db99770af17513569ebf6b070f3b03fc744d53be))

feat: colored arrows, vol graph, lower % of vol.

* Add colors (green/red) and arrows * Make arrows blink when target below/above range is met in
  watch mode * Add volatility graph for volatility mode * Support volatility percentages as low as
  .001%

- Colored arrows, vol graph, lower % of vol.
  ([`2270532`](https://github.com/sadsfae/goldteeth/commit/227053224e64a2ae627c81692ef373893753c358))

* Add colors (green/red) and arrows * Make arrows blink when target below/above range is met in
  watch mode * Add volatility graph for volatility mode * Support volatility percentages as low as
  .001%

- Move to finnhub instead of polygon.
  ([`903b6f2`](https://github.com/sadsfae/goldteeth/commit/903b6f2d8da39540e08f85eacb70410bba505fce))

* Polygon free tier only gives yesterday prices * Use websockets and finnhub API

- Move to src/ structure, handle AH stock query
  ([`6c4d2e8`](https://github.com/sadsfae/goldteeth/commit/6c4d2e8013be3a5d22bf4c32d97211aa4d7ad563))

- Set entry point to main function
  ([`434e81d`](https://github.com/sadsfae/goldteeth/commit/434e81dbf5a69102fbdd16d2fdb44a59ad72bc8a))
