from pydantic import BaseModel, validator
from pydantic.dataclasses import dataclass
from typing import List

class LabelName(BaseModel):
    long: str
    short: str


LABELS = (
 LabelName(long='Centrosome', short='Centrosome'),
 LabelName(long='Centrosome Distal Appendage', short='Controsome D App'),
 LabelName(long='Centrosome Subdistal Appendage', short='Controsome SD App'),
 LabelName(long='Chromatin', short='Chromatin'),
 LabelName(long='Extracellular Space', short='ECS'),
 LabelName(long='Endosomal Network', short='Endo'),
 LabelName(long='Endosome Membrane', short='Endo mem'),
 LabelName(long='Endoplasmic Reticulum', short='ER'),
 LabelName(long='Endoplasmic Reticulum Membrane', short='ER mem'),
 LabelName(long='Endoplasmic Reticulum Exit Site', short='ERES'),
 LabelName(long='Endoplasmic Reticulum Exit Site Membrane', short='ERES mem'),
 LabelName(long='Euchromatin', short='E Chrom'),
 LabelName(long='Nucleolus-associated Euchromatin', short='N-E Chrom'),
 LabelName(long='Golgi', short='Golgi'),
 LabelName(long='Golgi Membrane', short='Golgi Mem'),
 LabelName(long='Heterochromatin', short='H Chrom'),
 LabelName(long='Nucleolus-associated Heterochromatin', short='N-H Chrom'),
 LabelName(long='Lipid Droplen', short='LD'),
 LabelName(long='Lipid Droplet Membrane', short='LD mem'),
 LabelName(long='Lysosome', short='Lyso'),
 LabelName(long='Lysosome membrane', short='Lyso mem'),
 LabelName(long='Microtubule', short='MT'),
 LabelName(long='Microtubule outer', short='MT out'),
 LabelName(long='Mitochondria', short='Mito'),
 LabelName(long='Mitochondria Membrane', short='Mito mem'),
 LabelName(long='Mitochondria Ribosome', short='Mito Ribo'),
 LabelName(long='Nuclear Envelope', short='NE'),
 LabelName(long='Nuclear Envelope', short='NE mem'),
 LabelName(long='Nuclear Pore', short='NP'),
 LabelName(long='Nuclear Pore outer', short='NP out'),
 LabelName(long='Plasma Membrane', short='PM'),
 LabelName(long='Nucleolus', short='Nucleolus'),
 LabelName(long='Nucleus', short='Nucleus'),
 LabelName(long='Ribosome', short='Ribo'),
 LabelName(long='Vesicle', short='Vesicle'),
 LabelName(long='Vesicle membrane', short='Vesicle mem'),
)

class AnnotationState(BaseModel):
    present: bool
    annotated: bool


class Label(BaseModel):
    name: LabelName
    value: int
    annotationState: AnnotationState

    @validator('name')
    def valid_label_name(cls, v):
        if v not in LABELS:
            raise ValueError(f'{v} is not in the collection of valid labels: {LABELS}')
        return v

class Instances(BaseModel):
    labels: List[Label]
