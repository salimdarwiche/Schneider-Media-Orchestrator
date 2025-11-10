# Agenda Export/Import Feature

## Overview
The Schneider Media Orchestrator now supports exporting and importing complete agenda configurations with all media references, allowing you to save, share, and restore presentation setups.

## Features

### Export Agenda
- Saves complete agenda configuration to a JSON file
- Includes all agenda slots with times, titles, and subtitles
- Captures media file references (videos and presentations)
- Preserves custom names and settings
- Saves app configuration (mode, menu position, time zone, etc.)

### Import Agenda
- Restores agenda from a JSON file
- Automatically maps media items to loaded files by filename
- Handles missing files gracefully
- Restores all app settings and configurations
- Works with the same or different media files

## How to Use

### Exporting an Agenda

1. Open the **Settings** dialog (click the settings button)
2. Go to the **General** tab
3. Configure your agenda in Meeting mode:
   - Add agenda slots using "+ 15 min", "+ 30 min", or "+ 1 hour" buttons
   - Fill in titles and times
   - Assign videos and presentations to slots
4. Click the **Export Agenda** button
5. A JSON file will be downloaded with the filename format: `schneider-agenda-YYYY-MM-DD.json`

### Importing an Agenda

1. Open the Schneider Media Orchestrator
2. Load your video and presentation files (same filenames as when exported)
3. Open the **Settings** dialog
4. Go to the **General** tab
5. Click the **Import Agenda** button
6. Select your previously exported JSON file
7. The agenda will be restored with all settings and media items automatically mapped

## Important Notes

### File Mapping
- Media items are mapped by **filename** when importing
- If you import with different files, ensure the filenames match
- Missing files will be skipped (agenda slots remain but without those media items)
- Custom names will be restored for matching files

### Portability
- Export files are plain JSON and can be shared with others
- Others can import your agenda if they have files with matching names
- Great for preparing presentations in advance or creating templates

### App Settings Restored
When importing, these settings are restored:
- App mode (Presentation or Meeting)
- Menu position (if not in Meeting mode)
- Time zone
- Loop settings
- Sort modes for videos and presentations

## Example Use Cases

1. **Prepare in Advance**: Create your agenda at home, export it, then import at the venue with the actual media files
2. **Templates**: Create reusable agenda templates for recurring meetings
3. **Backup**: Export your agenda before making changes, so you can restore if needed
4. **Sharing**: Share agenda configurations with colleagues who have the same media files

## Troubleshooting

### Media Items Not Appearing After Import
- Ensure the media files have the **exact same filenames** as when exported
- Load the media files **before** importing the agenda
- Check the exported JSON to see what filenames were saved

### Settings Not Restored
- Verify you're using a valid JSON file exported from this tool
- Check that the JSON has a "version" and "agendaSlots" property

### Import Button Not Responding
- Ensure you've selected a valid .json file
- Check browser console for error messages
- Try exporting a new agenda and importing it to test

## Technical Details

### JSON File Structure
```json
{
  "version": "1.0",
  "exportDate": "2025-11-10T18:03:01.586Z",
  "appSettings": {
    "menuPos": "left",
    "appMode": "meeting",
    "timeZone": "Europe/Paris",
    ...
  },
  "videos": [
    {
      "name": "intro-video.mp4",
      "_customName": "Introduction",
      "_id": "unique-id",
      "_addedAt": 1699635781586
    }
  ],
  "presentations": [...],
  "agendaSlots": [
    {
      "id": "slot-id",
      "title": "Opening Remarks",
      "subtitle": "Welcome",
      "start": "10:00",
      "end": "10:15",
      "items": [
        {
          "id": "media-id",
          "type": "video",
          "mediaName": "intro-video.mp4",
          "_customName": "Introduction"
        }
      ]
    }
  ]
}
```

## Version History
- **v1.0** (2025-11-10): Initial implementation with full export/import support
