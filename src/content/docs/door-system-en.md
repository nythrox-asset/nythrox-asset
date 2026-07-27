---
title: Interactive Door System
source: README.md
version: Nythrox Interactive Door System 1.4.0
---

## What's new in 1.4.0

- The virtual hinge now pivots on the leaf face toward the swing side, like
  a real hinge knuckle (**Hinge At Leaf Face**, on by default). This
  continues the hinge refinement started with the 1.3.2 **Hinge inset**:
  the inset moves the pivot along the door width, the leaf face option
  removes the mid-thickness offset that visibly detached thick slabs from
  their frame.
- New **Demonstrated** hinge placement: the door rotates around the exact
  centre of the recorded closed to open motion, reproducing the recorded
  pose perfectly even on meshes with meaningless bounds.
- Open, close, and locked **sounds**, with a volume control.
- **Blueprint events**: On Door Opened, On Door Closed, and
  On Door Interaction Denied.
- **Locking**: a locked door refuses interaction, plays the locked sound,
  and fires the denied event.
- **Auto-close** after a configurable delay.
- Motion **easing**: Ease In Out by default for a hand-pushed feel; Linear
  and Ease Out are available.
- **Linked doors**: double doors and airlocks open and close together.
- **Replicated door state** for networked games, server authoritative (see
  the Multiplayer section, including its one honest limitation).
- **Detect frame** button: one click measures the real jamb of the opening
  and sets Hinge inset to match.
- The panel no longer overwrites settings that were changed outside of it
  (Details panel, scripts, undo) and refreshes automatically when the
  editor selection changes.

## Upgrading from 1.3.x

Doors created with 1.3.x load and work without re-recording poses. Two new
defaults intentionally change how existing doors move:

- Easing now defaults to **Ease In Out**. Set **Ease Mode** to Linear on
  the door component to restore the exact 1.3.x motion.
- The hinge now pivots at the leaf face by default. Disable
  **Hinge At Leaf Face** on the door component to restore the previous
  mid-thickness pivot.

Everything else (recorded poses, prompt settings, hinge side, hinge inset)
is preserved as recorded.

## Installation

1. Close Unreal Editor.
2. Copy the complete `NythroxDoorSystem` folder into
   `<YourProject>/Plugins/`.
3. Open the project, enable **Nythrox Interactive Door** if Unreal asks, then
   restart the editor.
4. Open **Tools > Nythrox Interactive Door**.

The plugin contains an Editor module and a Runtime module. Interactive doors
require the Runtime module in the final game. The archive contains the Win64
Editor binaries and the C++ sources; packaging a game may compile the runtime
module for the selected game configuration.

## Before creating a door

Select only the moving door parts and their collision meshes/components.
Do not select the wall, frame, floor, or any fixed surrounding geometry. A
double door should be created as two independent doors; afterwards, add each
leaf to the other's **Linked Doors** list on the door component so both
leaves open and close together.

## Door settings

| Control | Default | Purpose |
|---|---:|---|
| Interaction key | E | Key displayed by the prompt and handled by the door. |
| Distance (cm) | 250 | Maximum interaction distance from the player to the visible bounds. |
| Move duration (s) | 0.65 | Open/close animation duration. |
| Prompt vertical offset (cm) | 0 | Signed vertical offset from the center of the visible bounds. |
| Hinge edge | Automatic | Automatic, Left, or Right virtual hinge. |
| Hinge inset (cm) | 0 | Move the virtual hinge inward from the selected slab edge; negative values move it outward. |
| Detect frame (button) | - | Measures the real jamb of the opening around the selected door and sets Hinge inset to that value. Nothing changes if no wall is found. |
| Rotate around the door edge | On | Use the virtual edge hinge for rotating doors. |
| Show [key] prompt in game | On | Display the localized interaction prompt in range. |
| Starts open | Off | Start the game in the recorded open state. |

The panel refreshes automatically when the editor selection changes. Press
**Refresh** to force a recount of the selected mesh components and
collisions at any time.

**Detect frame** measures the opening by scanning the world-space bounding
boxes (AABB) of the Static Mesh actors flanking the door leaf. It
deliberately does not use a line trace: the visual meshes produced by the
Roblox export pipeline carry no collision (NoCollision), so a trace would
either hit nothing or hit a coarse proxy hull instead of the visible wall.
The wall pieces beside the leaf therefore have to be Static Mesh actors
whose bounds reach the opening. If no flanking wall is found, the hinge
inset is left untouched.

## Guided workflow

1. Select every moving visual mesh and collision component.
2. Choose the settings and press **Create door**. The tool creates
   `BP_InteractiveDoor`, replaces the sources, makes its components Movable,
   and records the initial closed pose.
3. If needed, correct the actor's closed transform and press
   **Record closed**.
4. Move and/or rotate the entire door actor to its desired open pose, then
   press **Record open**. The actor returns to the closed pose automatically.
5. Use **Preview closed**, **Preview open**, or **Preview animation** without
   starting Play mode.
6. If Automatic opens around the wrong side, choose Left or Right and preview
   again.
7. If the slab extends into the wall, press **Detect frame** to measure the
   real jamb automatically, or increase **Hinge inset** manually until the
   virtual pivot matches the visible jamb. Previewing applies the new value
   immediately; recording the open pose again is not required.
8. Test the interaction in Play mode by approaching the door and pressing the
   configured key.

**Undo door** restores the source actors for the latest door creation when its
operation data is still available. Unreal's normal Undo is also supported for
the active transaction.

## How the virtual hinge works

The tool does not move or repair the imported mesh pivot. It examines the
largest visible door slab, detects its two vertical side edges, and builds a
virtual hinge on the selected side.

- **Automatic** compares the recorded open pose with the two possible arcs and
  chooses the best matching edge.
- **Left** and **Right** force a side when the automatic preview is wrong.
- **Hinge inset** shifts the resolved edge toward the centre of the slab in
  world centimetres. A negative value shifts it outside the slab. `0` preserves
  the original edge-detection behaviour.
- **Hinge At Leaf Face** (component setting, on by default since 1.4.0) moves
  the pivot from mid-thickness to the slab face toward the swing side, like a
  real hinge knuckle. On thick slabs the mid-thickness pivot visibly detached
  the open leaf from its frame; disable the option to restore it.
- **Hinge Placement** set to **Demonstrated** (component setting) skips edge
  detection entirely and rotates the door around the exact centre of the
  recorded closed to open motion. If the open pose was placed accurately,
  this reproduces it perfectly and works even when the mesh bounds are
  meaningless (placeholder cubes). It falls back to the detected slab edge
  when the recorded rotation is smaller than about `2` degrees.
- For a rotation greater than approximately `0.5°`, the door center follows a
  circular arc around the virtual edge.
- With no meaningful rotation, the exact recorded translation is preserved,
  which supports sliding doors.
- If no reliable door edge can be found, the component falls back to the
  classic transform interpolation.

This makes the animation independent from a bad mesh pivot and prevents the
door center from following a straight chord through the wall.

## Sliding doors

The same workflow supports doors that translate instead of rotate. Record
the open pose by moving the door actor without rotating it (any rotation
below `0.5` degrees counts as none): the component then skips the virtual
hinge and interpolates the recorded translation linearly, with the selected
easing still applied. No hinge settings are needed for a sliding door, and
two sliding panels can be paired with **Linked Doors** like any double door.

## Component settings added in 1.4.0

All new settings live on the `NythroxDoorComponent` of the door Blueprint
(`BP_InteractiveDoor`), in the Details panel under the listed category.
Every one of them is also readable and writable from Blueprint.

| Property | Category | Default | Purpose |
|---|---|---:|---|
| Locked (`bLocked`) | Nythrox Door > Interaction | Off | A locked door refuses interaction, plays Locked Sound, and fires On Door Interaction Denied. It does not move the door. |
| Auto Close Delay (`AutoCloseDelay`) | Nythrox Door > Interaction | 0 s | Seconds the door stays fully open before closing itself. `0` means never. |
| Linked Doors (`LinkedDoors`) | Nythrox Door > Interaction | empty | Other door actors toggled together with this one (double doors, airlocks). Links are not followed transitively, so two leaves may simply reference each other. |
| Ease Mode (`EaseMode`) | Nythrox Door > Motion | Ease In Out | Easing applied to the open/close motion: Linear, Ease Out, or Ease In Out. Ease In Out feels like a hand-pushed door. |
| Ease Exponent (`EaseExponent`) | Nythrox Door > Motion | 2.0 | Strength of the easing curve, from `1` (almost linear) to `5`. |
| Hinge Placement (`HingePlacement`) | Nythrox Door > Motion | Slab Edge (detected) | Slab Edge uses the detected door edge, refined by Hinge inset and Hinge At Leaf Face. Demonstrated uses the exact rotation centre of the recorded poses. |
| Hinge At Leaf Face (`bHingeAtLeafFace`) | Nythrox Door > Motion | On | Places the hinge on the slab face toward the swing side instead of at mid-thickness. Disable for the 1.3.x pivot. |
| Open Sound (`OpenSound`) | Nythrox Door > Audio | None | Played at the door location when it starts opening. |
| Close Sound (`CloseSound`) | Nythrox Door > Audio | None | Played at the door location when it starts closing. |
| Locked Sound (`LockedSound`) | Nythrox Door > Audio | None | Played when interaction is refused because the door is locked. |
| Sound Volume (`SoundVolume`) | Nythrox Door > Audio | 1.0 | Volume multiplier for the three sounds, `0` to `2`. `0` mutes them. |
| Replicate Door State (`bReplicateDoorState`) | Nythrox Door > Network | On | Replicates the open/closed state to clients in networked games; the server stays authoritative. See Multiplayer. |

The component also exposes three assignable events under
**Nythrox Door > Events**:

- **On Door Opened**: fired when the door finishes opening (gameplay only).
- **On Door Closed**: fired when the door finishes closing (gameplay only).
- **On Door Interaction Denied**: fired when interaction is refused because
  the door is locked.

Sounds and events fire during gameplay, not during editor previews.

## Multiplayer

With **Replicate Door State** enabled (the default), the open/closed state
of the door is replicated from the server to every client. The server is
authoritative; each machine animates the movement locally and plays its own
sounds and events. A listen server host interacts with doors out of the box,
because the host is the server.

The honest limitation: a door placed in the level has no owning connection,
so an interaction triggered on a remote client cannot reach the server
through the door component itself. Route the request through an actor the
client owns; it is one line of Blueprint: on your game's Character or
PlayerController, a Run-on-Server custom event that calls `SetDoorOpen` or
`ToggleDoor` on the door. The resulting state then replicates back to every
client automatically.

Two related notes:

- The built-in `[E]` key polling uses the first local Player Controller. On
  a remote client it triggers the interaction locally, which, as explained
  above, cannot reach the server by itself; use the Blueprint routing for
  client-driven doors in networked games.
- `Locked` is a plain property and is not replicated. In networked games,
  set it on the server (or on every machine) and gate interactions through
  `TryInteract` so the lock is respected.

## Prompt behavior

The prompt is always rendered in screen space, centered on the visible door
bounds, with the configured signed vertical offset. The door mesh therefore
cannot cut or occlude the text.

The runtime prompt follows English, French, German, or Spanish and displays the
selected key, for example `[E] Open`, `[E] Close`, `[E] Ouvrir`, or
`[E] Fermer`. Other languages fall back to English.

## Saving an interactive or static door

| Keep interactive animation | Save door result |
|---|---|
| On | Saves the existing interactive Blueprint with its Runtime component, poses, prompt, and input settings. |
| Off | Creates a separate `BP_StaticDoor` with meshes, materials, transforms, and collisions, but no Runtime component, prompt, or interaction. |

Saving a static version does not delete or convert the interactive actor
already present in the scene. To save the static door closed, press
**Preview closed** before **Save door**.

## Collision and runtime behavior

- Selected Static Mesh Components, including hidden `RBX_OWNED_COLLISION`
  components, move with the door.
- Their collision profiles and enabled collision remain intact.
- Movement uses teleport-style transform updates without sweep. The door does
  not automatically stop when a player or obstacle blocks its path.
- Interaction distance is measured to the visible bounds rather than to the
  actor or mesh pivot.
- The built-in key polling uses the first local Player Controller. Door
  state replication for networked games is described in the Multiplayer
  section, including how a remote client must route its interaction.

## Blueprint API

The Runtime component exposes:

- `TryInteract` for custom input systems; it respects `Locked` and fires
  On Door Interaction Denied when refused;
- `ToggleDoor` to alternate open/closed states;
- `SetDoorOpen` to request a specific state;
- `IsDoorOpen` to read the current state;
- `SetLocked` and `IsLocked` to control and read the lock without moving
  the door;
- the assignable events On Door Opened, On Door Closed, and
  On Door Interaction Denied (see Component settings added in 1.4.0).

## Existing doors and panel settings

Panel fields are fully applied when a door is created. For an existing door,
edit its component in the Details panel for general runtime values. The hinge
choice is also read and applied by the Nythrox panel during hinge previews and
recording.

Since 1.4.0 the panel refreshes automatically when the editor selection
changes, and its commands only write the hinge fields you actually edited
since the last refresh. A value changed elsewhere in the meantime (Details
panel, a script, another tool, or undo) is read back instead of being
overwritten by a stale copy of the panel.

Doors created by older versions without hinge data automatically resolve a
virtual edge at runtime. Former world-space prompts are forced to readable
screen space.

## Limitations and troubleshooting

| Problem | Check |
|---|---|
| The panel is missing | Enable the plugin, restart Unreal, then use the Tools menu. |
| Create door is disabled | Select only valid moving Static Mesh actors/components and press Refresh. |
| The door opens through the wrong side | Select Left or Right under Hinge edge, then Preview animation. |
| The hinge is inside the wall | Press Detect frame, or increase Hinge inset until the preview pivots on the visible jamb. You do not need to record the open pose again. |
| Detect frame reports no wall | The scan uses the bounding boxes (AABB) of Static Mesh actors, not traces. The wall pieces beside the leaf must be Static Mesh actors whose bounds reach the opening. |
| Pressing the key does nothing | Verify Play mode, interaction distance, the configured key, that the Runtime plugin is enabled, and that Locked is off. |
| The door refuses to open and plays a sound | The door is Locked; call SetLocked(false) or clear the flag on the component. |
| The motion feels different after upgrading | See Upgrading from 1.3.x: set Ease Mode to Linear and/or disable Hinge At Leaf Face. |
| A remote client cannot open the door | Expected for level-placed doors; route the interaction through the server as shown in the Multiplayer section. |
| The prompt is too high or low | Change Prompt vertical offset; positive and negative values are supported. |
| A static door is saved open | Preview closed before saving the static version. |

Menu, panel, and runtime prompt labels support English, French, German, and
Spanish. Some Python notifications may remain in English or French.
