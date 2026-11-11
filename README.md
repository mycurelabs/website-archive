# MYCURE Website Archive

Full-page screenshots of every major version of the MYCURE website, from the 2018 launch to today, with a short history of each version. Published with GitHub Pages.

Each version was checked out from [mycurelabs/mycure.md](https://github.com/mycurelabs/mycure.md), run locally on a toolchain from its era, and captured at 1440 px wide.

## Layout

- `screenshots/<version>/` holds the full-resolution JPGs that the zoom viewer opens.
- `thumbs/<version>/` holds the cropped card thumbnails.
- `build.py` holds the version histories and generates `index.html` and `versions/*.html`.
- `assets/` holds the styles, the zoom viewer script and the MYCURE logo.

## Updating

Edit `VERSIONS` in `build.py`, add the screenshots, and then run:

```sh
python3 build.py
```

Preview the site locally with `python3 -m http.server` and commit the generated HTML.
