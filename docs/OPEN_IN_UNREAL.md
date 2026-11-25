# Inspecting the archived assets in UE 5.4

[← Overview](../README.md)

The `unreal/Content` directory is an asset archive, not a complete packaged VR
application. Use a separate inspection project so the original archive remains
unchanged.

1. Create a **Blank C++ project in Unreal Engine 5.4**, or use a compatible
   existing inspection project.
2. Install the matching **VR Expansion Plugin 5.4** release. Follow the
   [upstream 5.4 installation instructions](https://github.com/mordentral/VRExpansionPlugin/blob/5.4-Locked/README.md)
   for plugin compilation and project dependencies. The archived classes use
   `VRCharacter`, `VRPlayerController` and `GrippableStaticMeshActor` from this
   plugin.
3. Enable Enhanced Input and OpenXR as needed by the inspection project. Compile
   the project and plugin before loading the custom Blueprint classes.
4. With the editor closed, copy `unreal/Content/Project_0412` into the inspection
   project's `Content` directory. Preserve its name and internal paths because
   the assets reference `/Game/Project_0412/...`.
5. Open the project and inspect the four Blueprint classes and input-mapping
   context. Review compiler messages and node connections before attempting
   play or headset use.
6. Open `Content/Project_0412/MAPS/VRtest_0412`. This is the retained test map;
   the four final architectural experiment maps are not included in this archive.

The original descriptor identifies UE 5.4 and enables OpenXR. Its local editor
extensions and machine-specific configuration are not required to document the
Blueprint source and have not been copied into this repository.

## Verification status

| Check | Status |
| --- | --- |
| Original asset copies and SHA-256 hashes | Checked |
| Referenced project assets present in the archive | Checked by static inspection |
| Blueprint symbols and package references | Recorded |
| Blueprint compilation in UE 5.4 | Not run |
| OpenXR/Pico headset interaction | Not run |
| Final scoring build and four experimental maps | Not recovered in the supplied archive |
