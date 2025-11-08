# Schneider Electric - Quick Sketch Dashboard

A Visio-like electrical equipment designer with automatic connection features, built using Schneider Electric's brand identity and theming.

![Dashboard Screenshot](https://github.com/user-attachments/assets/bd98b112-faeb-455c-9261-b27059f0cd12)

## Features

### 🎨 Schneider Electric Branding
- Full implementation of Schneider Electric brand palette
- Life Green (#3DCD58) primary color
- Professional color scheme with dark gray (#626469) and light gray (#9FA0A4)
- Consistent styling inspired by beta.html

### 🔧 Equipment Library
Six comprehensive equipment categories with 22+ electrical components:

1. **Power Generation**
   - Generator, Solar PV, Wind Turbine, Battery

2. **Transformation**
   - Power Transformer, Current Transformer, Voltage Transformer

3. **Protection**
   - Circuit Breaker, Disconnector, Fuse, Relay

4. **Distribution**
   - Busbar, Cable, Switchgear

5. **Loads**
   - Motor, Generic Load, Light

6. **Monitoring**
   - Energy Meter, RTU, Control Panel

### ⚡ Auto-Connection Feature
**The key innovation**: When you draw a line between two equipment items, they automatically connect!

**How it works:**
1. Drag equipment from the palette to the canvas
2. Click the "Connect" tool
3. Click on the first equipment
4. Click on the second equipment
5. **Connection automatically created with arrow!**

The connection:
- Follows equipment when moved
- Shows directional arrow
- Displays connection indicator animation
- Can be customized (color and width)

### 🎯 Drawing Tools
- **Select Tool**: Select and move equipment
- **Connect Tool**: Draw automatic connections between equipment
- **Pan Tool**: Navigate the canvas

### 🔍 View Controls
- **Zoom In/Out**: Scale the canvas (10% - 300%)
- **Fit to View**: Automatically frame all equipment
- **Grid Background**: Visual alignment guide

### 📋 Properties Panel
When you select equipment, edit:
- Name
- Tag/ID
- Voltage (kV)
- Current (A)
- Power (MW)
- Delete equipment

### 💾 Export & History
- **Export as PNG**: Save your diagram as an image
- **Undo/Redo**: Full history support (Ctrl+Z, Ctrl+Y)
- **Clear Canvas**: Start fresh
- **Auto-save**: Preserves work in browser storage

### ⌨️ Keyboard Shortcuts
- `Ctrl+Z` - Undo
- `Ctrl+Y` - Redo
- `Delete` - Delete selected element
- `Escape` - Deselect all

## Usage Guide

### Getting Started
1. Open `dashboard.html` in a modern web browser
2. The interface shows three main areas:
   - **Left**: Equipment palette
   - **Center**: Drawing canvas
   - **Right**: Properties panel

### Adding Equipment
1. Find the equipment in the left palette (organized by category)
2. Click and drag it onto the canvas
3. Drop it where you want it positioned
4. The equipment appears with its icon and name

### Connecting Equipment
1. Add at least two equipment items to the canvas
2. Click the **"Connect"** button in the toolbar (turns green)
3. Click on the **first equipment** (e.g., Generator)
4. Click on the **second equipment** (e.g., Motor)
5. A red connection line with an arrow automatically appears!
6. Status bar confirms: "Connected: Generator → Motor"

![Auto-Connection Demo](https://github.com/user-attachments/assets/916f94ab-b78c-4a78-9217-c544dd9a341b)

### Customizing Connections
Before connecting equipment:
- **Line Color**: Click the color picker to choose voltage color (red, orange, blue, purple, or custom)
- **Line Width**: Adjust the slider (1-8 pixels)

### Editing Equipment Properties
1. Click the **"Select"** tool
2. Click on any equipment
3. The properties panel (right) shows editable fields:
   - Name, Tag/ID
   - Electrical properties (Voltage, Current, Power)
4. Enter values as needed
5. Click **"Delete Element"** to remove equipment

### Moving Equipment
1. Select the equipment with the **Select** tool
2. Drag it to a new position
3. Connected lines automatically follow!

### Organizing Your Diagram
- **Pan**: Use the Pan tool to move around large diagrams
- **Zoom**: Use +/- buttons or mouse wheel to zoom
- **Fit to View**: Automatically centers all equipment

## Technical Details

### Technologies Used
- Pure HTML5, CSS3, and JavaScript (no dependencies!)
- HTML5 Canvas for drawing
- Drag-and-drop API for equipment
- LocalStorage for persistence

### Browser Compatibility
- Chrome/Edge (recommended)
- Firefox
- Safari
- Any modern browser with HTML5 Canvas support

### File Structure
```
dashboard.html          # Complete standalone application
Beta.html               # Reference for Schneider Electric theming
grid-whiteboard.html    # Reference for equipment features
```

## Design Philosophy

### Schneider Electric Identity
The dashboard follows Schneider Electric's design principles:
- **Life Green** as the primary action color
- Professional, clean interface
- Clear visual hierarchy
- Accessible and intuitive controls

### Inspired by Visio
- Simple drag-and-drop workflow
- Visual equipment library
- Smart connection detection
- Properties-based editing
- Export capabilities

### Quick Sketch Focused
- Fast equipment placement
- Automatic connections (no manual line drawing!)
- Minimal clicks required
- Immediate visual feedback
- No complex configuration needed

## Future Enhancements

Possible improvements:
- Save/Load diagram files (JSON format)
- Export to SVG for vector scaling
- Connection labels and annotations
- Multi-select and group operations
- Component rotation
- Grid snapping options
- More equipment types
- Connection validation rules
- Print layout optimization

## Credits

Created for Schneider Electric's Media Orchestrator project.

**Inspired by:**
- Beta.html - Schneider Electric theming and brand guidelines
- grid-whiteboard.html - Electrical equipment concepts

## License

Part of the Schneider-Media-Orchestrator project.

---

**Quick Tip**: The auto-connection feature is what makes this dashboard special - no need to manually draw lines! Just click Connect, click two equipment items, and they're automatically connected with a properly styled line and arrow. Perfect for quick electrical sketches! ⚡
