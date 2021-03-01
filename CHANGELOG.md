# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- [pconway.render.play] Statements to change if window size has changed.
  Recompute the population and restart the game when it happens.


## [1.0.3] 2021-02-28
### Added
- [pconway.core.gameoflife.compute_cell_next_state] Compute the next state
  of a single cell.

### Changed
- [pconway.render.play] and [pconway.clitools.gameoflife] Changed default
  alive_char from "o" to "." because it looks better.
- [setup.py] Read version number from pconway/__version__.py instead of
  separately definition.
- [pconway.tests.test_gameoflife.py] Changed random_matrix to accommodate
  recent changes.
- [pconway.core.gameoflife.mutation] Draw random number from np.random.binomial
  and use xor gate to perform mutation instead of using nested for-loops.
- [pconway.core.gameoflife.get_alive_neighbours] Use np.count_nonzero to count
  number of alive cells instead of using nested for-loops.
- [pconway.core.gameoflife.compute_next_state] Use np.vectorize and
  pconway.core.gameoflife.compute_cell_next_state (new) to compute
  next state of a matrix instead of using nested for-loops and statements.
- Put tests in the module instead.
- [pconway.render.play] Compute wait time efficiently by using time.sleep()

### Fixed
- Typos in CHANGELOG.md
- Formatting according to PEP 8


## [1.0.2] 2021-02-22
### Removed
- __init__.py in pconway/tests/ so it's not interpreted as a module.


## [1.0.1] 2021-02-22
### Fixed
- Images links PyPI


## [1.0.0] 2021-02-21
### Added
- pconway.clitools.gameoflife() Play Conway's game of life from commandline.
- pconway.render.play Play Conway's game of life and render the game using
  Curses.
- pconway.core.custom_game The class library for some defined games.
  Added a game mode where the initial matrix is randomized.
- pconway.core.game The base class for a game of Conway's game of life.
- pconway.core.gameoflife.mutation() that flips 1 or 0 randomly.
- [pconway.core.gameoflife] Functions that convert matrices of 1 and 0
  according to the Conway's game of life.
- This library using mypythonlibrary as template
- This CHANGELOG file to hopefully serve as an evolving example of a
  standardized open source project CHANGELOG.

[Unreleased]: https://github.com/terrencetec/pconway
[1.0.3]: https://github.com/terrencetec/pconway/releases/tag/v1.0.3
[1.0.2]: https://github.com/terrencetec/pconway/releases/tag/v1.0.2
[1.0.1]: https://github.com/terrencetec/pconway/releases/tag/v1.0.1
[1.0.0]: https://github.com/terrencetec/pconway/releases/tag/v1.0.0
