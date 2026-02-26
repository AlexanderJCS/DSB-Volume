import ORSModel
from PyQt6.QtCore import QThread, pyqtSignal

from typing import Optional

from . import meshhelper
from .. import payload

class PreprocessingWorker(QThread):
    update_label: pyqtSignal = pyqtSignal(str)
    finished: pyqtSignal = pyqtSignal()

    def __init__(self, filepath: str, dragonfly_mesh: ORSModel.ors.FaceVertexMesh, psds: Optional[ORSModel.ors.MultiROI],
                 annotations: Optional[ORSModel.ors.Annotation]):
        super().__init__()

        self.dragonfly_mesh = dragonfly_mesh
        self.psds = psds
        self.annotations = annotations
        self.filepath = filepath

    def run(self):
        try:
            self.update_label.emit("Converting Mesh")
            mesh = meshhelper.ors_to_trimesh(self.dragonfly_mesh)

            annotations_pcd = None
            if self.annotations is not None:
                self.update_label.emit("Saving Annotations")
                annotations_pcd = meshhelper.annotations_to_list(self.annotations)

            psds_mesh = None
            if self.psds is not None:
                self.update_label.emit("Saving MultiROI")
                psds_mesh = meshhelper.multiroi_to_mesh(self.psds)

            self.update_label.emit("Skeletonizing Mesh")
            skeleton = meshhelper.skeletonize_mesh(mesh)

            self.update_label.emit("Saving to File")
            payload.pld_save(
                payload.Payload(
                    dendrite_mesh=mesh,
                    skeleton=skeleton,
                    annotations=annotations_pcd,
                    psds=psds_mesh
                ),
                filepath=self.filepath
            )
            self.update_label.emit("Saved!")
        except Exception as e:
            self.update_label.emit(f"An unexpected error occurred while preprocessing")
            raise e
        finally:
            self.finished.emit()
