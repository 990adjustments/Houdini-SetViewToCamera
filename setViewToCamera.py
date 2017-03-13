"""Set the current view to the selected camera.

Usage:

First Select a camera in your scene.
"""

def saveViewportToCam(camera_node):
    desktop = hou.ui.curDesktop()
    scene_viewer = desktop.paneTabOfType(hou.paneTabType.SceneViewer)
    viewport = scene_viewer.curViewport()
    
    # set camera
    viewport.saveViewToCamera(camera_node)

try:
    # camera selection
    cam = hou.selectedNodes()[0]
    saveViewportToCam(cam)
    hou.ui.setStatusMessage("Camera view set", severity=hou.severityType.Message)
    
except IndexError:
    hou.ui.displayMessage("Please select a camera.", severity=hou.severityType.Error, title="No camera selected")