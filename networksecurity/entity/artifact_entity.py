from dataclasses import dataclass  #convenient way of creating a class whose main purpose is to store related data.

# artifact is an output produced by one stage that is passed to another stage

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str #If the training data fails validation, its location can be stored here
    invalid_test_file_path: str
    drift_report_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str #points to the preprocessing object
    transformed_train_file_path: str
    transformed_test_file_path: str

@dataclass
class ClassificationMetricArtifact:
    f1_score: float
    precision_score: float #model predicted as positive, how many were actually positive?
    recall_score: float #Of all the actual positive cases, how many did the model correctly detect?
    
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
    train_metric_artifact: ClassificationMetricArtifact #model's performance on the training data.
    test_metric_artifact: ClassificationMetricArtifact
