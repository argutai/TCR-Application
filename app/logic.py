import os
import pandas as pd

absolute_path = os.path.dirname(__file__)

path = os.path.join(absolute_path, 'static/figures/KCL_bulk/Sample_bubbles')
bubble_files = os.listdir(path)

posts = [
    {
        'graph_name': 'Bar chart - Clonotype count per sample',
        'legend': 'legend - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae nulla dolor.\n',
        'image_path': 'static/figures/KCL_bulk/clonotype_count/patient.png'
    },
    {
        'graph_name': 'Bubble plot - Proportion of clonotypes per sample',
        'legend': 'legend - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae nulla dolor.\n',
        'image_path': 'static/figures/KCL_bulk/clonotype_proportions/barchart.png'
    }
]

path = os.path.join(absolute_path, 'static/metadata.txt')
metadata = pd.read_csv(path, delimiter='\t')



class Figure:
    def __init__(self, patient_id, sample, protocol, pool_id, type):
        self.patient_id = patient_id
        self.Sample = sample
        self.protocol = protocol
        self.pool_id = pool_id
        self.type = type

class Patient:
    def __init__(self, patient_id, hormad1, genomics, figures):
        self.patient_id = patient_id
        self.hormad1 = hormad1
        self.genomics = genomics
        self.figures = figures

def initialise_patients():
    patient_names = (list(set(metadata['patient_id'])))
    patient_list = []
    for patient in patient_names:
        patient_figs = []
        samples = metadata['Sample'][metadata['patient_id']==patient]
        for sample in samples:
            protocol = metadata['protocol'][metadata['Sample']==sample].values[0]
            patient_id = metadata['patient_id'][metadata['Sample']==sample].values[0]
            pool_id = metadata['pool_id'][metadata['Sample']==sample].values[0]
            type = metadata['type'][metadata['Sample']==sample].values[0]
            patient_figs.append(Figure(patient_id, sample, protocol, pool_id, type))
        pat = metadata[metadata['patient_id'] == patient]
        hormad1 = list(set(pat['HORMAD1']))[0]
        genomics = list(set(pat['Genomics']))[0]
        new_patient = Patient(patient, hormad1, genomics, patient_figs)
        patient_list.append(new_patient)
    return patient_names, patient_list

patient_names, patient_list = initialise_patients()
obj = patient_list[patient_names.index('KCL725')]
# print(obj.genomics)






# patient = 'KCL717'
# vars()[patient]
# print(vars()[patient].figures[0].pool_id)