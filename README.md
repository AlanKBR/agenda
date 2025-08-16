# Agenda

a vibecoded fork of fullcallendar

## Overview

This repo contains a Flask-based agenda/calendar app that integrates FullCalendar assets for a timeline/resource view UI. It includes local static assets and example migrations.

## Quick start

- Python 3.12+
- Optional: a virtualenv (recommended)

### Setup

1. Create and activate a virtual environment
   
   - Windows (PowerShell)
     
     ```powershell
     python -m venv venv
     ./venv/Scripts/Activate.ps1
     ```

2. Install dependencies
   
   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Run the app
   
   ```powershell
   python app.py
   ```

Then open the URL shown in the terminal (typically http://127.0.0.1:5000/).

## Notes

- Instance databases are kept in `instance/` and are ignored by git by default.
- Vendor assets for FullCalendar are kept under `static/fullcalendar/` and `fullcalendar-scheduler-6.1.18/` (with upstream LICENSE included).

## Credits

- FullCalendar and Scheduler assets are © their respective authors. See their LICENSE files shipped in `fullcalendar-scheduler-6.1.18/`.
