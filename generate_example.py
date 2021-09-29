from annotation_metadata.models.crop import Instances, Label, LabelName

labels = [Label(value=0, 
                name=LabelName(long='Extracellular Space', short='ECS'), 
                annotationState = {'present' : True, 'annotated': True}),]
instances = Instances(labels=labels)

if __name__ == '__main__':
    print(instances.json(indent=2))