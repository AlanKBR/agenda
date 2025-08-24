# Agenda dependencies manifest

Python runtime (install with pip):
- Flask (>=3.0,<4.0)
- Flask-SQLAlchemy (>=3.1,<4.0)
- SQLAlchemy (>=2.0,<3.0)
- python-dateutil (>=2.9,<3.0)
- requests (>=2.31,<3.0)

Node packages used (install with npm/yarn/pnpm):
- flatpickr (^4.6.13)
- fullcalendar (^6.1.18) and plugins:
  - @fullcalendar/daygrid
  - @fullcalendar/interaction
  - @fullcalendar/list
  - @fullcalendar/multimonth
  - @fullcalendar/resource-timeline
  - @fullcalendar/timegrid
  - @fullcalendar/timeline
- js-beautify (^1.15.4) [dev/formatting]
- terser (^5.43.1) [build/minify]

Notes:
- The UI currently ships minified assets under `agenda/static/fullcalendar` and `agenda/static/vendor/flatpickr`. If you prefer installing from npm and copying assets, the scripts in `package.json` show how to sync Flatpickr assets.
- For reuse as a package, consider generating assets during build and excluding vendored `.min.*` files from VCS.